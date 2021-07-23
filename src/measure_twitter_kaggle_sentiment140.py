
import csv
import random
import re

import pandas as pd

import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from utilities.text_measures import measure_text_word_measures
from utilities.general_utilities import append_to_csv


def remove_apostrophes_and_whitespace(text):

	text = re.sub(r"\s{1,}", " ", text)
	text = re.sub(r"\s\'|\'", "", text)
	return text

def remove_urls(text):
	# Quite greedy - don't care too much about false positives
	# Any word with a fullstop within it, and at least one character either side
	text = re.sub(r"\S+\.\S+", "", text)
	return text


def remove_hashtags_and_usernames(text):
	# Quite greedy - don't care too much about false positives
	# Any word with a fullstop within it, and at least one character either side
	text = re.sub(r"\@\S+", "", text)
	text = re.sub(r"\#\S+", "", text)
	return text


def clean_twitter_text(text):

 	# Remove commas and extra whitespace
 	text = remove_apostrophes_and_whitespace(text)

 	text = remove_urls(text)
 	
 	text = remove_hashtags_and_usernames(text)

 	return text


def measure_randomly_collated_tweets():


	input_filename = "../data/corpora/twitter_kaggle_sentiment140/raw/training.1600000.processed.noemoticon.csv"
	results_filename = "../data/results/results_word_measures_twitter.csv"

	p_accept_tweet = 0.001
	N = 2000

	sample_count = 1000

	for counter in range(sample_count):
		print("Working {} of {}".format(counter, sample_count))

		randomly_selected_tweets = []
		with open(input_filename, 'r', encoding="ISO-8859-1") as read_obj:
		    csv_reader = csv.reader(read_obj)
		    for row in csv_reader:
		        # row variable is a list that represents a row in csv
		        if random.random() < p_accept_tweet:
			        tweet_content = row[5]
			        print("\nNext:")
			        print(tweet_content)
		        	randomly_selected_tweets.append(tweet_content)

		text = " ".join(randomly_selected_tweets)
		clean_text = clean_twitter_text(text)
		
		print(clean_text)

		metadata = [
			"Twitter Kaggle Sentiment", counter, "random_concat", 2009,
			"","", "word_measures", N
			]
		word_measures = measure_text_word_measures(clean_text, 2000)
		csv_row = metadata + word_measures
		#append_to_csv(csv_row, results_filename)


if __name__=="__main__":
	measure_randomly_collated_tweets()