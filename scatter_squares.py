from matplotlib import pyplot

input_data = range(1, 1001)
squares = [x**2 for x in input_data]


pyplot.style.use('seaborn')

fig, ax = pyplot.subplots()

ax.scatter(input_data, squares, c=squares, cmap=pyplot.cm.Blues, s=1)

pyplot.savefig("squares_plot.png", bbox_inches='tight')
