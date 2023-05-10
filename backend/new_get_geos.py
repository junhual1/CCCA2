
import json
import couchdb
# from flask import Flask, render_template, jsonify
# from flask_cors import CORS

admin = 'admin'
password = 'qazwsxedc'
url = f'http://{admin}:{password}@172.26.129.182:5984/'

couch = couchdb.Server(url)

# get sate & city twi - agism
def api_0(state):
    db = couch['twi']
    view = db.view('agism/new-view', startkey=[state], endkey=[state, {}],group_level = 2)
    results = []
    for row in view:
        result = {"city": row['key'][1],'total': row['value']['total'], 'mentioned': row['value']['mentioned'], 'percentage': row['value']['percentage']}
        results.append(result)
    return results

# get all geo locations
def api_geo():
    db = couch['geocenter']
    view = db.view('geocenter/new-view')
    results = {}
    for row in view:
        results[row['key']]= {'lat': row['value']['lat'], 'lng': row['value']['lng']}
    return results

# get sate & city SUDO - agism
def api_sudo(state):
    db = couch['sudo']
    view = db.view('agism/new-view', startkey=[state], endkey=[state, {}])
    results = []
    for row in view:
        result = {"city": row['key'][1],'ageing_population': row['value']['ageing_population'], 'ageing_population_percentage': row['value']['ageing_population_percentage']}
        results.append(result)
    return results

# get victoria agism data
sudo_result = api_sudo('victoria')
twi_result = api_0('victoria')
geo = api_geo()

# merge twi/sudo with geolocation
def combine_geo_data(result):
    for location in result:
        city_name = location['city']
        location['lat'] = geo[city_name]['lat']
        location['lng'] = geo[city_name]['lng']
    return result

twi_result = combine_geo_data(twi_result)
sudo_result = combine_geo_data(sudo_result)

# formate the twitter information front end needed
for item in twi_result:
    lat = item['lat']
    lng = item['lng']
    name = item['city']
    tot = item['total']
    count = item['mentioned']
    percentage = item['percentage']
    print("{"+f"name: '{name}', lat: {lat}, lng: {lng}, total: {tot},count: {count}, percentage: {percentage} "+'},')

# formate the SUDO information front end needed
for item in sudo_result:
    lat = item['lat']
    lng = item['lng']
    name = item['city']
    tot = item['ageing_population']
    percentage = item['ageing_population_percentage']
    print("{"+f"name: '{name}', lat: {lat}, lng: {lng}, total: {tot}, percentage: {percentage} "+'},')
    

# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port='5000')