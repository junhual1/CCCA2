# from mastodon import Mastodon
# import os


# mastodon = Mastodon(api_base_url='https://mastodon.au', access_token = 'sR7_FjfeylT2c7wqJKwPep6g3izM_E9sQyqf58x-ezE')
# mastodon.retrieve_mastodon_version()
# print(mastodon.status('110224847455353234')['created_at'])

from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json,datetime,couchdb,re

m = Mastodon(
        api_base_url=f'https://mastodon.au',
        access_token='3pNPEKMUu8fkt6knKW_Mc0NKqdpKLoOKwa0hiWaZhWk'
    )

user = 'yinxy1'
psw = 'Yxy0112*'
# connect to the CouchDB server
server = couchdb.Server('http://yinxy1:Yxy0112*@127.0.0.1:5984/')

# select the database
db = server['mastodon']

a_toot = {}
class Listener(StreamListener):
    def on_update(self, status):
        # account_id = status['account']['id']
        a_toot["toot_id"] = status['id']
        a_toot["content"] = status['content']
        # .apply(lambda x: x.encode("ascii", "ignore").decode("utf-8"))
        a_toot["time"] = status['created_at'].date().strftime("%Y-%m-%d")
        db.save(a_toot)

m.stream_public(Listener())

