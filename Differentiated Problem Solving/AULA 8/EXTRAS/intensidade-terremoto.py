import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(0, 10, 400)

def f(x):
    return np.log10(x) - 4

plt.plot(x, f(x), label='I(E) = log10(E) - 4')
plt.axhline(y=3, color='red', linestyle='--', label='y = 3')
plt.xlabel('Energia liberada (E)')
plt.xscale('log')
plt.ylabel('Intensidade (I)')
plt.title('Intensidade de um terremoto')
plt.legend()
plt.grid(True)
plt.show()
