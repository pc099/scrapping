import pandas as pd
import os
import tweepy,jsonpickle

output_data ='output_data'

API_KEY = os.getenv('api_key_twitter_dev')
API_KEY_SECRET = os.getenv('api_key_secret_twitter_dev')
ACCESS_TOKEN = os.getenv('access_token_twitter_dev')
ACESS_TOKEN_SECRET = os.getenv('access_token_secret_twitter_dev')


def name_id(url):
    sp =url.split('/')
    spl =sp[5].split('?')
    return sp[3],spl[0]



def tweet_comments(name, tweet_id):
    replies = []
    for tweet in tweepy.Cursor(api.search,q='to:'+name, count=200,include_rts=False).items(100000):
        print('fetching tweets')
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                replies.append(tweet)
    master_list = []
    for i in replies:
        print('adding to list')
        row = {'user': i.user.screen_name, 'text': i.text.replace('\n', ' ')}
        master_list.append(row)
    return master_list



if __name__ == '__main__':

    url = 'https://twitter.com/andrewyng/status/1290029141522173952?s=21'

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    name, tweet_id = name_id(url=url)
    master_list = tweet_comments(name, tweet_id)
    df = pd.DataFrame().from_dict(i for i in master_list)

    df.to_csv(os.path.join(output_data,'comments_v1.csv'), index=None)








