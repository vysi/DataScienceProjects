import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 6*np.pi, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)
y_f = 3 * x + 1

plt.plot(x, y_sin, label='Sin(x)', color='k', linestyle='--', linewidth=3)
plt.plot(x, y_cos, label='Cos(x)', color='blue', linestyle=':')
plt.plot(x, y_f, label='3*x+1', color='#006400', linestyle='-.')
# plt.legend(loc='center right')
# plt.legend(loc=(0.6, 0.7))
plt.legend()
plt.ylabel('Y-Achse', rotation=45)
plt.xlabel('X-Achse')
plt.ylim(-1.5, 5)
plt.margins(0)
plt.title('My first Plot')
plt.savefig('myplot.png')
plt.show()
