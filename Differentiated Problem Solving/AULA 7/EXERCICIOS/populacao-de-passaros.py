import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 350, 850)

def f(x):
    return 5600 / (0.5 + 27.5 * np.exp(-0.044 * x))

plt.figure(figsize=(8,5))
plt.title("Exercício 3: População de Pássaros")
plt.plot(x, f(x), label=r"$n(t) = \frac{5600}{0.5 + 27.5e^{-0.044t}}$", color="blue")
plt.scatter(0, f(0), color="red", label=f"População inicial = {f(0):.0f} pássaros")
plt.text(0.5, f(0) + 20, f"(0, {f(0):.0f})", color="red")
plt.scatter(340, f(340), color="green", label=f"População se aproxima de {f(340):.0f} pássaros")
plt.axhline(11200, color="green", linestyle="--", label="População Limite (11.200)")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.xlim(-1, 350)
plt.ylim(150, 11500)
plt.xlabel("Tempo (anos)")
plt.ylabel("População de Pássaros")
plt.legend()
plt.grid(True)
plt.show()
