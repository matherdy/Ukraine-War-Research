import tweepy
import json
from googletrans import Translator
import pandas as pd
import sys
import datetime
import os
import time

# Const variables, not subjected to change through out the script
KEYWORDS = []

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
BEARER_TOKEN = ""

translator = Translator()


# Parse in keywords and secrets from env folder
with open('env/keywords.txt', 'r') as f:
    contents = f.readlines()
    for line in contents:
        for key in line.strip().split():
            KEYWORDS.append(key)
            
with open('env/twitter_secrets.json','r') as f:
    data = json.load(f)
    
    CONSUMER_KEY = data['CONSUMER_KEY']
    CONSUMER_SECRET = data['CONSUMER_SECRET']
    ACCESS_KEY = data['ACCESS_KEY']
    ACCESS_SECRET = data['ACCESS_SECRET']
    BEARER_TOKEN = data['BEARER_TOKEN']
    
# Try to authenticate the Client
try:
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN, 
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_KEY,
        access_token_secret=ACCESS_SECRET
    )
    print("Client is sucessfully authenticated!\n")
except:
    print("Unable to authenticate client with the provided credentials!\n")
    sys.exit(1)

# start time to scrape
now = datetime.datetime.now()
start_time = now.strftime('%Y-%m-%dT%H:%M:%SZ')

# create destination folder for new data
folder_name = './data/'+now.strftime('%m_%d_%Y')
try:
    os.makedirs(folder_name) 
    print(f"Folder '{folder_name}' created successfully!\n")
except:
    print(f"Unable to create folder '{folder_name}'")
    sys.exit(1)

 
# Replace with your own search query
for key in KEYWORDS:
    print('📢 Collecting data for keyword: %s...\n' % key)
    tweets = client.search_recent_tweets(query=key, 
                                         tweet_fields=['context_annotations', 'created_at'], 
                                         start_time=start_time,
                                         max_results=100) 

    if tweets.data is not None:
        data = {
        'tweet_id': [],
        'created_at': [],
        'keyword_search': [],
        'text': []
        }
        
        for tweet in tweets.data:
            # Check if tweet is in English
            if tweet.text is not None:
                if translator.detect(tweet.text).lang == 'en':
                    data['tweet_id'].append(tweet.id)
                    data['created_at'].append(tweet.created_at)
                    data['keyword_search'].append(key)
                    data['text'].append(tweet.text)
            
        # Export to csv file
        df = pd.DataFrame(data=data)
        df.to_csv(folder_name+'/'+key+'.csv',index=False)
            
        # Status update
        print('✅ Completed!\n\n')
    else:
        # Status update
        print('❌ NoneType object detected! Unable to collect data!\n\n')