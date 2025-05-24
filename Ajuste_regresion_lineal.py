# -*- coding: utf-8 -*-
"""
Created on Mon May 19 00:23:16 2025

@author: Asus
"""
import matplotlib.pyplot as plt
import numpy as np


x_data = np.array([1, 2, 3, 4, 5, 6])
y_data = np.array([5.04, 8.12, 10.64, 13.18, 16.20, 20.04])

print("--- Regresión Lineal Simple ---")
print(f"Puntos de datos (x): {x_data}")
print(f"Puntos de datos (y): {y_data}\n")


n = len(x_data)

sum_x = np.sum(x_data)
sum_y = np.sum(y_data)
sum_xy = np.sum(x_data * y_data) # Suma de xi * yi
sum_x_squared = np.sum(x_data**2) # Suma de xi^2

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)

a0 = (sum_y - a1 * sum_x) / n

print(f"Ecuación de la Línea de Regresión:")
print(f"f(x) = {a0:.4f} + {a1:.4f}x\n")

print("--- Predicciones ---")
valores_a_predecir = [15, 30, 50]
for xi_pred in valores_a_predecir:
    y_pred = a0 + a1 * xi_pred
    print(f"f({xi_pred}) = {y_pred:.2f}")

# Crear un rango de x para dibujar la línea de regresión de forma suave
x_line = np.linspace(min(x_data) - 1, max(x_data) + 1, 100) # Extender un poco el rango
y_line = a0 + a1 * x_line

plt.figure(figsize=(10, 6))

plt.scatter(x_data, y_data, color='red', s=80, zorder=5, label='Puntos de Datos Originales')

# Línea de regresión calculada (azul, discontinua)
plt.plot(x_line, y_line, color='blue', linestyle='--', linewidth=2, label=f'Línea de Regresión: f(x) = {a0:.2f} + {a1:.2f}x')
