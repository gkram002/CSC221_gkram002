import plotly.express as px

from die157 import Die


die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1200):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
#add all three together
max_result = die_1.sides + die_2.sides + die_3.sides
poss_results = range(3, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling three D6s 1200 Times"
label = {'x': 'Result', 'y': 'Frequency from the Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=label)
fig.update_layout(xaxis_dtick=1)
fig.show()