
import json
import couchdb
from flask import Flask, render_template, jsonify
from flask_cors import CORS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Define the list of node IPs in the cluster
cluster_nodes = ["172.26.132.54", "172.26.133.32", "172.26.130.9"]

admin = 'admin'
password = 'qazwsxedc'

# Initialize a CouchDB server object for each node
node_servers = [f"http://{admin}:{password}@{node_ip}:5984/" for node_ip in cluster_nodes]

for node in node_servers:
    try:
        server = couchdb.Server(node)
        print('Connected to CouchDB node:', node)
        break  # Exit loop if a healthy node is found
    except couchdb.http.Unauthorized:
        print('Unauthorized access to CouchDB node:', node)
    except couchdb.http.PreconditionFailed:
        print('Precondition failed for CouchDB node:', node)
    except couchdb.http.ServerError:
        print('Error connecting to CouchDB node:', node)
else:
    # Executed if no healthy node is found
    print('No healthy CouchDB nodes found.')
    exit()


app = Flask(__name__)
CORS(app)

# get result - twi
def api_0(state, scenario):
    db = server['twitter1']
    view = db.view(f'{scenario}/new-view', startkey=[state], endkey=[state, {}],group_level = 2)
    
    sua = []
    value_media = []
    for row in view:
        sua.append(row['key'][1])
        value_media.append(row['value']['percentage'])
    
    d = {'sua': sua, 'value_media': value_media}
    df = pd.DataFrame(data=d)
    
    return df

# get result - sudo - agism
def api_sudo_agism(state):
    db = server['sudo']
    view = db.view('agism/new-view', startkey=[state], endkey=[state, {}])
    
    sua = []
    value_official = []
    for row in view:
        sua.append(row['key'][1])
        value_official.append(row['value']['ageing_population_percentage'])
    
    d = {'sua': sua, 'value_official': value_official}
    df = pd.DataFrame(data=d)
    
    return df

# get result - sudo - sexism
def api_sudo_sexism(state):
    db = server['sudo']
    view = db.view('sexism/new-view', startkey=[state], endkey=[state, {}])
    
    sua = []
    value_official = []
    for row in view:
        sua.append(row['key'][1])
        value_official.append(row['value']['gender_ratio'])
    
    d = {'sua': sua, 'value_official': value_official}
    df = pd.DataFrame(data=d)
    
    return df

# get result - sudo - unemployment
def api_sudo_unemployment(state):
    db = server['sudo']
    view = db.view('unemployment/new-view', startkey=[state], endkey=[state, {}])
    
    sua = []
    value_official = []
    for row in view:
        sua.append(row['key'][1])
        value_official.append(row['value']['employment_rate'])
    
    d = {'sua': sua, 'value_official': value_official}
    df = pd.DataFrame(data=d)
    
    return df

# get top 3 and bottom 3 twitter topic engagement(except zero)
def generate_color(df):

    sort_by_twi = df['value_media'].sort_values(ascending=False)
    sort_by_twi_pos = sort_by_twi[sort_by_twi != 0]
    top_3 = list(sort_by_twi_pos.head(3).index)
    bottom_3 = list(sort_by_twi_pos.tail(3).index)

    df_get_rank = df.reset_index()
    top_3_final = []
    bottom_3_final = []
    for i in top_3:
        top_3_final.append(df_get_rank[df_get_rank['index'] == i].index.item())
    for i in bottom_3:
        bottom_3_final.append(df_get_rank[df_get_rank['index'] == i].index.item())
    
    color = ['dimgrey'] * (df.shape[0])
    for i in range(df.shape[0]):
        if i in top_3_final:
            color[i] = 'tomato'
        elif i in bottom_3_final:
            color[i] = 'dodgerblue'

    return color

# Function to display value labels on top of bars
def autolabel(ax, bars,num):
    for bar in bars:
        height = bar.get_height()
        if num == 1:
            ax.annotate(f'{round(height,4)}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', color='black', rotation=90)
        else:
            ax.annotate(f'{round(height,4)}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', color='black', rotation=90)


# main function to generate histogram
@app.route('/api_histogram/<state>/<twi>/<sudo>')
def create_figure(state, twi, sudo):
    
    # get twitter & sudo data
    twi_df = api_0(state, twi)
    if sudo == 'agism':
        sudo_df = api_sudo_agism(state)
        ax1_ylabel = 'Percentage of ageing population (%)'
        ax2_ylabel = 'Percentage of agsim discussion engagement (%)'

    elif sudo == 'sexism':
        sudo_df = api_sudo_sexism(state)
        ax1_ylabel = 'Gender ratio'
        ax2_ylabel = 'Percentage of sexism discussion engagement (%)'

    elif sudo == 'unemployment':
        sudo_df = api_sudo_unemployment(state)
        ax1_ylabel = 'Percentage of currently employed population (%)'
        ax2_ylabel = 'Percentage of employment discussion engagement (%)'

    df = twi_df.merge(sudo_df, how='inner', on='sua').sort_values('value_official', ascending=False)

    
    fig, ax1 = plt.subplots(figsize=(20, 8))

    # Calculate the width of the bars
    bar_width = 0.4

    # Calculate the position for the bars on the primary y-axis
    primary_bar_positions = np.arange(len(df['value_official']))

    # Plot the column plot on the primary y-axis
    bars1 = ax1.bar(primary_bar_positions, df['value_official'], width=bar_width, color='silver')
    ax1.set_ylabel(ax1_ylabel)
    ax1.set_ylim(0, max(df['value_official'])*1.15)
    ax1.spines['left'].set_visible(True)
    ax1.spines['left'].set_color('grey')
    ax1.yaxis.label.set_color('grey')
    ax1.tick_params(axis='y', colors='grey')

    # Create a secondary y-axis
    ax2 = ax1.twinx()

    # Calculate the position for the bars on the secondary y-axis
    secondary_bar_positions = primary_bar_positions + bar_width

    # twitter data colors
    colors = generate_color(df)

    # Plot additional data on the secondary y-axis
    if state=='australian capital territory' or state=='offshore territories' or state=='northern territory':
        # no color difference for small states
        bars2 = ax2.bar(secondary_bar_positions, df['value_media'], width=bar_width, color='dimgrey')
    else: 
        bars2 = ax2.bar(secondary_bar_positions, df['value_media'], width=bar_width, color=colors)
    ax2.set_ylabel(ax2_ylabel)
    ax2.set_ylim(0, max(df['value_media'])*1.15)

    # Set the x-tick positions and labels for both y-axes
    ax1.set_xticks(primary_bar_positions + bar_width/2)
    ax1.set_xticklabels(df['sua'], rotation=30, ha='right')

    # Customize the appearance of the secondary y-axis
    ax2.spines['right'].set_visible(True)
    ax2.spines['right'].set_color('black')
    ax2.yaxis.label.set_color('black')
    ax2.tick_params(axis='y', colors='black')

    # set figure title
    if twi=='agism' and sudo=='agism':
        ax1_title = 'Comparison of agesim topic engagement and ageing population percentage'
    elif twi=='sexism' and sudo=='sexism':
        ax1_title = 'Camparison of sexism topic engagement and gender ratio'
    elif twi=='unemployment' and sudo=='unemployment':
        ax1_title = 'Comparison of employment topic engagement and employment rate'
    elif twi=='unemployment' and sudo=='agism':
        ax1_title = 'Comparison of employment topic engagement and ageing population percentage'
    elif twi=='unemployment' and sudo=='sexism':
        ax1_title = 'Comparison of employment topic engagement and gender ratio'
    title_font = {'fontsize': 16, 'fontweight': 'bold', 'fontfamily': 'Arial'}
    ax1.set_title(ax1_title, fontdict=title_font)
    ax1.set_xlabel('SUA name')

    # label bars
    autolabel(ax1, bars1,1)
    autolabel(ax2, bars2,2)

    # Save the figure as PNG to a BytesIO buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the PNG image as base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Return the base64-encoded image
    return image_base64
    # plt.savefig('plot.png', bbox_inches='tight', dpi=300)
    # plt.show()


#pt1  
#get the sum of state with geo for map 
@app.route('/api_twi_state_total/<topic>/<state>')
def api_twi_state_total(topic,state):
    db = server['twitter1']
    view = db.view(f'{topic}/new-view', startkey=[state], endkey=[state, {}],group_level = 2)
    results = []
    total_sum = 0
    mentioned_sum = 0

    for row in view:
        result = {
            "city": row['key'][1],
            'total': row['value']['total'],
            'mentioned': row['value']['mentioned'],
            'percentage': row['value']['percentage']
        }
        total_sum += row['value']['total']
        mentioned_sum += row['value']['mentioned']
        results.append(result)
        
    summary = {
        "total": total_sum,
        "count": mentioned_sum,
        "percentage": mentioned_sum / total_sum
    }
    db_geo = server['geocenter']
    view = db_geo.view('geocenter/new-view')
    geo = {}

    for row in view:
        if row['key'] == state:
            geo[state] = {'lat': row['value']['lat'], 'lng': row['value']['lng']}
            break
        
    return {"summary": summary, state: geo[state]}

#summary of twi server in three topics
@app.route('/api_twi_total/<topic>')
def api_twi_total(topic):
    db = server['twitter1']
    view = db.view(f'{topic}/new-view')
    results = []
    total_sum = 0
    mentioned_sum = 0

    for row in view:
        result = {
            'total': row['value']['total'],
            'mentioned': row['value']['mentioned'],
            'percentage': row['value']['percentage']
        }
        total_sum += row['value']['total']
        mentioned_sum += row['value']['mentioned']
        results.append(result)
        
    summary = {
        "total": total_sum,
        "count": mentioned_sum,
        "percentage": mentioned_sum / total_sum
    }
   
        
    return {"summary": summary}



# changed, get the real-time data from mastodon 
@app.route('/api_mastodon/<topic>')
def api_mastodon(topic):
    result = {'total':0,'mentioned':0,'percentage':0}
    for database in server:
        if 'mastodon' in database:
            db = server[database]
            view = db.view(f'{topic}/new-view',group_level = 1)
            
            for row in view:
                result['total'] += row['value']['total']
                result['mentioned'] +=  row['value']['mentioned']
    
    result['percentage'] = result['mentioned']/result['total']
    return result



#pt2
#get geo location of state parm 
@app.route('/api_geo/<state>')
def api_geo(state):
    db_geo = server['geocenter']
    view = db_geo.view('geocenter/new-view')
    geo = {}

    for row in view:
        if row['key'] == state:
            geo[state] = {'lat': row['value']['lat'], 'lng': row['value']['lng']}
            break

    return geo[state]

# get all geo locations
def get_geo():
    db = server['geocenter']
    view = db.view('geocenter/new-view')
    results = {}
    for row in view:
        results[row['key']]= {'lat': row['value']['lat'], 'lng': row['value']['lng']}
    return results

# return value sorted / with the top3 / last3 flag for front end plotting
def ranking(lst, lst_diction, type_):
    if type_ == 'Twitter':
        rank = sorted(lst)
        last3 =2
        top3=len(rank)-3
        for i in range(len(rank)):
            if i <= last3 and rank[i][0] != 0:
                curr_rank = -1
            elif i <= last3 and rank[i][0] == 0:
                last3 +=1
                curr_rank = 0
            elif rank[i][0] >= rank[top3][0]:
                curr_rank = 1
            else:
                curr_rank = 0
            for output_dic in lst_diction:
                if rank[i][1] == output_dic['city']:
                    output_dic['rank'] = curr_rank
                    break
        return lst_diction
    else:
        ranked_result = []
        rank = sorted(lst,reverse=True)
        for i in range(len(rank)):
            for output_dic in lst_diction:
                if rank[i][1] == output_dic['city']:
                    output_dic['rank'] = 0
                    ranked_result.append(output_dic)
                    break
        return ranked_result

# new added, get all citys of the state with geo for twitter
@app.route('/api_twi_state_city/<topic>/<state>')
def api_page2_twi(state,topic):
    all_geo = get_geo()
    
    return_value = {'state':{}}
    return_value['state']['lat'] = all_geo[state]['lat']
    return_value['state']['lng'] = all_geo[state]['lng']

    rank = []

    db = server['twitter1']

    view = db.view(f'{topic}/new-view', startkey=[state], endkey=[state, {}],group_level = 2)
    results = []
    for row in view:
        result = {"city": row['key'][1],'total': row['value']['total'], 'count': row['value']['mentioned'], 'percentage': row['value']['percentage'],
        'lat': all_geo[row['key'][1]]['lat'], 'lng': all_geo[row['key'][1]]['lng']}
        results.append(result)
        rank.append([row['value']['percentage'],row['key'][1]])

    results = ranking(rank,results,'Twitter')
    return_value['results'] = results
    return return_value


## new added for page 2 sudo plot
@app.route('/api_sudo_state_city/<topic>/<state>')
def api_page2_sudo(state,topic):
    all_geo = get_geo()

    return_value = {'state':{}}
    return_value['state']['lat'] = all_geo[state]['lat']
    return_value['state']['lng'] = all_geo[state]['lng']

    db = server['sudo']
    
    view = db.view(f'{topic}/new-view', startkey=[state], endkey=[state, {}])
    results = []
    rank = []
    if topic == 'agism':
        for row in view:
            result = {"city": row['key'][1],'population': row['value']['ageing_population'], 'percentage': row['value']['ageing_population_percentage'],
            'lat': all_geo[row['key'][1]]['lat'], 'lng': all_geo[row['key'][1]]['lng']}
            results.append(result)
            rank.append([row['value']['ageing_population_percentage'],row['key'][1]])
    elif topic == 'unemployment':
        for row in view:
            result = {"city": row['key'][1],'population': row['value']["people_employed"], 'percentage': row['value']["employment_rate"],
            'lat': all_geo[row['key'][1]]['lat'], 'lng': all_geo[row['key'][1]]['lng']}
            results.append(result)
            rank.append([row['value']["employment_rate"],row['key'][1]])
    else:
        for row in view:
            result = {"city": row['key'][1],'males': row['value']["males"],'females': row['value']["females"],'percentage': row['value']["gender_ratio"],
            'lat': all_geo[row['key'][1]]['lat'], 'lng': all_geo[row['key'][1]]['lng']}
            results.append(result)
            rank.append([row['value']["gender_ratio"],row['key'][1]])

    results = ranking(rank,results,'SUDO')
    return_value['results'] = results
    return return_value




#get all citys of agism by state with geo for sudo
@app.route('/api_sudo_agism_state_city/<state>')
def api_sudo_agism_state_city(state):
    db = server['sudo']
    view = db.view('agism/new-view', startkey=[state], endkey=[state, {}])
    data = []
    for row in view:
        result = {"city": row['key'][1], 'count': row['value']['ageing_population'], 'percentage': row['value']['ageing_population_percentage']}
        data.append(result)

    db_geo = server['geocenter']
    view = db_geo.view('geocenter/new-view')
    geo = {}

    for row in view:
        if row['key'] == state:
            geo[state] = {'lat': row['value']['lat'], 'lng': row['value']['lng']}
            break

    return {state :geo[state], "results": data} 


#get all citys of sexism by state with geo for sudo

@app.route('/api_sudo_sexism_state_city/<state>')
def api_sudo_sexism_state_city(state):
    db = server['sudo']
    view = db.view('sexism/new-view', startkey=[state], endkey=[state, {}])
    data = []
    for row in view:
        result = {"city": row['key'][1], 'male': row['value']['males'], 'female': row['value']['females'], 'ratio': row['value']['gender_ratio']}
        data.append(result)

    db_geo = server['geocenter']
    view = db_geo.view('geocenter/new-view')
    geo = {}

    for row in view:
        if row['key'] == state:
            geo[state] = {'lat': row['value']['lat'], 'lng': row['value']['lng']}
            break

    return {state :geo[state], "results": data} 

#get all citys of unemployment_state by state with geo for sudo

@app.route('/api_sudo_unemployment_state_city/<state>')
def api_sudo_unemployment_state_city(state):
    db = server['sudo']
    view = db.view('unemployment/new-view', startkey=[state], endkey=[state, {}])
    data = []
    for row in view:
        result = {"city": row['key'][1], 'employed': row['value']['people_employed'], 'employment_rate': row['value']['employment_rate']}
        data.append(result)

    db_geo = server['geocenter']
    view = db_geo.view('geocenter/new-view')
    geo = {}

    for row in view:
        if row['key'] == state:
            geo[state] = {'lat': row['value']['lat'], 'lng': row['value']['lng']}
            break

    return {state :geo[state], "results": data} 



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')