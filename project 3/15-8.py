import plotly.express as px

from dice import Die



die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
#multiply them
max_result = die_1.sides * die_2.sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Multiplying Two D8s 1000 Times"
label = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=label)
fig.update_layout(xaxis_dtick=1)
fig.show()