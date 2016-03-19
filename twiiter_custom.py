# -*- coding: utf-8 -*-

import os

from tweepy_code import extract_tweets_using_keywords

cached = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves','you','your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'also', 'said', 'would', 'k']


def perform_sentiment_analysis(twitter_data):
    # return a dict for a topic


def get_the_relevant_words((x,y)):
    global cached
    return [[word if word not in cached for word in x_i.split()] for x_i in x]

def collect_twitter_data((_issues,top_words)):
    words_collection = get_the_relevant_words((_issues,top_words)) # a list of lists of words
    twitter_init_class = extract_tweets_using_keywords()
    sentiment_results = []
    for words in words_collection:
        tweepy_string = ' OR '.join(word for word in words)
        tweets_csv = twitter_init_class.extract_tweets(tweepy_string) # tweets_csv contains two columns : 'Date' and 'Tweets'
        sentiment_dict_for_the_state = perform_sentiment_analysis(tweets_csv)
        sentiment_results.append(sentiment_dict_for_the_state)
    return sentiment_results



def get_the_mood(sentiment_results):  # sentiment_results of a state : [dict_for_topic1 , dict_for_topic2 , ...]
    # return the mood of the state
