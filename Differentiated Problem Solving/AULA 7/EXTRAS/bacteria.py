import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 12, 300)


def f(x):
    return 100 * np.power(2, x/3)


plt.plot(x, f(x), label='P(t) = 100 * 2^(t/3)')
plt.axhline(y=800, color='red', linestyle='--', label='y = 800')
plt.xlabel('Tempo (horas)')
plt.ylabel('População de bactérias')
plt.title('Crescimento exponencial de bactérias')
plt.legend()
plt.grid(True)
plt.show()