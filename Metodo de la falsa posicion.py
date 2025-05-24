# -*- coding: utf-8 -*-
"""

@author: Asus
"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función a analizar
def funcion_objetivo(x_val):
    """Calcula el valor de la función f(x) = 2x*cos(2x) - (x+1)^2."""
    return 2 * x_val * np.cos(2 * x_val) - (x_val + 1)**2

# Función para calcular el error relativo
def calcular_error_relativo(valor_actual, valor_nuevo):
    """Calcula el error relativo porcentual entre dos valores."""
    if valor_actual == 0:  # Evitar división por cero
        return 0.0
    return np.abs((valor_actual - valor_nuevo) / valor_actual) * 100

# Implementación del método de Falsa Posición
def metodo_falsa_posicion(a_inicial, b_inicial, num_iteraciones, raiz_verdadera, func):
    """
    Aplica el método de la falsa posición para encontrar la raíz de una función.

    Args:
        a_inicial (float): Límite inferior del intervalo.
        b_inicial (float): Límite superior del intervalo.
        num_iteraciones (int): Número de iteraciones a realizar.
        raiz_verdadera (float): Valor de la raíz real para cálculo de error.
        func (function): La función objetivo a la que se le busca la raíz.

    Returns:
        float: La raíz aproximada encontrada.
    """
    a = a_inicial
    b = b_inicial
    
    print("\n--- Resultados del Método de Falsa Posición ---")
    
    # Primera estimación fuera del bucle para iniciar el proceso
    xi_estimado = b - (func(b) * (a - b)) / (func(a) - func(b))

    for i in range(1, num_iteraciones + 1):
        fa = func(a)
        fb = func(b) # Agregamos fb para mayor claridad, aunque no se usa directamente en el condicional

        # Recalcular xi en cada iteración
        xi_estimado = b - (func(b) * (a - b)) / (func(a) - func(b))
        
        # Evaluar la condición para ajustar el intervalo
        if func(a) * func(xi_estimado) < 0:
            b = xi_estimado
        else:
            a = xi_estimado
        
        error = calcular_error_relativo(raiz_verdadera, xi_estimado)
        print(f'Iteración {i}: a = {a:.6f}, b = {b:.6f}, Raíz aprox. = {xi_estimado:.6f}, Error = {error:.4f}%')
    
    return xi_estimado

# --- Parámetros iniciales y ejecución ---
if __name__ == "__main__":
    limite_a = -3.0
    limite_b = -2.0
    num_max_iteraciones = 5
    raiz_exacta = -2.1913 # Valor de la raíz conocido para referencia

    # Ejecutar el método de falsa posición
    raiz_encontrada = metodo_falsa_posicion(limite_a, limite_b, num_max_iteraciones, raiz_exacta, funcion_objetivo)

    # --- Visualización de resultados ---
    x_vals = np.linspace(-3, 3, 400) # Más puntos para una curva más suave
    y_vals = funcion_objetivo(x_vals)

    plt.figure(figsize=(10, 6)) # Aumentar el tamaño de la figura
    plt.plot(x_vals, y_vals, label='f(x) = 2x*cos(2x) - (x+1)^2', color='blue')
    plt.plot(raiz_encontrada, 0, 'ro', markersize=8, label=f'Raíz encontrada = {raiz_encontrada:.4f}')
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.7) # Eje X
    plt.axvline(raiz_encontrada, color='red', linestyle=':', linewidth=0.7) # Línea vertical en la raíz

    plt.xlabel('Eje X')
    plt.ylabel('Eje Y (f(x))')
    plt.title('Gráfica del Método de Falsa Posición y Raíz Aproximada')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()