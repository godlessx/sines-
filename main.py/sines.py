
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.figure(figsize=(10, 6), layout='constrained')

y_total = y1 + y2

plt.title("Sines")
plt.xlabel("X")
plt.ylabel("Y")

plt.plot(x, y1, label="Sin(x)")
plt.plot(x, y2, label="Sin(2x)")
plt.plot(x, y_total, label="Sum")

plt.grid()
plt.legend()
plt.show()