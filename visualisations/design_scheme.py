COLOR_1 = "#3C5488FF" # dark blue
COLOR_2 = "#E64B35FF" # red
COLOR_3 = "#00A087FF" # green
COLOR_4 = "#4DBBD5FF" # light-blue
COLOR_5 = "#F22CA3FF" # pink
COLOR_BLACK = "#404040"

COLOR_FIC = COLOR_1
COLOR_NF = COLOR_4
COLOR_NEWS = COLOR_5
COLOR_SOCIAL = "gray"
COLOR_MAG = COLOR_2

import matplotlib.font_manager as fm
FONT_PROP = fm.FontProperties(fname='/home/chasmani/.fonts/HelveticaLTStd-Roman.otf')
# Add like 	plt.xlabel("Year", fontproperties=FONT_PROP)

FONT_SIZE = 12
FONT_PROP.set_size(FONT_SIZE)
print(FONT_PROP)

BOLD_FONT_PROP = fm.FontProperties(fname='/home/chasmani/.fonts/HelveticaLTStd-Bold.otf')
BOLD_FONT_PROP.set_size(FONT_SIZE)

LINEWIDTH = 1
POINT_SIZE=50
