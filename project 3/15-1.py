import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
cubes = [1, 24, 68, 64, 120 ]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, s=30)

ax.set_title("Square Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=15)
ax.set_ylabel('Square of Value', fontsize=14)

#set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
#show that plot
plt.show()

