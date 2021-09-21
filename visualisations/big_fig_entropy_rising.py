

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

from plot_timeseries import get_timeseries_combined_plot_with_conf_intervals
from plot_icon_conditions import get_entropy_icons_low_prevalence, get_entropy_icons_high_prevalence

def big_fig():


	fig_width, fig_height = plt.gcf().get_size_inches()

	fig = plt.figure(figsize=(fig_width*1.5, fig_height*1.5), constrained_layout=True)
	
	#fig = plt.figure(figsize=(fig_width*2, fig_height), constrained_layout=True)


	# nrows
	gs = fig.add_gridspec(nrows=10, ncols=9)

	# Top Left - Timeseries
	ax1 = plt.subplot(gs[:6,:6])

	get_timeseries_combined_plot_with_conf_intervals(measure="H_1")
	plt.xlabel("Year")
	plt.ylabel("Word Entropy")

	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)

	# Robustness - TTR
	ax2 = plt.subplot(gs[:3,6:])

	get_timeseries_combined_plot_with_conf_intervals(measure="ttr")
	plt.xlabel("Year")
	plt.ylabel("Type Token Ratio")

	ax2.spines['right'].set_visible(False)
	ax2.spines['top'].set_visible(False)


	# Robustness - Zif
	ax3 = plt.subplot(gs[3:6,6:])

	get_timeseries_combined_plot_with_conf_intervals(measure="zipf_clauset")
	plt.xlabel("Year")
	plt.ylabel("-1 x Zipf")

	ax3.invert_yaxis()
	ax3.spines['right'].set_visible(False)
	ax3.spines['top'].set_visible(False)


	# Boxplots
	ax4 = plt.subplot(gs[6:,:4])

	get_entropy_icons_low_prevalence()

	ax5 = plt.subplot(gs[6:,5:])

	get_entropy_icons_high_prevalence()


	plt.tight_layout()

	plt.savefig("images/entropy_rising.tiff", format="tiff", dpi=300)

	plt.show()




if __name__=="__main__":

	big_fig()

