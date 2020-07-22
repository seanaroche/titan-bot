import tweepy as tp
import time
from keys import CONSUM_KEY, CONSUM_SEC, ACC_SEC, ACC_KEY


auth = tp.OAuthHandler(CONSUM_KEY, CONSUM_SEC)
auth.set_access_token(ACC_KEY, ACC_SEC)
api = tp.API(auth)

mentions = api.mentions_timeline()

for m in mentions:
    print(m.text + ' - ' + str(m.id))
    if '#hello' in m.text.lower():
        print('found #hello')
        print('responding...')


file_name = 'last_id.txt'


def retrieve_last_id(file_name):
    m_read = open(file_name, 'r')
    last_id = int(m_read.read().strip())
    m_read.close()
    return last_id


def store_last_id(last_id, file_name):
    m_write = open(file_name, 'w')
    m_write.write(str(last_id))
    m_write.close()
    return


def reply_tweet():
    print('replying...')
    last_id = retrieve_last_id(file_name)
    mentions = api.mentions_timeline(last_id, tweet_mode='extended')

    for m in reversed(mentions):
        print(str(m.id) + ' - ' + m.full_text)
        last_id = m.id
        store_last_id(last_id, file_name)
        if '#hello' in m.full_text.lower():
            print('found #hello')
            print('responding...')
            api.update_status('@' + m.user.screen_name + '#TitanUp', m.id)
            api.create_friendship('@' + m.user.screen_name)


while True:
    reply_tweet()
    time.sleep(10)
