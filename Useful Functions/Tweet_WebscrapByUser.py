# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:33:36 2020

@author: Jinxin
"""

import GetOldTweets3 as got
import pandas as pd


# Parameters: list of twitter usernames, max number of most recent tweet
def username_tweets_to_csv(username,count):
    # create query object
    tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                   .setMaxTweets(count)
                   
    # create list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    
    # create list of chosen tweet data
    user_tweets = [[tweet.date,tweet.text] for tweet in tweets]
    
    # create of dataframe from tweet list
    tweets_df = pd.DataFrame(user_tweets,columns = ['Datetime','Text'])
    
    # convert dataframe to CSV
    tweets_df.to_csv('{}-{}k-tweets.csv'.format(username,int(count/1000)),sep=',')
    

# call function

username = 'realDonaldTrump'
count = 20

username_tweets_to_csv(username,count)