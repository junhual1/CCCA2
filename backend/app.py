
import json
import couchdb
from flask import Flask, render_template, jsonify
from flask_cors import CORS

admin = 'admin'
password = 'qazwsxedc'
url = f'http://{admin}:{password}@172.26.129.182:5984/'

couch = couchdb.Server(url)

db = couch['twi']


app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return render_template('Index.html')



@app.route('/api_0/<param>')
def api_0(param):
    view = db.view('agism/new-view', startkey=[param], endkey=[param, {}])
    doc = list(view)
    doc_value = doc[0]["value"]
    result = {"city": param,'total': doc_value['total'], 'mentioned': doc_value['mentioned']}
    return result

@app.route('/api_11/<state>')
def api_11(state):
    view = db.view('agism/new-view', startkey=[state.lower()], endkey=[state.lower() + "\ufff0"])
    results = []
    for doc in view:
        city_data = doc['value']
        result = {
            'city': doc['key'][0],
            'mentioned': city_data['mentioned'],
            'total': city_data['total']
        }
        results.append(result)
    return {'results': results}

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