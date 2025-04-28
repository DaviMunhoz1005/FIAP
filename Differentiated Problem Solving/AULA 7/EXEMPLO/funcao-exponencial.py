import numpy
import numpy as np
import matplotlib.pyplot as plt

x = numpy.linspace(1, 8, 48)
a, b = [100, 2]


def f(x):
    return a * b ** x

plt.title("Exemplo Função Exponencial")
plt.plot(x, f(x), label=f"y = {a} * {b} ** x", color="blue")
plt.scatter(6, f(6), label=f"Número de Users após 6 meses = {f(6)}", color="red")
plt.text(6, f(6), f"({6}, {f(6)})", color="red")
plt.axhline(color="black", linewidth="1")
plt.axvline(color="black", linewidth="1")
plt.legend()
plt.grid()
plt.show()