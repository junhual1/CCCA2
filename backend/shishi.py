import json
import couchdb
from flask import Flask, render_template, jsonify


admin = 'admin'
password = 'qazwsxedc'
url = f'http://{admin}:{password}@172.26.129.182:5984/'

couch = couchdb.Server(url)

db = couch['sudo']


view = db.view('agism/new-view', startkey=["new south wales"], endkey=["new south wales", {}])

for row in view:
    result = {"city": row['key'][1],'ageing_population': row['value']['ageing_population'], 'ageing_population_percentage': row['value']['ageing_population_percentage']}
    print(result)




#view = db.view('agism/new-view', startkey=["Adelaide"], endkey=["param", {}])
#doc = list(view)
#doc_value = doc[0]["value"]
#percent= doc_value['mentioned']/doc_value['total']
#print (f"Adelaide: {percent:.2f}%")

#@app.route('/api_0/<param>')
#def api_0(param):
#    view = db.view('agism/new-view', startkey=[param], endkey=[param, {}])
#    for doc in view:
#        percent= doc['value']['mentioned']/doc['value']['total']
#    return f"{percent:.5f}"