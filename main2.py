# -*- coding: utf-8 -*-

import os

import pandas as pd
import numpy as np

from collections import Counter

from twitter_custom import collect_twitter_data , get_the_mood

from LDA_code import perform_LDA

def get_data_from_database():
    # read the input file and the unique state tags

if __name__ == '__main__' :
    csv_input , states = get_data_from_database()
    Date_col = 2
    Article_col = 0
    Heading_col = 1
    Content_col = 3
    Location_col = 4
    for state in states:
        state_input = csv_input[csv_input[csv_input.columns[Location_col]] == state]
        _issues , major_issue_no , minor_issue_no , top_words_collection = perform_LDA(state_input)
        sentiment_results_list_for_the_state = collect_twitter_data(zip(_issues , top_words_collection))
        mood_of_the_state = get_the_mood(sentiment_results)
