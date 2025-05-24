# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 00:00:13 2025

@author: Asus
"""
import numpy as np
from sympy import symbols, integrate, cos, exp, pi
import pandas as pd # Importamos pandas para tablas más claras

def f1(x_val):
    """Función 1: 2 * cos(2x)"""
    return 2 * np.cos(2 * x_val)

def f2(x_val):
    """Función 2: -x^2 - x/2 + 4"""
    return -x_val**2 - x_val/2 + 4

def f3(x_val):
    """Función 3: exp(-x^2) - Función Gaussiana"""
    return np.exp(-x_val**2)

x_simbolico = symbols('x')
integrales_analiticas = [
    integrate(2 * cos(2 * x_simbolico), (x_simbolico, 0, pi/4)),
    integrate(-x_simbolico**2 - x_simbolico/2 + 4, (x_simbolico, 0.5, 1.5)),
    integrate(exp(-x_simbolico**2), (x_simbolico, 0, 1)) # Esta no tiene solución elemental en términos simples
]

print("=== RESULTADOS ANALÍTICOS (CALCULADOS CON SYMPY) ===")
for i, analitica_val in enumerate(integrales_analiticas):
    print(f"Integral {i+1}: {analitica_val.evalf():.8f}") # Aumentamos la precisión mostrada
print("-" * 50, "\n")



def regla_trapecio_simple(func, a, b):
    """Implementa la regla del trapecio simple."""
    return (b - a) / 2 * (func(a) + func(b))

def regla_trapecio_multiple(func, a, b, n_segmentos):
    """Implementa la regla del trapecio compuesta con 'n_segmentos'."""
    h = (b - a) / n_segmentos
    x_puntos = np.linspace(a, b, n_segmentos + 1)
    suma = func(a) + func(b)
    for i in range(1, n_segmentos):
        suma += 2 * func(x_puntos[i])
    return h / 2 * suma

def regla_simpson_1_3(func, a, b):
    """Implementa la regla de Simpson 1/3 (requiere 2 segmentos, 3 puntos)."""
    m = (a + b) / 2 # Punto medio
    return (b - a) / 6 * (func(a) + 4 * func(m) + func(b))

def regla_simpson_3_8(func, a, b):
    """Implementa la regla de Simpson 3/8 (requiere 3 segmentos, 4 puntos)."""
    h = (b - a) / 3
    return 3 * h / 8 * (func(a) + 3 * func(a + h) + 3 * func(a + 2 * h) + func(b))


def regla_simpson_especial_6_8(func, a, b):
    """Implementa una regla de Simpson modificada o compuesta para 6 segmentos."""
    n_seg = 6
    h_step = (b - a) / n_seg
    x_vals = np.linspace(a, b, n_seg + 1)
    
    suma_s = func(x_vals[0]) + func(x_vals[6]) + \
             5 * (func(x_vals[1]) + func(x_vals[5])) + \
             6 * func(x_vals[3]) + \
             func(x_vals[2]) + func(x_vals[4])
    return 3 * h_step / 10 * suma_s

funciones_de_prueba = [f1, f2, f3]
limites_de_integracion = [(0, np.pi/4), (0.5, 1.5), (0, 1)]

# Diccionario de métodos para facilitar la iteración
diccionario_metodos = {
    "Trapecio Simple": regla_trapecio_simple,
    "Trapecio Múltiple (n=2)": lambda f, a, b: regla_trapecio_multiple(f, a, b, 2),
    "Trapecio Múltiple (n=4)": lambda f, a, b: regla_trapecio_multiple(f, a, b, 4),
    "Trapecio Múltiple (n=6)": lambda f, a, b: regla_trapecio_multiple(f, a, b, 6),
    "Simpson 1/3": regla_simpson_1_3,
    "Simpson 3/8": regla_simpson_3_8,
    "Simpson Especial 6/8": regla_simpson_especial_6_8
}

print("=== RESULTADOS NUMÉRICOS Y ERRORES RELATIVOS ===")

for i in range(len(funciones_de_prueba)):
    func_actual = funciones_de_prueba[i]
    a_lim, b_lim = limites_de_integracion[i]
    exact_val_sympy = integrales_analiticas[i].evalf() # Valor analítico para la comparación

    print(f"\n--- Función {i+1}: '{func_actual.__doc__.strip()}' en [{a_lim:.4f}, {b_lim:.4f}] ---")
    print(f"Valor Analítico Exacto: {exact_val_sympy:.8f}")

    resultados_tabla = []
    for nombre_metodo, funcion_metodo in diccionario_metodos.items():
        resultado_numerico = funcion_metodo(func_actual, a_lim, b_lim)

        error_porcentual = "N/A" # 
        if i != 2: 
            if exact_val_sympy != 0:
                error_porcentual = abs((float(exact_val_sympy) - resultado_numerico) / float(exact_val_sympy)) * 100
                error_porcentual = f"{error_porcentual:.4f}%"
            else: 
                error_porcentual = "Indefinido (Exacto es 0)" if resultado_numerico != 0 else "0.00%"

        resultados_tabla.append({
            "Método": nombre_metodo,
            "Resultado Numérico": f"{resultado_numerico:.8f}",
            "Error Relativo (%)": error_porcentual
        })
    
    df_resultados = pd.DataFrame(resultados_tabla)
    print(df_resultados.to_string(index=False))
    print("-" * 50)

