import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(-14, 0, 400)

def f(x):
    return -np.log10(x)

plt.plot(x, f(x), label='pH = -log10([H⁺])')
plt.axhline(y=6, color='red', linestyle='--', label='pH = 6')
plt.axvline(x=1e-6, color='green', linestyle=':', label='[H⁺] = 10⁻⁶')
plt.xlabel('Concentração de Íons de Hidrogênio [H⁺]')
plt.xscale('log')
plt.ylabel('pH')
plt.title('Acidez de uma Substância')
plt.legend()
plt.grid(True)
plt.show()
