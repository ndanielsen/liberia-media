#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Extracts features from cleaned content.

and I'm getting tired so not in a class based style

Author:
Nathan Danielsen
nathan.danielsen [at] gmail.com
"""

import string
from collections import namedtuple

import seaborn as sns
import pandas as pd
import nltk
from nltk.util import ngrams
import matplotlib.pyplot as plt

df = pd.read_pickle('data/cleaned_content.pickle')


features = ['datetime', 'category', 'title', 'author', 'clean_content' ]
text_features = ['category', 'title', 'author', 'clean_content' ]

analysis = df[features]

uni = lambda x: unicode(x)

for col in text_features:
    analysis[col] = analysis[col].apply(uni)


sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def first(x):
    x = x.strip()
    x = sent_detector.tokenize(x)
    return ' '.join(x[:4])

analysis['lead'] = analysis.clean_content.apply(first)

def ebola(x):
    """Returns 1 if ebola in tokenized words"""
    x = x.strip()
    x = x.strip(string.punctuation)
    x = x.lower()
    tokens = nltk.word_tokenize(x)
    if 'ebola' in tokens or 'ebv' in tokens:
        return 1
    else:
        return 0   

analysis['ebola_title'] = analysis.title.apply(ebola)
analysis['ebola_lead'] = analysis.lead.apply(ebola)
analysis['ebola_content'] = analysis.clean_content.apply(ebola)
analysis['title_len'] = analysis.title.apply(lambda x: len(x))
analysis['content_len'] = analysis.clean_content.apply(lambda x: len(x))
analysis['lead_len'] = analysis.lead.apply(lambda x: len(x))


#### County Data
counties = pd.read_csv('data/counties.csv')


def tokenize(x):
    x = x.strip()
    x = x.lower()
    x = x.strip(string.punctuation)
    
    tokens = nltk.word_tokenize(x)
    return tokens

def sents(x):
    x = x.strip()
    x = sent_detector.tokenize(x)
    return ' '.join(x)



def location(x):
	"""
	Returns a list of all locations mentioned. 
	"""
    locations = []
    n_locations = list(counties.capital)
    n_locations += list(counties.county)

    x = x.strip()
    x = x.strip(string.punctuation)
    x = x.lower()
    tokens = nltk.word_tokenize(x)
    
    for entity in n_locations:
      
        entity = tuple(entity.lower().split())
        entity_len = len(entity)

        ngram_tokens = ngrams(tokens, entity_len)
        for ngram in ngram_tokens:
            if entity == ngram:
                full_name = ' '.join(entity)
                locations.append(full_name)
    return locations


analysis['location_title'] = analysis.title.apply(location)
analysis['location_content'] = analysis.clean_content.apply(location)
analysis['location_lead'] = analysis.lead.apply(location)











#### Attempt at visualization

dates = pd.date_range(analysis.datetime.min(), analysis.datetime.max(), freq='W')
lead_plot = pd.Series(analysis.title_len, index=dates)
sns.lmplot("title_len", "ebola_lead", analysis)