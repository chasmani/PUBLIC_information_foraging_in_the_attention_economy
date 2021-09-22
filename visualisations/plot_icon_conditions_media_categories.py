


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import BboxImage
from matplotlib.transforms import Bbox, TransformedBbox

from design_scheme import COLOR_NF, COLOR_FIC, COLOR_NEWS, COLOR_MAG, COLOR_SOCIAL, LINEWIDTH, FONT_PROP, BOLD_FONT_PROP, COLOR_3



def plot_patch_choice_low_prev(seed=11, im_count=10):

	np.random.seed(seed)

	ax = plt.gca()

	icon_file_book = "resources/005-open-book-blue.png"
	icon_file_news = "resources/001-newspaper-folded-blue.png"
	icon_file_twitter = "resources/003-twitter.png"

	im_book = plt.imread(icon_file_book)
	im_news = plt.imread(icon_file_news)	
	im_twitter = plt.imread(icon_file_twitter)

	x,y = 0,0

	xs = np.random.random(size=im_count) * 6 + 1
	ys = np.random.random(size=im_count) * 6 + 1

	lamb=0.1

	R_inv_min = 3

	for i in range(im_count):
		x = xs[i]
		y = ys[i]

		r_inv = 1/(lamb*x) + 1/y
		if r_inv < R_inv_min+0.1:
			alpha=0.8
		else:
			alpha=0.4

		bb = Bbox.from_bounds(x,y,1,1)  
		bb2 = TransformedBbox(bb,ax.transData)
		bbox_image = BboxImage(bb2,
	                            norm = None,
	                            origin=None,
	                            clip_on=False, 
	                            alpha=alpha)


		if x > 5:
			bbox_image.set_data(im_book)
		else:
			bbox_image.set_data(im_news)
		ax.add_artist(bbox_image)

	# Twitter
	for i in range(5):
		x = np.random.random() * 2 + 0.5
		y = np.random.random() * 4 + 6

		r_inv = 1/(lamb*x) + 1/y
		if r_inv < R_inv_min+0.1:
			alpha=0.8
		else:
			alpha=0.4

		bb = Bbox.from_bounds(x,y,1,1)  
		bb2 = TransformedBbox(bb,ax.transData)
		bbox_image = BboxImage(bb2,
	                            norm = None,
	                            origin=None,
	                            clip_on=False, 
	                            alpha=alpha)

		bbox_image.set_data(im_twitter)
		ax.add_artist(bbox_image)
	
	
	xx = np.linspace(3.37,10, 100)
	yy = [1/(R_inv_min - 1/(lamb*x)) for x in xx]
	yy_2 = [10]*100
	plt.fill_between(xx, yy, yy_2, color=COLOR_3, alpha=0.1)


	plt.plot(xx,yy, color=COLOR_3, linewidth=LINEWIDTH*4, linestyle="dashed")


	plt.yticks([])
	plt.xticks([])
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)


	plt.ylabel(r"$\bar{r}_p$", fontproperties=FONT_PROP)
	plt.xlabel(r"$\bar{u}_p$", fontproperties=FONT_PROP)


	plt.xlim(0,10)
	plt.ylim(0,10)


def plot_patch_choice_high_prev(seed=3, im_count=20, lamb=2):

	np.random.seed(seed)

	ax = plt.gca()

	icon_file_book = "resources/005-open-book-blue.png"
	icon_file_news = "resources/001-newspaper-folded-blue.png"
	icon_file_twitter = "resources/003-twitter.png"


	im_book = plt.imread(icon_file_book)
	im_news = plt.imread(icon_file_news)
	im_twitter = plt.imread(icon_file_twitter)	

	x,y = 0,0

	xs = np.random.random(size=im_count) * 8
	ys = np.random.random(size=im_count) * 6


	R_inv_min = 0.5


	for i in range(im_count):
		x = xs[i]
		y = ys[i]

		if x > 5:
			y -= 1


		r_inv = 1/(lamb*x) + 1/y
		if r_inv < R_inv_min+0.1:
			alpha=0.8
		else:
			alpha=0.4

		bb = Bbox.from_bounds(x,y,1,1)  
		bb2 = TransformedBbox(bb,ax.transData)
		bbox_image = BboxImage(bb2,
	                            norm = None,
	                            origin=None,
	                            clip_on=False, 
	                            alpha=alpha)

		if x > 5:
			bbox_image.set_data(im_book)
		else:
			bbox_image.set_data(im_news)
		ax.add_artist(bbox_image)

	# Twitter
	for i in range(5):
		x = np.random.random() * 2 + 0.5
		y = np.random.random() * 4 + 6

		r_inv = 1/(lamb*x) + 1/y
		if r_inv < R_inv_min+0.1:
			alpha=0.8
		else:
			alpha=0.4

		bb = Bbox.from_bounds(x,y,1,1)  
		bb2 = TransformedBbox(bb,ax.transData)
		bbox_image = BboxImage(bb2,
	                            norm = None,
	                            origin=None,
	                            clip_on=False, 
	                            alpha=alpha)

		bbox_image.set_data(im_twitter)
		ax.add_artist(bbox_image)
	

	xx = np.linspace(1,10, 100)
	yy = [1/(R_inv_min - 1/(lamb*x)) for x in xx]
	yy_2 = [10]*100
	plt.fill_between(xx, yy, yy_2, color=COLOR_3, alpha=0.1)


	plt.plot(xx,yy, color=COLOR_3, linewidth=LINEWIDTH*4, linestyle="dashed")



	plt.yticks([])
	plt.xticks([])
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)


	plt.ylabel(r"$\bar{r}_p$", fontproperties=FONT_PROP)
	plt.xlabel(r"$\bar{u}_p$", fontproperties=FONT_PROP)


	plt.xlim(0,10)
	plt.ylim(0,10)


def plot_low_to_high_prevalence():

	fig_width, fig_height = plt.gcf().get_size_inches()

	fig = plt.figure(figsize=(fig_width*2, fig_height), constrained_layout=True)
	
	#fig = plt.figure(figsize=(fig_width*2, fig_height), constrained_layout=True)


	# nrows
	gs = fig.add_gridspec(nrows=1, ncols=5)

	# Left - Low Prevalence
	ax1 = plt.subplot(gs[:,:2])

	plot_patch_choice_low_prev()

	plt.xlabel(r"Average Item Size, $\bar{u}_p$")
	plt.ylabel(r"Average Item Utility Rate, $\bar{r}_p$")


	ax2 = plt.subplot(gs[:,3:])

	plot_patch_choice_high_prev()

	plt.xlabel(r"Average Item Size, $\bar{u}_p$")
	plt.ylabel(r"Average Item Utility Rate, $\bar{r}_p$")

	plt.tight_layout()

	plt.savefig("images/icons_media_categories.tiff", format="tiff", dpi=300)

	plt.show()




if __name__=="__main__":
	plot_low_to_high_prevalence()
	