
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.image import BboxImage
from matplotlib.transforms import Bbox, TransformedBbox

import scipy.stats

from design_scheme import COLOR_NF, COLOR_FIC, COLOR_NEWS, COLOR_MAG, LINEWIDTH, FONT_PROP, COLOR_3

import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from utilities.timeseries_measures import get_centered_moving_average



def get_entropy_rising_icon_graph(seed=3, y_min=3, im_count=10):

	np.random.seed(seed)

	ax = plt.gca()

	icon_file_blue = "resources/001-newspaper-folded-blue.png"
	icon_file_grey = "resources/001-newspaper-folded-grey.png"

	im_blue = plt.imread(icon_file_blue)
	im_grey = plt.imread(icon_file_grey)	

	x,y = 0,0

	xs = np.random.random(size=im_count) * 9
	ys = np.random.random(size=im_count) * 6 + 2

	for i in range(im_count):
		x = xs[i]
		y = ys[i]

		bb = Bbox.from_bounds(x,y,1,1)  
		bb2 = TransformedBbox(bb,ax.transData)
		bbox_image = BboxImage(bb2,
	                            norm = None,
	                            origin=None,
	                            clip_on=False)

		if y > (y_min+0.5):
			bbox_image.set_data(im_blue)
		else:
			bbox_image.set_data(im_grey)
		ax.add_artist(bbox_image)
	

	plt.axhline(y_min+1, xmax=1, color=COLOR_3, linestyle="dashed", linewidth=LINEWIDTH*2)


	xx = np.linspace(0, 10, 100)
	yy = [y_min+1]*100
	yy_2 = [10]*100

	plt.fill_between(xx, yy, yy_2, color=COLOR_3, alpha=0.1)

	plt.yticks([])
	plt.xticks([])

	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['bottom'].set_visible(False)

	plt.ylabel(r"$r_i$")

	plt.xlim(0,10)
	plt.ylim(0,10)


def get_entropy_icons_low_prevalence():

	get_entropy_rising_icon_graph(seed=3, y_min=2, im_count=10)


def get_entropy_icons_high_prevalence():

	get_entropy_rising_icon_graph(seed=13, y_min=5, im_count=30)	




if __name__=="__main__":
	get_entropy_icons_high_prevalence()
	plt.show()