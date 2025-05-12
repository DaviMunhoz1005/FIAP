import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 15, 50)

def f(x):
    return 1000 * np.exp(0.05 * x)


plt.plot(x, f(x), label='A(t) = 1000 * e^(0.05 * x)')
plt.axhline(y=2000, color='red', linestyle='--', label='y = 2000')
plt.xlabel('Tempo (anos)')
plt.ylabel('Investimento')
plt.title('Crescimento exponencial do Investimento')
plt.legend()
plt.grid(True)
plt.show()