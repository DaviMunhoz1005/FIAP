import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 20, 60)
a, b = (1000, 1.3)


def f(x):
    return a * b ** x


plt.title("Exercício 1: Crescimento de dados em Database")
plt.plot(x, f(x), label=f"y = {a} * {b} ** x", color="blue")
plt.scatter(15, f(15), label=f"Número de Registros após 15 dias = {f(15):.0f}", color="red")
plt.text(15, f(15), f"({15}, {f(15):.0f})", color="red")
plt.axhline(color="black", linewidth="1")
plt.axvline(color="black", linewidth="1")
plt.legend()
plt.grid()
plt.show()
