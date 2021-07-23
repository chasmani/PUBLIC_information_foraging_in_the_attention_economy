
import csv
import random
import re

import pandas as pd

import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import langdetect
import nltk

from utilities.text_measures import measure_text_word_measures
from utilities.general_utilities import append_to_csv


def remove_apostrophes_and_whitespace(text):

	text = re.sub(r"\s{1,}", " ", text)
	text = re.sub(r"\'", "", text)
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

def remove_if_not_english(text):
	try:
		L = len(text)

		if langdetect.detect(text[:int(L/2)]) == "en" and langdetect.detect(text[int(L/2):]) == "en":

			return text
	except:
		pass
	return ""


def clean_facebook_text(text):

	# Remove commas and extra whitespace
	text = remove_apostrophes_and_whitespace(text)

	text = remove_urls(text)
	
	text = remove_hashtags_and_usernames(text)

	# If it is not English jsut set the text to blank
	text = remove_if_not_english(text)

	return text


def measure_randomly_collated_statuses():


	input_filename = "../data/corpora/facebook_minimaxir/collated/facebook_statuses.csv"
	results_filename = "../data/results/results_word_measures_facebook.csv"

	p_accept_post = 0.05
	N = 2000

	sample_count = 20
	random.seed(0)

	collated_text_samples = []


	with open(input_filename, 'r') as read_obj:
		this_collated_sample = ""
		word_counter = 0
		csv_reader = csv.reader(read_obj)
		total_count = 0
		for row in csv_reader:
				# row variable is a list that represents a row in csv
			status_type = row[4]

			if status_type == "status":
				status = row[2]
				clean_status = clean_facebook_text(status)
				if len(clean_status) > 0:
					total_count += 1
				tokens = nltk.tokenize.word_tokenize(clean_status)
				words = [word.lower() for word in tokens if word.isalpha()]
				word_counter += len(words)
				this_collated_sample += (" " + clean_status)
				if word_counter > 2500:
					collated_text_samples.append(this_collated_sample)
					this_collated_sample = ""
					word_counter = 0
		print(total_count)

		
	print(len(collated_text_samples))

	counter = 0
	for text_sample in collated_text_samples:
		counter += 1
		clean_text = clean_facebook_text(text_sample)

		
		metadata = ["Facebook", counter, "random_concat", 2016,
					"","", "word_measures", N
					]
		word_measures = measure_text_word_measures(clean_text, 2000)
		print(word_measures)
		csv_row = metadata + word_measures
		#append_to_csv(csv_row, results_filename)
		

if __name__=="__main__":
	measure_randomly_collated_statuses()