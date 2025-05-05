import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(0, 7, 400)
comparacoes = np.log2(x)

valores = [1000, 100000, 10000000]

for v in valores:
    print(f"Para {v} registros, {np.log2(v):.2f} comparações.")


plt.title("Exemplo Função Logarítmica")
plt.plot(x, comparacoes)
plt.xscale('log')
plt.axhline(color="black", linewidth="1")
plt.axvline(color="black", linewidth="1")
plt.legend()
plt.grid()
plt.show()