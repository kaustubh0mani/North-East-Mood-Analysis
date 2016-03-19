# -*- coding: utf-8 -*-
import tweepy

import pandas as pd

import os

class extract_tweets_using_keywords():
    def __init__(self):
        access_token = '462591468-CmTmDhFNKHwZ4N5H1DColkYkA6FU5vf5KaBty4Yd'
        access_token_secret = '6KVdAMviYTemTx592gZw1LUtghfTBcwO0SaFwN3eWJa7Z'
        consumer_key = 'XfRaBazeRYz3bVVk1mrAEyKxs'
        consumer_secret = 'jDjfawHH5oy2PStJ47HhwvrpqvMhWvx6WBC05gKrsm1xaYZ85M'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        self.results = api.search
    def extract_tweets(self,x):
        tweets_df = pd.DataFrame()
        tweets_list = []
        date_list = []
        User_Id = []
        for tweet in tweepy.Cursor(self.results, q=x, count=1000, result_type="recent", include_entities=True, lang="en").items():
            date_list.append(tweet.created_at)
            tweets_list.append(tweet.text)
            #print tweet.created_at , tweet.text
            #print len(tweets_list)
        tweets_df['Date'] = pd.Series(date_list)
        tweets_df['Tweets'] = pd.Series(tweets_list)
        return tweets_df
fg = extract_tweets_using_keywords()
tweets = fg.extract_tweets('#naga OR peace accord')
