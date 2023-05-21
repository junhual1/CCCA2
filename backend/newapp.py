
import json
import couchdb
from flask import Flask, render_template, jsonify
from flask_cors import CORS

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
    db = server['sudo']
    view = db.view('agism/new-view', startkey=[state], endkey=[state, {}],group_level = 2)
    results = []
    total_sum = 0
    mentioned_sum = 0

    for row in view:
        result = {
            "city": row['key'][1],
            'total': row['value']['total_people'],
            'mentioned': row['value']['ageing_population'],
            'percentage': row['value']['ageing_population_percentage']
        }
        total_sum += row['value']['total_people']
        mentioned_sum += row['value']['ageing_population']
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



#get the real-time data from mastodon 
@app.route('/api_mastodon/<topic>')
def api_mastodon(topic):
    result = {'total':0,'mentioned':0,'percentage':0}
    for database in server:
        if 'mastodon' in database:
            db = couch[database]
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

    db = couch['twitter1']

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

    db = couch['sudo']
    
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