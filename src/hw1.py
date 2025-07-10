import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')
plt.xlabel('x-axis')
plt.ylabel('Your Name Here')  # Replace with your actual name
plt.title('Sine Function')
plt.legend()
plt.grid(True)
plt.savefig('figure.png')
plt.show()

