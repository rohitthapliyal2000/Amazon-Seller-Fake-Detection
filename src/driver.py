import requests
import nltk
from lxml import html
import itertools
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import sys
import time
import fetching_ as fetch_
import fetching__ as fetch__
import random
from nltk.stem import WordNetLemmatizer
import negation as ng
import progress_bar as pb

def create_word_features(words):

	lemmatizer = WordNetLemmatizer()
	return dict([(lemmatizer.lemmatize(word.lower()), True) for word in words if len(word) > 2])

def sentiment_analysis():

	fake_product_reviews = []
	original_product_reviews = []

	fetch_.fetching(fake_product_reviews, original_product_reviews)

	ng.hack(fake_product_reviews)
	ng.hack(original_product_reviews)

	fake_product_reviews = [(create_word_features((word.split())), 'fake') for word in fake_product_reviews]
	original_product_reviews = [(create_word_features((word.split())), 'original') for word in original_product_reviews]

	training_set_for_fakeness = fake_product_reviews + original_product_reviews
	classifier = NaiveBayesClassifier.train(training_set_for_fakeness)

	time.sleep(1)

	neg_rev = []
	pos_rev = []

	fetch__.fetching(neg_rev, pos_rev)

	ng.hack(pos_rev)
	pb.progress(80.0, 100)
	ng.hack(neg_rev)
	pb.progress(100.0, 100, True)
	time.sleep(5)

	print("\n\nPhase 2...\n")

	time.sleep(1)
	pb.progress(0.0, 100)
	neg_rev = [(create_word_features((word.split())), 'neg') for word in neg_rev]
	pb.progress(50.0, 100)
	pos_rev = [(create_word_features((word.split())), 'pos') for word in pos_rev]
	pb.progress(100.0, 100, True)

	# Accuracy testing purpose
	# num1 = int(3/4 * len(neg_rev))
	# num2 = int(3/4 * len(pos_rev))

	# random.shuffle(neg_rev)
	# random.shuffle(pos_rev)

	# print(num1, num2)

	# training_set_for_sentiments = neg_rev[:num1] + pos_rev[:num2]
	# test = neg_rev[num1:] + pos_rev[num2:]
	# print(len(training_set_for_sentiments), ' ', len(test))

	# classifier = NaiveBayesClassifier.train(training_set_for_sentiments)

	# print(nltk.classify.util.accuracy(classifier, test) * 100)

	time.sleep(5)
	print("\n\nPhase 3...\n")
	pb.progress(0.0, 100)
	time.sleep(1)

	training_set_for_sentiments = neg_rev + pos_rev
	classifier_ = NaiveBayesClassifier.train(training_set_for_sentiments)

	pb.progress(25.0, 100)


	# Testing
	test = []

	with open("reviews.txt") as file:
		for line in file:
			test.append(line.lower())

	ng.hack(test)

	pb.progress(50.0, 100)
	time.sleep(1)

	fake_c = 0
	original_c = 0
	pos_c = 0
	neg_c = 0

	for i in range(1, len(test)):

		line = test[i]

		if classifier.classify(create_word_features(line.split())) == 'fake':
			fake_c += 1
		else:
			original_c += 1

		if classifier_.classify(create_word_features(line.split())) == 'neg':
			neg_c += 1
		else:
			pos_c += 1

	time.sleep(1)
	time.sleep(1)
	pb.progress(100.0, 100.0, True)

	fakeness = fake_c / (fake_c + original_c)
	negativeness = neg_c / (neg_c + pos_c)
	answer = (fakeness + negativeness) / 2

	time.sleep(1)

	print("\n\nThere is", answer * 100, "% possibility that the seller is fake.")
	# End of testing


if __name__ == "__main__":
	sentiment_analysis()
