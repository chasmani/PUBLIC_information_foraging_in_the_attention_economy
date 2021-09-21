


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from design_scheme import COLOR_NF, COLOR_FIC, COLOR_NEWS, COLOR_MAG, COLOR_SOCIAL, LINEWIDTH, FONT_PROP, BOLD_FONT_PROP


metadata_headers = [
		"source",
		"sample_id", 
		"category", 
		"year", 
		"author", 
		"title", 
		"measure_type",
		"length"]

word_measures_headers = [
	"word_count", 
	"avg_word_length", 
	"ttr",
	"zipf_cdf",
	"zipf_clauset", 
	"H_0",
	"H_1",
	"H_2"]
	

def coha_boxplots(measure="H_1"):


	measure_type = "word_measures"
	headers = metadata_headers + word_measures_headers

	input_filename = "../data/results/results_{}_coha.csv".format(measure_type)
	df_coha = pd.read_csv(input_filename, delimiter=";", names=headers)
	# Recent COHA
	df_coha = df_coha[(df_coha['year'] > 1999)]
	# Rmeove an outlier in COHA
	df_coha = df_coha[(df_coha['H_1'] > 6)]
	

	coha_categories = ["mag", "news", "", "fic", "nf"]
	coha_verbose = ["Mag", "News", "", "Fiction", "Non-Fic"]

	source_cats_order = [
		"Facebook ",
		"Twitter ",
		"",
		"COHA news",
		"COHA mag",
		"COCA news",
		"COCA mag",
		"BNC NEWS",
		"",
		"COHA nf",
		"COHA fic", 
		"COCA acad", 
		"COCA fic",
		"BNC ACPROSE",
		"BNC FICTION"
	]

	N = 2000

	df_coha = df_coha[(df_coha['length'] == float(N))]	
	

	sns.boxplot(data=df_coha, y=measure, x="category", orient="v", order=coha_categories, linewidth=2)


	plt.xticks(range(len(coha_verbose)), coha_verbose, rotation=45, ha='right')
	ax = plt.gca()
	ax.yaxis.grid(True)

if __name__=="__main__":
	coha_boxplots()
	plt.show()