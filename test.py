from matplotlib import pyplot

input_data = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

pyplot.style.use('seaborn')
fig, ax = pyplot.subplots()  # fig is entire figure, while ax is the single plot
ax.plot(input_data, squares, linewidth=3)

# set chart title and label axes

ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels

ax.tick_params(axis="both", labelsize=14)

pyplot.show()