import numpy as np
import matplotlib.pyplot as plt

y_hat = np.linspace(0.01, 0.99, 1000)


def cross_entropy(y_hat):
    return -np.log(y_hat)


valores = [0.9, 0.7, 0.5, 0.1]

for v in valores:
    print(f"L({v}) - {cross_entropy(v):.2f}")

plt.figure(figsize=(8, 6))
plt.plot(y_hat, cross_entropy(y_hat), label=r"$L(\hat{y}) = -\log(\hat{y})$", color='blue')
plt.title("Função de Perda (Cross-Entropy) para $y = 1$", fontsize=14)
plt.xlabel(r"$\hat{y}$", fontsize=12)
plt.ylabel(r"Perda $L(\hat{y})$", fontsize=12)
plt.grid(True)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()
plt.show()
