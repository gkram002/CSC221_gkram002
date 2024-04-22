import matplotlib.pyplot as plt

from randomwalkv2 import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
ax.scatter(0, 0, color='purple', edgecolors='red', s=500)
ax.scatter(rw.x_values[-1], rw.y_values[-1], color='orange', edgecolors='none',s=500)
plt.show()