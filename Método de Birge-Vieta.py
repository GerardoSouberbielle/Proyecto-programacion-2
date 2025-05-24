# -*- coding: utf-8 -*-
"""

@author: Asus
"""

import numpy as np
import matplotlib.pyplot as plt

def birge_vieta(coefficients, initial_guess, iterations=10):
    """
    Implementa el método de Birge-Vieta para encontrar una raíz de un polinomio.

    Args:
        coefficients (np.array): Coeficientes del polinomio en orden descendente (ej. [a_n, a_n-1, ..., a_0]).
        initial_guess (float): Estimación inicial de la raíz.
        iterations (int): Número de iteraciones a realizar.

    Returns:
        float: La raíz aproximada encontrada.
    """
    a = np.array(coefficients, dtype=float) # Aseguramos que los coeficientes sean de tipo float
    x_i = float(initial_guess)
    n = len(a) # Grado del polinomio + 1

    # Arrays para almacenar los coeficientes b y c
    b = np.empty(n, dtype=float)
    c = np.empty(n, dtype=float)

    print("--- Resultados del Método de Birge-Vieta ---")

    for i in range(1, iterations + 1):
        # Calcular los coeficientes b y c para la iteración actual
        for j in range(n):
            if j == 0:
                b[j] = a[j]
                c[j] = a[j]
            else:
                b[j] = a[j] + x_i * b[j-1]
                # 'c' se calcula hasta n-2 para evitar IndexError
                # El último elemento de c no se utiliza para la siguiente estimación de x_i
                if j < n - 1:
                    c[j] = b[j] + x_i * c[j-1]
                else: # El último elemento de c no se necesita
                    c[j] = 0.0 # O cualquier otro valor que indique que no se usa

        # Guardar la estimación anterior de x_i para la impresión
        x_i_old = x_i
        
        # Calcular la nueva estimación de la raíz
        # c[n-2] es el valor que corresponde a b'(x_i) en el algoritmo
        # Aseguramos que c[n-2] no sea cero para evitar ZeroDivisionError
        if c[n-2] == 0:
            print(f"Advertencia: Derivada (c[{n-2}]) es cero en la iteración {i}. El método podría converger lentamente o fallar.")
            # Se podría considerar romper el bucle o ajustar x_i de otra manera
            break 
        x_i = x_i_old - (b[n-1] / c[n-2])

        print(f'\nIteración {i}:')
        print(f'  Estimación anterior de xi = {x_i_old:.6f}')
        print(f'  Coeficientes b: {np.round(b, 4)}')
        print(f'  Coeficientes c: {np.round(c, 4)}')
        print(f'  Nueva estimación de xi = {x_i:.6f}')
    
    return x_i

def plot_polynomial_and_root(coefficients, root_found, title="Método de Birge-Vieta"):
    """
    Grafica el polinomio y la raíz encontrada.

    Args:
        coefficients (np.array): Coeficientes del polinomio.
        root_found (float): La raíz aproximada a graficar.
        title (str): Título de la gráfica.
    """
    # Función para evaluar el polinomio
    polynomial_function = lambda x: np.polyval(coefficients, x)

    # Rango para graficar
    x_vals = np.linspace(root_found - 2, root_found + 2, 400) # Ajustar el rango alrededor de la raíz
    if root_found < -2 or root_found > 2: # Si la raíz está muy fuera de -2, 2, ampliar el rango
        x_vals = np.linspace(min(-5, root_found - 2), max(5, root_found + 2), 400)
    
    y_vals = polynomial_function(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='P(x)', color='blue')
    plt.plot(root_found, 0, 'ro', markersize=8, label=f'Raíz encontrada = {root_found:.4f}')
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.7) # Eje X
    plt.axvline(root_found, color='red', linestyle=':', linewidth=0.7) # Línea vertical en la raíz

    plt.xlabel('Eje X')
    plt.ylabel('P(x)')
    plt.title(title)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

# --- Parámetros iniciales y ejecución ---
if __name__ == "__main__":
    poly_coefficients = np.array([1, -5, 5, -1]) # Coeficientes del polinomio x^3 - 5x^2 + 5x - 1
    initial_root_guess = 0.8
    max_iterations = 10

    # Ejecutar el método de Birge-Vieta
    found_root = birge_vieta(poly_coefficients, initial_root_guess, max_iterations)

    # Visualizar los resultados
    plot_polynomial_and_root(poly_coefficients, found_root)