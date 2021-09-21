

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

from plot_timeseries import get_timeseries_combined_plot_with_conf_intervals
from plot_boxplots import coha_boxplots
from plot_geometry import get_geometry_plot, plot_short_vs_long_low_prevalence, plot_media_category_differences


def big_fig():


	fig_width, fig_height = plt.gcf().get_size_inches()

	fig = plt.figure(figsize=(fig_width*2, fig_height*2), constrained_layout=True)
	
	#fig = plt.figure(figsize=(fig_width*2, fig_height), constrained_layout=True)


	# nrows
	gs = fig.add_gridspec(nrows=3, ncols=4)

	# Top Left - Timeseries
	ax1 = plt.subplot(gs[:2,:2])

	get_timeseries_combined_plot_with_conf_intervals(measure="H_1")
	plt.xlabel("Year")
	plt.ylabel("Word Entropy")

	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)

	# Robustness - TTR
	ax2 = plt.subplot(gs[0,2])

	get_timeseries_combined_plot_with_conf_intervals(measure="ttr")
	plt.xlabel("Year")
	plt.ylabel("Type Token Ratio")

	ax2.spines['right'].set_visible(False)
	ax2.spines['top'].set_visible(False)


	# Robustness - Zif
	ax3 = plt.subplot(gs[0,3])

	get_timeseries_combined_plot_with_conf_intervals(measure="zipf_clauset")
	plt.xlabel("Year")
	plt.ylabel("-1 x Zipf")

	ax3.invert_yaxis()
	ax3.spines['right'].set_visible(False)
	ax3.spines['top'].set_visible(False)


	# Boxplots
	ax4 = plt.subplot(gs[1,2:])

	coha_boxplots()
	plt.ylabel("Word Entropy (Since Year 2000)")
	ax4.spines['right'].set_visible(False)
	ax4.spines['top'].set_visible(False)

	plt.xlabel(None)

	# Model General
	ax5 = plt.subplot(gs[2,1])

	get_geometry_plot()
	plt.legend()
	plt.title("Model")

	# Model General
	ax6 = plt.subplot(gs[2,2])
	plot_short_vs_long_low_prevalence()
	plt.title(r"Low Prevalance, $\lambda$")
	plt.ylabel("Utility")
	plt.xlabel("Time")

	# Model General
	ax7 = plt.subplot(gs[2,3])

	plot_media_category_differences()
	plt.title(r"High Prevalance, $\lambda$")
	plt.ylabel("Utility")
	plt.xlabel("Time")



	plt.tight_layout()

	plt.show()




if __name__=="__main__":

	big_fig()

