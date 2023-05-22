from mastodon import Mastodon, StreamListener
import time,datetime,couchdb
import sys

class Listener(StreamListener):
    def on_update(self, status):
        try:
            global server
            a_toot = {}
            count = cnt['count']
            if f'mastodon{count//1000000}' in server:
                db = server[f'mastodon{count//1000000}']
            elif count%1000000 == 0:
                db = server.create(f'mastodon{count//1000000}')
                map_unemployment = '''function (doc) {
                var keywords = ['got fired','employ','idle','job loss',' layoff','jobless','redundancy',
                'furlough','downsizing','out of work','retrenchment','job hunt',
                'career transition','job market','job search','job seeker','jobkeeper','hiring'];
                if (doc.content) {
                    var found = {};
                    for (var i = 0; i < keywords.length; i++) {
                    if (doc.content.toLowerCase().includes(keywords[i])) {
                        found[keywords[i]] = true;
                    }
                    }
                    if (Object.keys(found).length > 0) {
                    emit('unemployment', {total: 1, mentioned:1});
                    } else{
                    emit('unemployment', {total: 1, mentioned:0});
                    }
                } else {
                    emit('unemployment', {total: 1, mentioned:0});
                }
                }'''

                reduce_ = '''function (keys, values, rereduce) {
                var result = { total: 0, mentioned: 0, percentage: 0};

                for (var i = 0; i < values.length; i++) {
                    result.total += values[i].total;
                    result.mentioned += values[i].mentioned;
                }
                result.percentage = result.mentioned / result.total * 100;

                return result;
                }'''

                map_agism = '''function (doc) {
                var keywords = ['aging population','senior citizens','gerontology','age-related','retire',
                'longevity','ageism','elderly','silver economy','age-friendly','age discrimination','elder abuse','annuation',
                'pension','senile','nursing home', 'rest home','endowment insurance','aging care','old-age','old age'];
                if (doc.content) {
                    var found = {};
                    for (var i = 0; i < keywords.length; i++) {
                    if (doc.content.toLowerCase().includes(keywords[i])) {
                        found[keywords[i]] = true;
                    }
                    }
                    if (Object.keys(found).length > 0) {
                    emit('agism', {total: 1, mentioned:1});
                    } else{
                    emit('agism', {total: 1, mentioned:0});
                    }
                } else {
                    emit('agism', {total: 1, mentioned:0});
                }
                }'''


                map_sexism = '''function (doc) {
                var keywords = ['gender discrimination','sexism','gender bias','sexual harassment','glass ceiling','pay gap',
                "women's rights",'feminis','gender inequality','male privilege','woman security','women in leadership','gender stereotypes',
                'gender roles','gender-based violence','sexual violence','misogyny','gender issue','metoo','timesup','believewomen',
                'toxicMasculinity','genderequality','equalpay','endrapeculture','menomore','notallmen','maleprivilege','girlpower',
                'sexualharassment','consentmatters','consent matter'];
                if (doc.content) {
                    var found = {};
                    for (var i = 0; i < keywords.length; i++) {
                    if (doc.content.toLowerCase().includes(keywords[i])) {
                        found[keywords[i]] = true;
                    }
                    }
                    if (Object.keys(found).length > 0) {
                    emit('sexism', {total: 1, mentioned:1});
                    } else{
                    emit('sexism', {total: 1, mentioned:0});
                    }
                } else {
                    emit('sexism', {total: 1, mentioned:0});
                }
                }'''


                # Create the design document
                doc_unemployment = {
                    '_id': '_design/unemployment',
                    'views': {
                        'new-view': {
                            'map': map_unemployment,
                            'reduce': reduce_
                        }
                    }
                }
                # Create the design document
                doc_agism = {
                    '_id': '_design/agism',
                    'views': {
                        'new-view': {
                            'map': map_agism,
                            'reduce': reduce_
                        }
                    }
                }

                # Create the design document
                doc_sexism = {
                    '_id': '_design/sexism',
                    'views': {
                        'new-view': {
                            'map': map_sexism,
                            'reduce': reduce_
                        }
                    }
                }

                # Save the design document to the database
                db.save(doc_unemployment)
                db.save(doc_agism)
                db.save(doc_sexism)
            else: 
                db = server[f'mastodon{count//1000000}']
            a_toot["content"] = status['content']
            a_toot["time"] = status['created_at'].date().strftime("%Y-%m-%d")
            a_toot['toot_id']=str(status['id'])
            db.save(a_toot)
            cnt['count'] = len(db)

        except couchdb.http.ServerError:
            print('Error connecting to CouchDB node:', node)
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


# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         raise ValueError("Host and ports are needed! Quiting")
    
#     # input 1 2 3 are ip address for 3 couchDB cluster
#     ip1 = sys.argv[3]
#     ip2 = sys.argv[4]

#     # input 4 for mastdon access token
#     token = sys.argv[1]
    
#     # input
#     port = sys.argv[2]


#     # input 1 2 3 are ip address for 3 couchDB cluster
#     ips = sys.argv[5:]


m = Mastodon(
        api_base_url=f'https://mastodon.au/',
        access_token='3pNPEKMUu8fkt6knKW_Mc0NKqdpKLoOKwa0hiWaZhWk'
    )

# node_ip = ips[0]


cnt = {'count':0}


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
print(server)
m.stream_public(Listener())

