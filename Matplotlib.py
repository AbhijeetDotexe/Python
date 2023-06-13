import matplotlib.pyplot as plt
import numpy as np

# Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(1)
plt.subplot(231)
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')

# Bar Plot
x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]

plt.subplot(232)
plt.bar(x, y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')

# Scatter Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.subplot(233)
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Histogram
data = np.random.randn(1000)

plt.subplot(234)
plt.hist(data, bins=30)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')

# Pie Chart
labels = ['A', 'B', 'C', 'D']
sizes = [20, 30, 25, 25]

plt.subplot(235)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

# Show all plots
plt.tight_layout()
plt.show()
