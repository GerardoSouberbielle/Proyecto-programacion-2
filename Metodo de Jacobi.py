# -*- coding: utf-8 -*-
"""

@author: Asus
"""

import numpy as np

def calcular_error_relativo(valor_verdadero, valor_nuevo):
 
    if valor_verdadero == 0:
        return 0.0
    return np.abs((valor_verdadero - valor_nuevo) / valor_verdadero) * 100

def metodo_jacobi(matriz_A, vector_b, num_iteraciones=10, tolerancia=1e-6):
   
    # Inicializar las soluciones con ceros para la primera iteración
    num_ecuaciones = matriz_A.shape[0]
    x_actual = np.zeros(num_ecuaciones)
    x_anterior = np.zeros(num_ecuaciones)

    print("--- Resultados del Método de Jacobi ---")

  

    for i in range(1, num_iteraciones + 1):
        x_anterior[:] = x_actual[:] 
        
        print(f'\nIteración: {i}')
        
        for j in range(num_ecuaciones):
            sum_val = 0
            for k in range(num_ecuaciones):
                if j != k:
                    sum_val += matriz_A[j, k] * x_anterior[k]
            
            x_actual[j] = (vector_b[j] - sum_val) / matriz_A[j, j]
            
            error = calcular_error_relativo(x_anterior[j], x_actual[j])
            print(f'  x{j+1} = {x_actual[j]:.6f}, Error relativo x{j+1} = {error:.4f}%')
        
       

    return x_actual

if __name__ == "__main__":
    # Definición del sistema de ecuaciones Ax = b
    matriz_coeficientes = np.array([[1, 1, 2],
                                    [0, 1, 3],
                                    [1, 0, -1]], dtype=float) # Asegurar tipo float
    
    vector_constantes = np.array([[-2],
                                  [7],
                                  [-1]], dtype=float).flatten() # Usar flatten para un array 1D

    max_iteraciones = 5 

    # Ejecutar el método de Jacobi
    soluciones_finales = metodo_jacobi(matriz_coeficientes, vector_constantes, max_iteraciones)

    print("\n--- Soluciones Finales Aproximadas ---")
    for idx, val in enumerate(soluciones_finales):
        print(f"x{idx+1} = {val:.6f}")