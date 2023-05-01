# from mastodon import Mastodon
# import os


# mastodon = Mastodon(api_base_url='https://mastodon.au', access_token = 'sR7_FjfeylT2c7wqJKwPep6g3izM_E9sQyqf58x-ezE')
# mastodon.retrieve_mastodon_version()
# print(mastodon.status('110224847455353234')['created_at'])

from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json,datetime

m = Mastodon(
        api_base_url=f'https://mastodon.au',
        access_token='sR7_FjfeylT2c7wqJKwPep6g3izM_E9sQyqf58x-ezE'
    )

a = {}
class Listener(StreamListener):
    def on_update(self, status):
        account_id = status['account']['id']
        toot_id = status['id']
        date = status['created_at'].date()
        content = status['content']
        a[toot_id] = [account_id,content,date]
        # print(a)
        print(len(a))
        if len(a) == 3000:
            with open('result.json', 'w') as fp:
                json.dump(a, fp, indent=2, sort_keys=True, default=str)
            exit()



m.stream_public(Listener())

