import plotly.express as px

from dice import Die


die_1 = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
#add the two of them
max_result = die_1.sides + die_2.sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling two D8s 1000 Times"
label = {'x': 'Result', 'y': 'Frequency from the Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=label)

fig.update_layout(xaxis_dtick=1)
fig.show()