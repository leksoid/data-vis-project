from dice import Dice
from plotly.graph_objects import Bar, Layout
from plotly import offline


die_1 = Dice(6)
die_2 = Dice(6)
max_result = die_1.sides + die_2.sides

results = [(die_1.roll() + die_2.roll()) for _ in range(1000)]
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize results

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of D6 rolls', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
