


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from design_scheme import COLOR_NF, COLOR_FIC, COLOR_NEWS, COLOR_MAG, COLOR_SOCIAL, LINEWIDTH


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



def combined_snapshots(measure="H_1", measure_name="Word Entropy"):




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

	all_cats_list = [""]*16

	social_cats = all_cats_list.copy()
	social_cats[1] = "Twitter "
	social_cats[2] = "Facebook "

	short_form_cats = all_cats_list.copy()
	short_form_cats[4] = "COHA news"
	short_form_cats[5] = "COHA mag"
	short_form_cats[6] = "COCA news"
	short_form_cats[7] = "COCA mag"
	short_form_cats[8] = "BNC NEWS"

	long_form_cats = all_cats_list.copy()
	long_form_cats[10] = "COHA nf"
	long_form_cats[11] = "COHA fic"
	long_form_cats[12] = "COCA acad"
	long_form_cats[13] = "COCA fic"
	long_form_cats[14] = "BNC ACPROSE"
	long_form_cats[15] = "BNC FICTION"

	category_ticks = ["", "Twitter", "Facebook", "", "COHA News", "COHA Mag", 
		"COCA News", "COCA Mag", "BNC News", "", "COHA Non-Fic",
		"COHA Fiction", "COCA Non-Fic", "COCA Fiction", "BNC Non-Fic", 
		"BNC Fiction"]


	N = 2000

	df = df[(df['length'] == float(N))]	
	

	df = df.append([-999,-999,-999,-999,'setosa'])
	df['huecol'] = 0.0
	df['huecol'].iloc[-1]= 999

	ax = plt.gca()



	# Socials
	sns.violinplot(data=df, x=measure, y="source category", saturation=0.4, width=1.5, cut=0, inner="quartile", split=True, hue="huecol",  order=social_cats, linewidth=2, palette=[COLOR_SOCIAL])

	# Short form 
	sns.violinplot(data=df, x=measure, y="source category", saturation=0.4, width=1.5, cut=0, inner="quartile", split=True, hue="huecol",  order=short_form_cats, linewidth=2, palette=[COLOR_MAG])

	# Long form 
	sns.violinplot(data=df, x=measure, y="source category", saturation=0.4, width=1.5, cut=0, inner="quartile", split=True, hue="huecol",  order=long_form_cats, linewidth=2, palette=[COLOR_NF])


	plt.ylabel("")
	plt.xlabel(measure_name)

	plt.yticks(range(len(category_ticks)), category_ticks)



	plt.grid(axis="x")

	ax = plt.gca()
	ax.legend().set_visible(False)

	if measure == "zipf_clauset":
		ax.invert_xaxis()


	#plt.savefig("images/word_measure_distributions_{}.png".format(measure), format="png", dpi=300)



if __name__=="__main__":
	fig_width, fig_height = plt.gcf().get_size_inches()

	fig = plt.figure(figsize=(fig_width, fig_height*2), constrained_layout=True)
	
	combined_snapshots(measure="ttr", measure_name="Type Token Ratio")



	plt.show()