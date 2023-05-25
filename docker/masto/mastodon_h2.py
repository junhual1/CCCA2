import couchdb
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener


m = Mastodon(
    api_base_url=f'https://mastodon.au',
    access_token='3pNPEKMUu8fkt6knKW_Mc0NKqdpKLoOKwa0hiWaZhWk'
)

user = 'admin'
psw = 'qazwsxedc'
node_ip = '172.26.132.54'
# connect to the CouchDB server
server = couchdb.Server(f'http://{user}:{psw}@{node_ip}:5984')

cnt = {'count': 0}


class Listener(StreamListener):
    def on_update(self, status):
        a_toot = {}
        count = cnt['count']
        if f'mastodon{count//2000000}' in server:
            db = server[f'mastodon{count//2000000}']
        elif count % 2000000 == 0:
            db = server.create(f'mastodon{count//2000000}')
        else:
            db = server[f'mastodon{count//2000000}']
        a_toot["content"] = status['content']
        a_toot["time"] = status['created_at'].date().strftime("%Y-%m-%d")
        a_toot['toot_id'] = str(status['id'])
        db.save(a_toot)
        cnt['count'] = len(db)


m.stream_public(Listener())
