# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:03:12 2025

@author: Asus
"""

import numpy as np


matriz_A = np.array([[1, -0.1, -0.2],
                     [0.1, 7, -0.3],
                     [0.3, -0.2, -10]], dtype=float)

vector_b = np.array([7.85, 19.3, 71.4], dtype=float)

n_dimension = len(vector_b)

print("--- Resolución de Sistemas Lineales con Métodos Iterativos ---")
print("Matriz A:\n", matriz_A)
print("Vector b:", vector_b)
print("-" * 50, "\n")

try:
    solucion_exacta = np.linalg.solve(matriz_A, vector_b)
    print("Solución Exacta (usando np.linalg.solve):\n", np.round(solucion_exacta, 6))
    print("-" * 50, "\n")
except np.linalg.LinAlgError:
    print("Advertencia: La matriz A podría ser singular. La solución exacta no se pudo calcular fácilmente.")
    solucion_exacta = None


def metodo_jacobi(A, b, max_iteraciones=25, tolerancia=1e-6):
    """
    Resuelve el sistema Ax=b utilizando el método iterativo de Jacobi.
    """
    n = len(b)
    x = np.zeros(n, dtype=float) 
    x_prev = np.copy(x) 
    
    print("### Método de Jacobi ###")
    print(f"Iteración 0: {np.round(x, 6)}")

    for k in range(max_iteraciones):
        for i in range(n):
            
            suma = np.dot(A[i, :i], x_prev[:i]) + np.dot(A[i, i+1:], x_prev[i+1:])
            x[i] = (b[i] - suma) / A[i, i]
        
        print(f"Iteración {k+1}: {np.round(x, 6)}")

        if np.linalg.norm(x - x_prev, ord=np.inf) < tolerancia:
            print(f"Convergió en {k+1} iteraciones (tolerancia {tolerancia}).")
            break
        
        x_prev = np.copy(x) # Actualizar x_prev para la siguiente iteración
    else: 
        print(f"Jacobi no convergió en {max_iteraciones} iteraciones.")
    
    return x

# --- Implementación del Método de Gauss-Seidel ---

def metodo_gauss_seidel(A, b, max_iteraciones=25, tolerancia=1e-6):
    """
    Resuelve el sistema Ax=b utilizando el método iterativo de Gauss-Seidel.
    """
    n = len(b)
    x = np.zeros(n, dtype=float) 
    
    print("\n### Método de Gauss-Seidel ###")
    print(f"Iteración 0: {np.round(x, 6)}")

    for k in range(max_iteraciones):
        x_prev_iter = np.copy(x) 
        for i in range(n):
           
            suma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_prev_iter[i+1:]) 
            x[i] = (b[i] - suma) / A[i, i]
        
        print(f"Iteración {k+1}: {np.round(x, 6)}")

        # Criterio de convergencia
        if np.linalg.norm(x - x_prev_iter, ord=np.inf) < tolerancia:
            print(f"Convergió en {k+1} iteraciones (tolerancia {tolerancia}).")
            break
    else: