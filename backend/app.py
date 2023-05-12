
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
    db = server['twitter']
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
    db = server['twitter']
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
    db = server['mastodon0']
    view = db.view(f'{topic}/new-view')
    data = []
    for row in view:
        result = {'total': row['value']['total'], 'mentioned': row['value']['mentioned'], 'percentage' : row['value']['mentioned']/row['value']['total']}
        data.append(result)
    return {topic: data}




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

#get all citys of the state with geo for twitter
@app.route('/api_twi_state_city/<topic>/<state>')
def api_twi_state_city(topic, state):
    db = server['twitter']
    view = db.view(f'{topic}/new-view', startkey=[state], endkey=[state, {}],group_level = 2)
    data = []
    for row in view:
        result = {"city": row['key'][1],'total': row['value']['total'], 'count': row['value']['mentioned'], 'percentage': row['value']['percentage']}
        data.append(result)

    db_geo = server['geocenter']
    view = db_geo.view('geocenter/new-view')
    geo = {}

    for row in view:
        if row['key'] == state:
            geo[state] = {'lat': row['value']['lat'], 'lng': row['value']['lng']}
            break

    return {state :geo[state], "results": data} 


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