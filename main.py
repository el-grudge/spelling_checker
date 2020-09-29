import pandas as pd
import numpy as np
import collections
from gensim.parsing.preprocessing import remove_stopwords
import inflect
import re, unicodedata
from nltk.stem.snowball import SnowballStemmer
import nltk
#nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

if __name__ == '__main__':

    file = open("moby.txt", "rt")
    data = file.read()
    tokens = word_tokenize(data)
    print(len(tokens))
    print(len(set(tokens)))

    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = []

    for word in tokens:
        lemmatized_tokens.append(wordnet_lemmatizer.lemmatize(word))
        #print("{0:20}{1:20}".format(word, wordnet_lemmatizer.lemmatize(word)))

    print(len(lemmatized_tokens))
    print(len(set(lemmatized_tokens)))

    print(((lemmatized_tokens.count('history') + lemmatized_tokens.count('HISTORY'))/len(lemmatized_tokens))*100)

    occurence_count = Counter(lemmatized_tokens)
    print(occurence_count.most_common(10))

    print(data)
