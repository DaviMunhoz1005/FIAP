import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(2, 512, 500)
T = np.log2(n)

valores = [8, 64, 256]
for v in valores:
    print(f"T({v}) = {np.log2(v):.2f}")

plt.figure(figsize=(8, 6))
plt.plot(n, T, label=r"$T(n) = \log_2(n)$", color='blue', linewidth=2)
plt.title("Função T(n) = log2(n) para Compressão de Dados", fontsize=16)
plt.xlabel(r"$n$ (Número de Símbolos)", fontsize=14)
plt.ylabel(r"$T$ (Tamanho Médio do Símbolo)", fontsize=14)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.legend(loc='upper left', fontsize=12)
plt.show()
