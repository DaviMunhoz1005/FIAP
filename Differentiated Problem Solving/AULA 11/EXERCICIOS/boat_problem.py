import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # horas (0h = 12:00 AM)
depth = np.array([9.8, 11.4, 11.6, 11.2, 9.6, 8.5, 6.5, 5.7, 5.4, 6.0, 7.0, 8.6, 10.0])

def func_senoidal(t, A, B, C, D):
    return A * np.cos(B * (t - C)) + D

guess = [3, 2*np.pi/12, 2, 8]
params, _ = curve_fit(func_senoidal, time, depth, p0=guess)
A, B, C, D = params

print(f"Função ajustada: depth(t) = {A:.2f} * cos({B:.2f}(t - {C:.2f})) + {D:.2f}")

t_fit = np.linspace(0, 12, 300)
depth_fit = func_senoidal(t_fit, A, B, C, D)

plt.scatter(time, depth, color="red", label="Dados")
plt.plot(t_fit, depth_fit, color="blue", label="Ajuste senoidal")
plt.xlabel("Tempo (h)")
plt.ylabel("Profundidade (ft)")
plt.legend()
plt.grid(True)
plt.show()