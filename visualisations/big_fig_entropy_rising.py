

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

from plot_timeseries import get_timeseries_combined_plot_with_conf_intervals
from plot_prey_choice_diet_distributions import plot_prey_diet_choice_distribution
from plot_rising_entropy_model import entropy_rising_simulation

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10})



def big_fig():


	fig_width, fig_height = plt.gcf().get_size_inches()

	fig = plt.figure(figsize=(fig_width*1.5, fig_height*1.5), constrained_layout=True)
	
	#fig = plt.figure(figsize=(fig_width*2, fig_height), constrained_layout=True)


	# nrows
	gs = fig.add_gridspec(nrows=10, ncols=12)

	# Top Left - Timeseries
	ax1 = plt.subplot(gs[:6,:8])

	get_timeseries_combined_plot_with_conf_intervals(measure="H_1")
	plt.xlabel("Year")
	plt.ylabel("Word Entropy")

	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)

	# Robustness - TTR
	ax2 = plt.subplot(gs[:3,8:])

	get_timeseries_combined_plot_with_conf_intervals(measure="ttr")
	plt.xlabel("Year")
	plt.ylabel("Type Token Ratio")

	ax2.spines['right'].set_visible(False)
	ax2.spines['top'].set_visible(False)


	# Robustness - Zif
	ax3 = plt.subplot(gs[3:6,8:])

	get_timeseries_combined_plot_with_conf_intervals(measure="zipf_clauset")
	plt.xlabel("Year")
	plt.ylabel("-1 x Zipf")

	ax3.invert_yaxis()
	ax3.spines['right'].set_visible(False)
	ax3.spines['top'].set_visible(False)


	# Model
	ax4 = plt.subplot(gs[6:,:-2])


	entropy_rising_simulation()

	ax4.spines['right'].set_visible(False)
	ax4.spines['top'].set_visible(False)


	plt.tight_layout()

	handles, labels = ax4.get_legend_handles_labels()
	ax4.figure.legend(handles[:], ["Consumed", "Ignored"], title="Information", 
		bbox_to_anchor=(1.0, 0.7), 
          bbox_transform=ax4.transAxes,
          frameon=True, loc='center left')
	
	ax4.get_legend().remove()


	plt.savefig("images/entropy_rising_new.tiff", format="tiff", dpi=300)

	plt.show()


def big_fig_with_entropy_only():


	fig_width, fig_height = plt.gcf().get_size_inches()

	fig = plt.figure(figsize=(fig_width*1.3, fig_height*1.5), constrained_layout=True)
	
	#fig = plt.figure(figsize=(fig_width*2, fig_height), constrained_layout=True)


	# nrows
	gs = fig.add_gridspec(nrows=10, ncols=12)

	# Top Left - Timeseries
	ax1 = plt.subplot(gs[:6,:])

	get_timeseries_combined_plot_with_conf_intervals(measure="H_1")
	plt.xlabel("Year")
	plt.ylabel("Word Entropy")

	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)


	# Model
	ax4 = plt.subplot(gs[6:,:-2])


	entropy_rising_simulation()

	ax4.spines['right'].set_visible(False)
	ax4.spines['top'].set_visible(False)


	plt.tight_layout()

	handles, labels = ax4.get_legend_handles_labels()
	ax4.figure.legend(handles[:], ["Consumed", "Ignored"], title="Information", 
		bbox_to_anchor=(1.0, 0.7), 
          bbox_transform=ax4.transAxes,
          frameon=True, loc='center left')
	
	ax4.get_legend().remove()


	plt.savefig("images/entropy_only_rising_new.tiff", format="tiff", dpi=300)

	plt.show()


if __name__=="__main__":

	big_fig_with_entropy_only()

