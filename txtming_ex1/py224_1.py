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
# carriage-returns, line-feeds, tabscode
list = ['\r', '\n', '\t']# contractions and other word strings to drop from further analysis, ading
# to the usual English stopwords to be dropped from the document collection
more_stop_words = ['cant', 'didnt', 'doesnt', 'dont', 'goes', 'isnt', 'hes',\ 
                   'shes', 'thats', 'theres', 'theyre', 'wont', 'youll', 'youre', 'youve',\
                   're', 'tv', 'g', 'us', 'en']
