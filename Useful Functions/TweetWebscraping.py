# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 10:07:11 2020

@author: Jinxin
"""

import GetOldTweets3 as got
import pandas as pd

# Parameters: Text query want to search, max number of most recent tweets to pull from
def text_query_to_csv(text_query,count):
    # Create query object
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query)\
                        .setMaxTweets(count)
    
    # Create of the list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    
    # Create list of chosen tweet data
    text_tweets = [[tweet.date,tweet.text] for tweet in tweets]
    
    # Create dataframe from tweets
    tweets_df = pd.DataFrame(text_tweets,columns = ['Datetime','Text'])
    
    # Convert tweets dataframe to csv file
    tweets_df.to_csv('{}-{}k-tweets.csv'.format(text_query,int(count/1000)),sep=',')
    

# Input search query and it will also name the csv file
    
text_query = 'California Wildfire'
count = 50

text_query_to_csv(text_query,count)