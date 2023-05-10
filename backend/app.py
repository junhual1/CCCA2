
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


db = server['twitter']


app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return render_template('Index.html')



@app.route('/api_0/<state>')
def api_0(state):
    view = db.view('agism/new-view', startkey=[state], endkey=[state, {}],group_level = 2)
    results = []
    for row in view:
        result = {"city": row['key'][1],'total': row['value']['total'], 'mentioned': row['value']['mentioned'], 'percentage': row['value']['percentage']}
        results.append(result)
    return {"results": results} 

@app.route('/api_00/<state>')
def api_00(state):
    view = db.view('agism/new-view', startkey=[state], endkey=[state, {}],group_level = 2)
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
        "total_sum": total_sum,
        "mentioned_sum": mentioned_sum,
        "percentage_avg": mentioned_sum / total_sum
    }
    return {"summary": summary}

@app.route('/api_000/<state>/<city>')
def api_000(state, city):
    view = db.view('agism/new-view', startkey=[state,city], endkey=[state,city,{}],group_level = 3)
    results = []
    for row in view:
        result = {
            "city": row['key'][1],
            'total': row['value']['total'],
            'mentioned': row['value']['mentioned'],
            'percentage': row['value']['percentage']
        }
        results.append(result)
    return {"results": results}


@app.route('/api_1/<param>')
def api_1(param):
    query = {
        "selector": {
            "state": {
                "$eq": param
            }
        }
    }
    
    results = []
    for row in db.find(query):
        results.append(row)
    return {'data': results}

@app.route('/api_2/<param>')
def api_2(param):
    view = db.view('agism/new-view', startkey=[param], endkey=[param, {}])
    doc = list(view)
    doc_value = doc[0]["value"]
    percent= doc_value['mentioned']/doc_value['total']
    return f"{percent:.5f}"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')