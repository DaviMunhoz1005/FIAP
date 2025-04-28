import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 8, 30)
a, b = (1, 2)


def f(x):
    return a * b ** x


plt.title("Exercício 2: Tempo de execução de um Algoritmo Exponencial")
plt.plot(x, f(x), label=f"y = {a} * {b} ** x", color="blue")
plt.scatter(8, f(8), label=f"Tempo de execução para 8 entradas = {f(8):.0f} segundos", color="red")
plt.text(8, f(8), f"({8}, {f(8):.0f})", color="red")
plt.axhline(color="black", linewidth="1")
plt.axvline(color="black", linewidth="1")
plt.legend()
plt.grid()
plt.show()
