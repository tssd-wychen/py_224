# Text Analysis of Movie Taglines (Python)# Note. Results from this program may differ from those published#       in the book due to differences between Python and R algorithm#       and approaches to the analysis# prepare for Python version 3x features and functionsfrom __future__ import division, print_function# impoert packages for text processing and multivariate analysisimport re # reg. exp.import nltk # draw on the python natural language toolkitimport pandas as pd # data frame structure and operationsimport numpy as np # array and numerical processingimport scipyimport matplotlib.pyplot as plt # 2D potting# terms by documents matrixfrom sklearn.feature_extraction.text import CountVectorizer# alternative distance metrics for multidimensional scalingfrom sklearn.metrics import euclidean_distancesfrom sklearn.metrics.pairwise import linear_kernel as cosine_distancesfrom sklearn.metrics.pairwise import manhattan_distances as manhatten_distances #from sklearn import manifold # multidimensional scalingfrom sklearn.cluster import KMeans # cluster analysis by partitioningfrom sklearn.decomposition import PCA # principle component analysis# define list of codes to be dropped from documents# carriage-returns, line-feeds, tabscodelist = ['\r', '\n', '\t']# contractions and other word strings to drop from further analysis, ading# to the usual English stopwords to be dropped from the document collectionmore_stop_words = ['cant', 'didnt', 'doesnt', 'dont', 'goes', 'isnt', 'hes',\                   'shes', 'thats', 'theres', 'theyre', 'wont', 'youll', 'youre', 'youve',\                   're', 'tv', 'g', 'us', 'en']