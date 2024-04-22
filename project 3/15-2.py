import matplotlib.pyplot as plt
x_values = range(1, 5000)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color="purple", s=10)

ax.set_title("Square Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=15)
ax.set_ylabel('Square of Value', fontsize=14)

#set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
#show that plot
plt.show()