# -*- coding: utf-8 -*-
"""
Created on Mon May 19 00:23:41 2025

@author: Asus
"""
import matplotlib.pyplot as plt
import numpy as np

x_puntos = np.array([1.0, 2.0, 3.0, 5.0, 7.0])
y_puntos = np.array([3.0, 6.0, 19.0, 99.0, 291.0])

print("--- Interpolación Polinomial de Newton ---")
print(f"Puntos de entrada: x = {x_puntos}, y = {y_puntos}\n")


def calcular_diferencias_divididas(x_vals, y_vals):
    """
    Calcula los coeficientes 'a' (diferencias divididas) para el polinomio de Newton.
    Este método es general y funciona para cualquier número de puntos.
    """
    n = len(x_vals)
    
    f_diff = np.zeros((n, n))
    f_diff[:, 0] = y_vals 

    for j in range(1, n): 
        for i in range(n - j): 
            f_diff[i, j] = (f_diff[i+1, j-1] - f_diff[i, j-1]) / \
                           (x_vals[i+j] - x_vals[i])
            
    
    coeficientes_a = f_diff[0, :]
    return coeficientes_a # Retorna [a0, a1, a2, a3, a4, ...]


def evaluar_polinomio_newton(x_eval, x_base, coeficientes_a):
    """
    Evalúa el polinomio de Newton en un punto o array de puntos.
    P(x) = a0 + a1*(x-x0) + a2*(x-x0)*(x-x1) + ...
    """
    n = len(coeficientes_a)
    resultado = coeficientes_a[0] # a0
    
    termino_prod = 1.0
    for i in range(1, n):
        termino_prod *= (x_eval - x_base[i-1]) 
        resultado += coeficientes_a[i] * termino_prod
    return resultado

try:
    a_coefs = calcular_diferencias_divididas(x_puntos, y_puntos)
    print("Coeficientes calculados (a0, a1, a2, a3, a4...):")
    print(np.round(a_coefs, 6)) # Mostrar coeficientes con más precisión

    valor_x_estimar = 4.0
    y_estimado_en_4 = evaluar_polinomio_newton(valor_x_estimar, x_puntos, a_coefs)
    
    print(f"\nValor estimado en x = {valor_x_estimar}: P({valor_x_estimar}) = {y_estimado_en_4:.2f}")

    x_rango_grafico = np.linspace(min(x_puntos) - 1, max(x_puntos) + 1, 200)
    y_polinomio_interpolante = evaluar_polinomio_newton(x_rango_grafico, x_puntos, a_coefs)

    plt.figure(figsize=(10, 6))

    # Puntos de datos originales (rojos)
    plt.scatter(x_puntos, y_puntos, color='red', s=100, zorder=5, label='Puntos de Datos Originales')

    # Punto estimado en x=4 (azul)
    plt.scatter([valor_x_estimar], [y_estimado_en_4], color='blue', s=150, zorder=6, label=f'Estimación P({valor_x_estimar})')
    plt.text(valor_x_estimar + 0.1, y_estimado_en_4, f'({valor_x_estimar}, {y_estimado_en_4:.2f})',
             verticalalignment='bottom', fontsize=10, color='blue')


    # Polinomio interpolante (línea discontinua negra)
    plt.plot(x_rango_grafico, y_polinomio_interpolante, color='black', linestyle='--', label='Polinomio Interpolante de Newton')

    plt.title('Interpolación Polinomial de Newton', fontsize=16)
    plt.xlabel('Eje X', fontsize=12)
    plt.ylabel('Eje Y', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Ocurrió un error: {e}")