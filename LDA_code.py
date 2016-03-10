# -*- coding: utf-8 -*-
import pandas as pd

from gensim import corpora, models

import re
import string
import numpy as np

def clean_articles(content):
    content = list(content)
    allwords = []
    i = 0
    while i < len(content):
        #words = [x for x in content[i].split()]
        #words = [''.join(c.lower() for c in s if True) for s in words]
        words = re.findall('[a-zA-Z]+-*[a-zA-Z]*' , content[i])
        allwords.append(words)
        i += 1

        # clean articles
    return allwords

def get_optimum_no_of_topics(content):
    return min(len(content)/3.0 , 10)
    # use arun's measure
    #return num_topics
    #return 10
def perform_LDA(csv_file):
    #print 'ada'
    Content_col = 3
    Heading_col = 1
    content = csv_file[csv_file.columns[Content_col]]
    headings = csv_file[csv_file.columns[Heading_col]]
    cleaned_content = clean_articles(content)
    documents = cleaned_content
    #documents = [''.join(x for x in document) for document in cleaned_content]
    #documents = [doc for doc.split() in cleaned_content]
    length = len(documents)
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(doc) for doc in documents]
    num_topics = get_optimum_no_of_topics(cleaned_content)
    lda = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes = 100)
    all_issues = []
    top_words = []
    num_top_words = 5
    topics_matrix = lda.show_topics(formatted=False, num_words=10, num_topics=num_topics)
    topics_matrix = np.array(topics_matrix)
    topic_words = topics_matrix[:,:,1]
    doc_topic_prob_matrix = np.zeros((length,num_topics))
    for i in range(length):
        for j in range(num_topics):
            doc_topic_prob_matrix[i][j] = lda.get_document_topics(corpus[i] , minimum_probability=0.0)[j][1]
    sum_cols = doc_topic_prob_matrix.sum(axis=0)
    topics_hierarchy = np.argsort(list(sum_cols))[::-1]
    major_issue_no = topics_hierarchy[0]
    minor_issue_no = topics_hierarchy[1]
    for topic_num in range(num_topics):
        top = sorted( zip( list(np.arange(1,length+1)) , corpus) , reverse=True ,  key = lambda (my_id,bow):lda.get_document_topics(bow,minimum_probability=0.0)[topic_num][1] )
        best_doc_ids = [top[i][0] - 1 for i in range(length)]
        best_doc_id = best_doc_ids[0]
        issue_of_the_topic = headings[best_doc_ids[:3]]
        top_words_of_the_topic = list(topic_words[topic_num])[:num_top_words]
        all_issues.append(issue_of_the_topic)
        top_words.append(top_words_of_the_topic)
    major_issue = all_issues[major_issue_no]
    minor_issue = all_issues[minor_issue_no]
    return all_issues , major_issue_no , minor_issue_no , top_words
