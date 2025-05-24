# -*- coding: utf-8 -*-
"""
Created on Mon May 19 00:26:03 2025

@author: Asus
"""

import matplotlib.pyplot as plt
import numpy as np


x_conocidos = np.array([2.0, 3.0, 5.0])
y_conocidos = np.array([6.0, 19.0, 99.0])

print("--- Interpolación de Newton (Grado 2) ---")
print(f"Puntos dados: x = {x_conocidos}, y = {y_conocidos}\n")


def calcular_coeficientes_newton(x_vals, y_vals):
    """
    Calcula los coeficientes b0, b1, b2 para el polinomio de Newton de grado 2.
    """
    if len(x_vals) != 3 or len(y_vals) != 3:
        raise ValueError("Se requieren exactamente 3 puntos para un polinomio de grado 2.")

    b0 = y_vals[0]
    b1 = (y_vals[1] - y_vals[0]) / (x_vals[1] - x_vals[0])
    b2 = ((y_vals[2] - y_vals[1]) / (x_vals[2] - x_vals[1]) - b1) / (x_vals[2] - x_vals[0])
    return b0, b1, b2

def evaluar_polinomio_newton(x_eval, x_base, b0, b1, b2):
    """
    Evalúa el polinomio de Newton en un punto o array de puntos.
    """
    return b0 + b1 * (x_eval - x_base[0]) + b2 * (x_eval - x_base[0]) * (x_eval - x_base[1])

# --- 3. Cálculo de Coeficientes y Evaluación ---
try:
    b0, b1, b2 = calcular_coeficientes_newton(x_conocidos, y_conocidos)
    print(f"Coeficientes del polinomio de Newton:")
    print(f"  b0 = {b0:.4f}")
    print(f"  b1 = {b1:.4f}")
    print(f"  b2 = {b2:.4f}\n")

    valor_a_estimar = 4.0
    estimacion_f4 = evaluar_polinomio_newton(valor_a_estimar, x_conocidos, b0, b1, b2)
    print(f"Valor estimado en x = {valor_a_estimar}: f({valor_a_estimar}) = {estimacion_f4:.2f}")

    x_para_grafico = np.linspace(1, 8, 100)
    y_polinomio_grafico = evaluar_polinomio_newton(x_para_grafico, x_conocidos, b0, b1, b2)

    plt.figure(figsize=(10, 6))

    # Puntos originales que definen el polinomio (azules)
    plt.scatter(x_conocidos, y_conocidos, color='blue', s=100, zorder=5, label='Puntos de Interpolación')

    # Otros puntos para contextualizar (rojos)
    x_otros_puntos = np.array([1, 2, 3, 5, 7, 8])
    y_otros_puntos = np.array([3, 6, 19, 99, 291, 444])
    plt.scatter(x_otros_puntos, y_otros_puntos, color='red', s=50, alpha=0.6, label='Otros Puntos (Contexto)')

    # Gráfico del polinomio interpolante (línea discontinua negra)
    plt.plot(x_para_grafico, y_polinomio_grafico, color='black', linestyle='--', label='Polinomio Interpolante')

    # Punto específico estimado (verde)
    plt.scatter([valor_a_estimar], [estimacion_f4], color='green
