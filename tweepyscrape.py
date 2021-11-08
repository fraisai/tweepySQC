import SEC_TWI_API
import tweepy
import pandas as pd
import json
import csv
import re
from textblob import TextBlob
import string
import preprocessor as p
import os
import time

auth = tweepy.OAuthHandler(SEC_TWI_API.consumer_key, SEC_TWI_API.consumer_secret)
auth.set_access_token(SEC_TWI_API.access_token, SEC_TWI_API.access_token_secret)

api = tweepy.API(auth)

def tweepyscrape(words_to_search, start_date, numtweet, number_runs):
    
    # Define a pandas dataframe to store the date of the tweet
    pd_data_tweet = pd.DataFrame(columns = ['screen_name', 'followers_count', 'retweet_count', 'favorite_count', 'text', 'created_at', 'hashtags', 'url', 'description'])
    
    # screen_name: EXAMPLE: "screen_name": "TwitterAPI"
    # followers_count : The number of followers the account has.
    # retweet_count: Number of times this Tweet has been retweeted. 
    # favorite_count: Indicates approximately how many times this Tweet has been liked by Twitter users.
    # text: actual UTF-8 text of the status update. EXAMPLE: "text":"To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm"
    # created_at: UTC time at which tweet was created. EXAMPLE: "created_at": "Wed Oct 10 20:19:24 +0000 2018"
    # hashtags:
    # verified : Indicates whether the user is verified or not. EXAMPLE: "verified": true
    # url:
    # description: EXAMPLE: "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
    
    #Time it takes to scrape tweets for each run
    prog_start = time.time

    for i in range(0, number_runs):
        start_run = time.time()
        print(start_run)
        
        # .Cursor() lets you collect tweets and it returns an object that you iterate over/loop thru to access the data
        collected_tweets = tweepy.Cursor(api.search_tweets, q=words_to_search, lang='en', since=start_date, tweet_mode='extended').items(numtweet)
        
        # Store ^ tweets into a python list
        list_tweet = [i for i in collected_tweets]
        
        
        # Start scraping tweets individually
        counter_tweet = 0
        
        # Values for the columns of the pandas DataFrame
        # ['screen_name', 'followers_count', 'retweet_count', 'favorite_count', 'text', 'created_at', 'hashtags', 'url', 'description'])
    
        for j in list_tweet:
            screen_name = j.user.screen_name 
            print(screen_name+ '\n')
            followers_count = j.user.followers_count
            retweet_count = j.retweet_count
            favorite_count = j.favorite_count
            created_at = j.user.created_at
            hashtags = j.entities['hashtags']
            url = j.user.url 
            description = j.user.description

            # For the tweet text part
            try:
                text = j.retweeted_status.full_text
            except AttributeError:
                text = j.full_text
                
            print("Text is: ")    
            print(text)
            
            # Add all the variables to the empty list, updated_tweet_list
            updated_tweet_list = [screen_name, followers_count, retweet_count, favorite_count, text, created_at, hashtags, url, description]

            # Append ^ to the pandas DataFrame that was previously created, pd_data_tweet
            # .loc[] link: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
            pd_data_tweet.loc[len(pd_data_tweet)] = updated_tweet_list

            # Increment counter, counter_tweet
            counter_tweet += 1
        end_run = time.time()
            
        print('no. of tweets scraped for run {} is {}'.format(i + 1, counter_tweet))
        
        # original: time.sleep(920) #15 minute sleep time
        #time.sleep(10) #15 minute sleep time
        
    # Once all runs have completed, save them to a single csv file:
    from datetime import datetime
    
    # Obtain timestamp in a readable format
    to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
    
    # Define working path and filename
    path = os.getcwd()
    filename = path + '/data/' + to_csv_timestamp + 'btc.csv'
    
    # Store dataframe in csv with creation date timestamp
    pd_data_tweet.to_csv(filename, index = False)
    
    program_end = time.time()
# tweepyscrape(words_to_search, start_date, numtweet, number_runs)

words_to_search = "#btc"
#Date format: "2021-11-03"
start_date = "2021-11-01"
numtweet = 5
number_runs = 4
tweepyscrape(words_to_search, start_date, numtweet, number_runs)
