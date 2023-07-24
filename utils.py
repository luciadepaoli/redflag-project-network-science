import pandas as pd 
import re
import nltk
from nltk.corpus import stopwords 
from nltk.corpus import wordnet as wn 
import string
import itertools
import networkx as nx 
import datetime as dt
import pickle5 as pickle
from itertools import chain
import numpy as np
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from collections import defaultdict
# DISCLAIMER
# change env to python 3.8 (python 3.7 (default) -> Error: Unsupported Pickle Protocol 5)

#nltk.download('words')
#nltk.download('stopwords') #downloading stopwords
#nltk.download('wordnet') #downloading wordnet
#nltk.download('averaged_perceptron_tagger') #downloading tagger
#nltk.download('omw-1.4')

def cleaner(tweet):
    tweet = re.sub("@[A-Za-z0-9]+","", tweet) # remove mentions (not interested in them)
    tweet = re.sub("#[A-Za-z0-9]+", "", tweet) # remove hashtags (we have them in a specific column)
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) # remove http links (not interested in them)
    tweet = " ".join(tweet.split())
    tweet = str.lower(tweet) #to lowercase
    lemma_function = WordNetLemmatizer()
    #basically we use pos_tag function on tokens that we get by applying wordpunct tokenization
    #to tweet (it separates all the words and symbols)
    #then we pass the token along with it's wordnet pos value that we get from the tag_map dictionary 
    #(noun, adjective, verb or adverb) to the lemma function (the WordNetLemmatizer()) 
    tweet = " ".join(lemma_function.lemmatize(token, tag_map[tag[0]]) 
                     for token, tag in nltk.pos_tag(nltk.wordpunct_tokenize(tweet))) #lemmatize
    
    tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) \
    if w.lower() in words and not w.lower() in stop_words) #remove stop words

    tweet = str.lower(tweet) #to lowercase
    return tweet

def cleanu (tweet):
    tweet = tweet.split()
    for i in range(len(tweet)):
        if tweet[i] == "u":
            tweet[i] = "you"
    tweet = " ".join(w for w in tweet)
    return tweet