
import matplotlib.pyplot as plt
import numpy as np

from design_scheme import LINEWIDTH, COLOR_MAG, COLOR_FIC, COLOR_4, COLOR_BLACK, FONT_PROP


def plot_discrete_info_curve(prevalence=1, handling_time=1, q=1, n=3, color="red", size_ratio=1):

	current_time = 0
	current_u = 0

	r = q/handling_time

	for i in range(n):

		encounter_time = current_time + 1/prevalence
		finish_time = encounter_time + handling_time

		tt_wait = np.linspace(current_time, encounter_time, 100)
		uu_wait = [current_u] * 100

		plt.plot(tt_wait, uu_wait, color=color, linewidth=LINEWIDTH*size_ratio)

		tt_handle = np.linspace(encounter_time, finish_time, 100)
		uu_handle = current_u + (tt_handle - encounter_time)*r

		plt.plot(tt_handle, uu_handle, color=color, linewidth=LINEWIDTH*size_ratio)

		current_time = finish_time
		current_u += q

	encounter_time = current_time + 1/prevalence
	finish_time = encounter_time + handling_time

	tt_wait = np.linspace(current_time, encounter_time, 100)
	uu_wait = [current_u] * 100	

	plt.plot(tt_wait, uu_wait, color=color, linewidth=LINEWIDTH)


def plot_expected_patch_utility(prevalence=1, handling_time=1, q=1, n=3, color="red", size_ratio=1):

	R = q/(1/prevalence + handling_time)

	tt_max = (1/prevalence + handling_time)*n

	tt = np.linspace(0, tt_max, 100)
	uu = R*tt
	plt.plot(tt, uu, color=color, linestyle="dashed", linewidth=LINEWIDTH*size_ratio)



def get_geometry_plot():

	plt.ylabel("Utility", fontproperties=FONT_PROP)

	xtick_marks = ['']*30
	xtick_marks[10] = r"$\frac{1}{\lambda_p}$"
	xtick_marks[20] = r"$\frac{1}{\lambda_p} + \bar{t}_p$"
	#xtick_marks[20] = r"$t_h"


	ytick_marks = ['']*22
	ytick_marks[10] = r"$\bar{u}_p$"

	plt.xticks(np.arange(0,3,0.1), xtick_marks)
	plt.yticks(np.arange(0,2.2,0.1), ytick_marks)
	
	ax = plt.gca()
	ax.tick_params(axis=u'both', which=u'both',length=0)

	plt.ylim(0,2.2)
	plt.xlim(0,4.5)
	plt.xlabel("Time", fontproperties=FONT_PROP)
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)

	prevalence=1
	handling_time=1 
	q=1
	n=2
	color=COLOR_FIC

	plt.axvline(x=2, ymax=1/2.2, color="lightgray", linewidth=LINEWIDTH)
	plt.axhline(y=1, xmax=2/4.5, color="lightgray", linewidth=LINEWIDTH)

	plot_expected_patch_utility(prevalence=prevalence, handling_time=handling_time, q=q, n=n, color=color, size_ratio=2)
	plot_discrete_info_curve(prevalence=prevalence, handling_time=handling_time, q=q, n=n, color=color, size_ratio=2)

	plt.plot(0,0, color=COLOR_FIC, label=r"Cumulative Utility")
	plt.plot(0,0, color=COLOR_FIC, linestyle="dashed", label=r"Utility Rate")
	



	plt.annotate(r"$\bar{r}_p$", (1.6,0.4), fontproperties=FONT_PROP)


if __name__=="__main__":
	get_geometry_plot()
	plt.show()