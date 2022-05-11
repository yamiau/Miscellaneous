''''This is a light study on the effectiveness of a trick to mentally calculate roots of non-perfect squares
The trick:  finding the nearest lower perfect square,
            take its root,  
            take the difference between the target square and the perfect square,
            add to the root value the ratio of the difference and twice the root,
            and that's an approximation of the real square root of the target square
'''''

#Imports
import math
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.io import export_png

#Structures to store results of calculations
squares = []
actuals = []
tricks = []
differences = []

for i in range(1000):
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

differences = [ abs((actuals[i] - tricks[i])) for i in range(len(squares))]



#Plotting the squares and their actual roots
plot_actual = figure(title = "Non-perfect squares and their roots",
             x_axis_label = "Actual roots",
             y_axis_label = "Square")
plot_actual.line(actuals, squares, line_width = 1, line_color = "green")
plot_actual.background_fill_color = None
plot_actual.border_fill_color = None
# export_png(plot_actual, filename = "actual roots.png")

#Plotting the squares and their trick roots
plot_tricks = figure(title = "Non-perfect squares and their trick roots",
             x_axis_label = "Trick roots",
             y_axis_label = "Square")
plot_tricks.line(tricks, squares, line_width = 1, line_color = "purple")
plot_tricks.background_fill_color = None
plot_tricks.border_fill_color = None
# export_png(plot_tricks, filename = "trick roots.png")

#Plotting the comparison between the two previous plots
plot_compare = figure(title = "Comparison between actual and trick roots",
             x_axis_label = "Actual roots",
             y_axis_label = "Square")
plot_compare.line(actuals, squares, legend_label = "Actual roots", line_width = 1, line_color = "green")
plot_compare.line(tricks, squares, legend_label = "Trick roots", line_width = 1, line_color = "purple")
plot_compare.background_fill_color = None
plot_compare.border_fill_color = None
# export_png(plot_compare, filename = "comparison.png")

#Plotting the difference between the values of actual and trick roots
plot_difference = figure(title = "Difference between actual and trick roots",
             x_axis_label = "Difference between roots",
             y_axis_label = "Square")
plot_difference.circle(differences, squares, size = 3, color = "cyan")
plot_difference.background_fill_color = None
plot_difference.border_fill_color = None
# export_png(plot_difference, filename = "difference.png")

#Making a grid to show all previous plots
grid = gridplot([[plot_actual, plot_tricks], [plot_compare, plot_difference]])
show(grid)