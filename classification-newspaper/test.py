
import pprint
import json
import re
from nltk.stem.snowball import SpanishStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import pickle

with open('v2-2017-01-23.json') as json_data:
	d = json.load(json_data)
	stemmer = SpanishStemmer()
	articleTitles = []
	originalArticleTitles = []
	for art in d['articulos']:
		# For each article:
		originalArticleTitles.append(art['titulo'])
		sentence = art['titulo'].split(' ')
		# Get the article's title
		for i, word in enumerate(sentence):
			# For each word in the title of the article stem it and encode it correctly
			sentence[i] = stemmer.stem(word).encode('utf8')
		sentence = (' ').join(sentence)
		sentence = re.sub('[^A-Za-z0-9]+',' ', sentence)
		articleTitles.append(sentence)
		#print sentence	
	#print articleTitles

	print "We have a total of ", len(articleTitles), " titulos de articulos"
	count_vect = CountVectorizer()
	X_train_counts = count_vect.fit_transform(articleTitles)
	print "The resulting matrix is of shape: ", X_train_counts.todense().shape
	
	#print count_vect.vocabulary_

	# Clustering
	print "Training K-Means clustering model"
	kmeans = KMeans(n_clusters=2, random_state=0).fit(X_train_counts)
	#print kmeans.labels_
	#print kmeans.cluster_centers_
	print "The title: '", originalArticleTitles[300], "' => ", kmeans.predict(X_train_counts[300])
	print "The title: '", originalArticleTitles[301], "' => ", kmeans.predict(X_train_counts[301])
	print "The title: '", originalArticleTitles[302], "' => ", kmeans.predict(X_train_counts[302])
	print "The title: '", originalArticleTitles[303], "' => ", kmeans.predict(X_train_counts[303])


	# SOM
	from mvpa2.suite import *
	som = SimpleSOMMapper((20, 30), 5, learning_rate=0.05)

	#print type(X_train_counts).__name__

	# Transform into dense matrix
	X_train_counts = np.array(X_train_counts.todense())
	som.train(X_train_counts)

	#import matplotlib.pyplot as plt
	#plt.imshow(som.K, origin='lower')
	#plt.show()
	mapped = som(X_train_counts)
	print "##########", len(mapped)

	# Save learned parameters to pickle
	f = open('trainedSOM_parameters.pkl','w')
	pickle.dump( mapped, f )
	f.close()
























