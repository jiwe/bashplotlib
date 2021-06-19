# scratch.py
from bashplotlib.scatterplot import plot_scatter

x_coords = [-10,20,30]
y_coords = [-10,20,30]
width = 10
char = 'x'
color = 'default'
title = 'My Test Graph'
xtitle = 'My X Axis'
ytitle = 'My Y Axis'

plot_scatter(
    None,
    x_coords,
    y_coords,
    width,
    char,
    color,
    title,
    xtitle,
    ytitle)
