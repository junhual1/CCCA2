
import json
import couchdb
# from flask import Flask, render_template, jsonify
# from flask_cors import CORS

admin = 'admin'
password = 'qazwsxedc'
url = f'http://{admin}:{password}@172.26.132.54:5984/'

couch = couchdb.Server(url)

# get sate & city twi - agism
def api_page2_twi(state,topic):
    all_geo = get_geo()
    
    return_value = {'state':{}}
    return_value['state']['lat'] = all_geo[state]['lat']
    return_value['state']['lng'] = all_geo[state]['lng']


    db = couch['twitter1']

    view = db.view(f'{topic}/new-view', startkey=[state], endkey=[state, {}],group_level = 2)
    results = []
    for row in view:
        result = {"city": row['key'][1],'total': row['value']['total'], 'count': row['value']['mentioned'], 'percentage': row['value']['percentage'],
        'lat': all_geo[row['key'][1]]['lat'], 'lng': all_geo[row['key'][1]]['lng']}
        results.append(result)

    return_value['results'] = results
    return return_value

# get all geo locations
def get_geo():
    db = couch['geocenter']
    view = db.view('geocenter/new-view')
    results = {}
    for row in view:
        results[row['key']]= {'lat': row['value']['lat'], 'lng': row['value']['lng']}
    return results

# get sate & city SUDO - agism
def api_page2_sudo(state,topic):
    all_geo = get_geo()

    return_value = {'state':{}}
    return_value['state']['lat'] = all_geo[state]['lat']
    return_value['state']['lng'] = all_geo[state]['lng']

    db = couch['sudo']
    
    view = db.view(f'{topic}/new-view', startkey=[state], endkey=[state, {}])
    results = []
    if topic == 'agism':
        for row in view:
            result = {"city": row['key'][1],'population': row['value']['ageing_population'], 'percentage': row['value']['ageing_population_percentage'],
            'lat': all_geo[row['key'][1]]['lat'], 'lng': all_geo[row['key'][1]]['lng']}
            results.append(result)
    elif topic == 'employment':
        for row in view:
            result = {"city": row['key'][1],'population': row['value']["people_employed"], 'percentage': row['value']["employment_rate"],
            'lat': all_geo[row['key'][1]]['lat'], 'lng': all_geo[row['key'][1]]['lng']}
            results.append(result)
    else:
        for row in view:
            result = {"city": row['key'][1],'males': row['value']["males"],'females': row['value']["females"],'percentage': row['value']["gender_ratio"],
            'lat': all_geo[row['key'][1]]['lat'], 'lng': all_geo[row['key'][1]]['lng']}
            results.append(result)

    return_value['results'] = results
    return return_value

print(api_page2_twi('victoria','agism'))
print(api_page2_sudo('victoria','agism'))
# #pt2
# #get geo location of state parm 
# # @app.route('/api_geo/<state>')
# def api_geo(state):
#     db_geo = server['geocenter']
#     view = db_geo.view('geocenter/new-view')
#     geo = {}

#     for row in view:
#         if row['key'] == state:
#             geo[state] = {'lat': row['value']['lat'], 'lng': row['value']['lng']}
#             break

#     return geo[state]

# # get victoria agism data
# sudo_result = api_sudo('victoria')
# twi_result = api_0('victoria')
# geo = api_geo()

# # merge twi/sudo with geolocation
# def combine_geo_data(result):
#     for location in result:
#         city_name = location['city']
#         location['lat'] = geo[city_name]['lat']
#         location['lng'] = geo[city_name]['lng']
#     return result

# twi_result = combine_geo_data(twi_result)
# sudo_result = combine_geo_data(sudo_result)

# # formate the twitter information front end needed
# for item in twi_result:
#     lat = item['lat']
#     lng = item['lng']
#     name = item['city']
#     tot = item['total']
#     count = item['mentioned']
#     percentage = item['percentage']
#     print("{"+f"name: '{name}', lat: {lat}, lng: {lng}, total: {tot},count: {count}, percentage: {percentage} "+'},')

# # formate the SUDO information front end needed
# for item in sudo_result:
#     lat = item['lat']
#     lng = item['lng']
#     name = item['city']
#     tot = item['ageing_population']
#     percentage = item['ageing_population_percentage']
#     print("{"+f"name: '{name}', lat: {lat}, lng: {lng}, total: {tot}, percentage: {percentage} "+'},')
    

# # if __name__ == '__main__':
# #     app.run(debug=True, host='127.0.0.1', port='5000')
