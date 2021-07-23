

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
	

def combined_snapshots(measure="H_1", ax=None):


	measure_type = "word_measures"
	headers = metadata_headers + word_measures_headers

	
	input_filename = "../data/results/results_{}_coca.csv".format(measure_type)
	df_coca = pd.read_csv(input_filename, delimiter=";", names=headers)

	input_filename = "../data/results/results_{}_coha.csv".format(measure_type)
	df_coha = pd.read_csv(input_filename, delimiter=";", names=headers)

	input_filename = "../data/results/results_{}_bnc.csv".format(measure_type)
	df_bnc = pd.read_csv(input_filename, delimiter=";", names=headers)

	input_filename = "../data/results/results_{}_twitter.csv".format(measure_type)
	df_twitter = pd.read_csv(input_filename, delimiter=";", names=headers)

	input_filename = "../data/results/results_{}_facebook.csv".format(measure_type)
	df_facebook = pd.read_csv(input_filename, delimiter=";", names=headers)

	# Recent COHA
	df_coha = df_coha[(df_coha['year'] > 1999)]
	# Rmeove an outlier in COHA
	df_coha = df_coha[(df_coha['H_1'] > 6)]
	



	# Combine all into one df
	df = pd.concat([df_coca, df_coha, df_bnc, df_twitter, df_facebook])

	df.replace(to_replace="Twitter Kaggle Sentiment", value="Twitter", inplace=True)
	df.replace(to_replace="random_concat", value="", inplace=True)


	df["source category"] = df["source"] + " " + df["category"]

	source_cats_order = [
		"COHA nf",
		"COHA fic",
		"COHA news",
		"COHA mag", 
		"",
		"COCA acad",
		"COCA fic",
		"COCA news",		
		"COCA mag",
		"",
		"BNC ACPROSE",
		"BNC FICTION",
		"BNC NEWS",		
		"",
		"Twitter ",
		"Facebook ",
	]

	N = 2000

	df = df[(df['length'] == float(N))]	
	

	ax = sns.boxplot(data=df, y=measure, x="source category", orient="v", ax=ax, order=source_cats_order, linewidth=2)

	#sns.pointplot(data=df, x=measure, y="source category", join=False, ci="sd")

	ax.artists[source_cats_order.index("BNC FICTION")-2].set_facecolor(COLOR_FIC)
	ax.artists[source_cats_order.index("COCA fic")-1].set_facecolor(COLOR_FIC)
	ax.artists[source_cats_order.index("COHA fic")].set_facecolor(COLOR_FIC)

	ax.artists[source_cats_order.index("BNC ACPROSE")-2].set_facecolor(COLOR_NF)
	ax.artists[source_cats_order.index("COCA acad")-1].set_facecolor(COLOR_NF)
	ax.artists[source_cats_order.index("COHA nf")].set_facecolor(COLOR_NF)

	ax.artists[source_cats_order.index("BNC NEWS")-2].set_facecolor(COLOR_NEWS)
	ax.artists[source_cats_order.index("COCA news")-1].set_facecolor(COLOR_NEWS)
	ax.artists[source_cats_order.index("COHA news")].set_facecolor(COLOR_NEWS)


	ax.artists[source_cats_order.index("COCA mag")-1].set_facecolor(COLOR_MAG)
	ax.artists[source_cats_order.index("COHA mag")].set_facecolor(COLOR_MAG)


	try:
		ax.artists[source_cats_order.index("Twitter ")-3].set_facecolor(COLOR_SOCIAL)
		ax.artists[source_cats_order.index("Facebook ")-3].set_facecolor(COLOR_SOCIAL)
	except:
		pass

	
	category_ticks = ["Non-Fic", "Fiction", "News", "Mag", "", 
		"Non-Fic", "Fiction", "News", "Mag", "",
		"Non-Fic", "Fiction", "News", "", 
		"Twitter", "Facebook"]
	

	plt.xticks(range(len(category_ticks)), category_ticks, rotation=45, ha='right')

	for label in ax.get_xticklabels():
		label.set_fontproperties(FONT_PROP)

	for label in ax.get_yticklabels():
		label.set_fontproperties(FONT_PROP)


	

def plot_combined_snapshots_one_measure(measure="H_1", measure_name="Word Entropy", invert_axis=False):

	#plt.figure(figsize=(10,4))

	default_x_size = plt.rcParamsDefault["figure.figsize"][0]
	default_y_size = plt.rcParamsDefault["figure.figsize"][1]

	size_ratio = 2

	plt.rcParams["figure.figsize"] = default_x_size*size_ratio, default_y_size*1.2


	FONT_PROP.set_size(20)
	BOLD_FONT_PROP.set_size(20)


	combined_snapshots(measure)

	plt.ylabel(measure_name, fontproperties=FONT_PROP)


	# Original axis way around
	#plt.xlabel(r"COHA                            COCA                           BNC                             ", fontproperties=BOLD_FONT_PROP)

	plt.xlabel(r"                                                 BNC                                        COCA                                   COHA                             ", fontproperties=BOLD_FONT_PROP)

	ax = plt.gca()
	
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)

	if invert_axis:
		ax.invert_yaxis()


	plt.gca().invert_xaxis()

	ax.yaxis.grid(True) # Show the vertical gridlines

	plt.tight_layout()

	plt.savefig("images/boxplot_distributions_{}.png".format(measure), dpi=300)

	plt.show()


def plot_boxplot_figures_for_all_measures():

	plot_combined_snapshots_one_measure(measure="H_1", measure_name="Word Entropy", invert_axis=False)
	plot_combined_snapshots_one_measure(measure="ttr", measure_name="Type Token Ratio", invert_axis=False)
	plot_combined_snapshots_one_measure(measure="zipf_clauset", measure_name="-1 x Zipf Exponent", invert_axis=True)



if __name__=="__main__":
	plot_boxplot_figures_for_all_measures()