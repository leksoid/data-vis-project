from matplotlib import pyplot
from random_walk import RandomWalk

while True:
    pyplot.style.use('classic')
    rw = RandomWalk(5_000)
    rw.fill_walk()

    fig, ax = pyplot.subplots()
    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=pyplot.cm.Blues, s=1)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # Show start and end of the walk
    start_point_x, start_point_y = (0, 0)
    ax.scatter(start_point_x, start_point_y, c='green', s=100, edgecolors='none')
    end_point_x, end_point_y = (rw.x_values[-1], rw.y_values[-1])
    ax.scatter(end_point_x, end_point_y, c='red', edgecolors='none', s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    pyplot.show()

    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break

