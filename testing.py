import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = x ** 2

fig, ax = plt.subplot()
ax.plot(x, y, label="F(x)")
plt.show()