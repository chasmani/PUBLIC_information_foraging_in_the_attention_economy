

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

from plot_boxplots import combined_snapshots
from plot_geometry import get_geometry_plot, plot_media_category_differences

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10})



def big_fig():


	fig_width, fig_height = plt.gcf().get_size_inches()

	fig = plt.figure(figsize=(fig_width*1.5, fig_height*1.5), constrained_layout=True)
	
	#fig = plt.figure(figsize=(fig_width*2, fig_height), constrained_layout=True)


	# nrows
	gs = fig.add_gridspec(nrows=5, ncols=3)

	# Top Left - KDEs for categories
	ax1 = plt.subplot(gs[:,:2])

	combined_snapshots()


	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)
	

	
	# Icons and foragers
	#ax2 = plt.subplot(gs[0,2])

	
	# Model
	ax3 = plt.subplot(gs[1:3,2])
	get_geometry_plot()
	plt.legend()
	
	# Short vs long
	ax4 = plt.subplot(gs[3:,2])

	plot_media_category_differences()

	plt.ylabel("Utility")
	plt.xlabel("Time")

	plt.legend()

	plt.tight_layout()

	plt.savefig("images/media_categories.tiff", format="tiff", dpi=300)
	

	plt.show()




if __name__=="__main__":

	big_fig()

