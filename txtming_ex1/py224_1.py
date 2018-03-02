# Text Analysis of Movie Taglines (Python)# Note. Results from this program may differ from those published
#       in the book due to differences between Python and R algorithm
#       and approaches to the analysis
# prepare for Python version 3x features and functions
from __future__ import division, print_function
# impoert packages for text processing and multivariate analysis
import re # reg. exp.
import nltk # draw on the python natural language toolkit
import pandas as pd # data frame structure and operations
import numpy as np # array and numerical processing
import scipyimport matplotlib.pyplot as plt # 2D potting# terms by documents matrix
from sklearn.feature_extraction.text import CountVectorizer# alternative distance metrics for multidimensional scaling
from sklearn.metrics import euclidean_distances
from sklearn.metrics.pairwise import linear_kernel as cosine_distances
from sklearn.metrics.pairwise import manhattan_distances as manhatten_distances #
from sklearn import manifold # multidimensional scaling
from sklearn.cluster import KMeans # cluster analysis by partitioning
from sklearn.decomposition import PCA # principle component analysis

# define list of codes to be dropped from documents
# carriage-returns, line-feeds, tabs
codelist = ['\r', '\n', '\t']# contractions and other word strings to drop from further analysis, ading
# to the usual English stopwords to be dropped from the document collection
more_stop_words = ['cant', 'didnt', 'doesnt', 'dont', 'goes', 'isnt', 'hes',\ 
                   'shes', 'thats', 'theres', 'theyre', 'wont', 'youll', 'youre', 'youve',\
                   're', 'tv', 'g', 'us', 'en', 've', 'vg', 'didn', 'pg', 'gp', 'our', 'we',\
                   'll', 'film', 'video', 'name', 'years', 'days', 'one', 'two', 'three',\
                   'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
# start with the initial list and add to it for movie text documents
stoplist = nltk.corpus.stopwords.words('English') + more_stop_words

# text parsing function for creating tect documents
# there is more we could do for data preparation
# stemming... looking for contractions... possessives...
# but we will work with what we have in this parsing functions
# if we want to do stemming at a letter time, we can use
#     porter = nltk.PorterStemmer()
# in a construction like this
#     words_stemmed = [porter.stem(word) for word in initial_words]
def text_parse(string):
    # replace non-alphanumeric with space
    temp_string = re.sub('[^a-zA-Z]', ' ', string)
    # replace codes with space
    for i in range(len(codelist)):
        stopstring = ' '+codelist[i]+' '
        temp_string = re.sub(stopstring, ' ', temp_string)
    # replace single-character words with space
    temp_string = re.sub('\s.\s',' ',temp_string)
    # convert uppercase to lowercase
    temp_string = temp_string.lower()
    # replace selected character strings / stop-words with space
    for i in range(len(stoplist)):
        stopstring = ' '+str(stoplist[i])+' '
        temp_string = re.sub(stopstring, ' ', temp_string)
    # replace multiple blank characters with one blank character
    temp_string = re.sub("\s+", ' ', temp_string)
    return(temp_string)

# read in the comma-delimited text file with from initial data
# preparation ... create the movies data frame for analysis
movies = pd.
