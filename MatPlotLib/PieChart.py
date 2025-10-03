import matplotlib.pyplot as plt

chart = [7, 2 ,3, 7, 6]

label = ['sleeping', 'playing', 'music', 'coding','Eating']

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']

plt.pie(chart, labels=label, autopct='%1.1f%%', startangle=140, explode=(0.1, 0, 0, 0, 0), shadow=True, colors=colors)

plt.title('Pie Chart Example')
plt.legend(title="Activities", loc="upper right")
plt.show()