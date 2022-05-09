''''This is a light study on the accuracy of a trick to mentally calculate roots of non-perfect squares
The trick:  finding the nearest lower perfect square,
            take its root,  
            take the difference between the target square and the perfect square,
            add to the root value the ratio of the difference and twice the root,
            and that's an approximation of the real square root of the target square
'''''

import math
from bokeh.plotting import figure, show

squares = []
actuals = []
tricks = []

for i in range(501):
    actual = math.sqrt(i)
    if (actual %1 != 0):
        squares.append(i)
        actuals.append(actual)
        perfect = i -1
        while (math.sqrt(perfect) %1 != 0):
            perfect -= 1
        root = math.sqrt(perfect)
        difference = i - perfect
        tricks.append( root + (difference/(2*root)) )

fig = figure(title = "Non-perfect square root trick",
             x_axis_label = "Result",
             y_axis_label = "Squared")

fig.line(squares, actuals, legend_label = "Actual roots", line_width = 2, line_color = "green")
fig.line(squares, tricks, legend_label = "Trick roots", line_width = 2, line_color = "magenta")

show(fig)






