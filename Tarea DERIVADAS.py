# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:23:10 2025

@author: ASUS
"""
from scipy.misc import derivative

def funcion(x):
    return -x**2 - x/2 + 4

pasos = [0.2, 0.1]
x = 0
#--------------------------------------------------------------------
def forward(f, x, h):
    return (-f(x + 2*h) + 4*f(x + h) - 3*f(x)) / (2*h)

def backwards(f, x, h):
    return (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2*h)

def centered(f, x, h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h)

print("===== DERIVADA ANALÍTICA =====")
for h in pasos:
    real = derivative(funcion, x, dx=h)
    print(f"h = {h} -> Derivada: {real:.6f}")

print("\n===== DERIVADAS NUMÉRICAS Y ERRORES =====")
for h in pasos:
    real = derivative(funcion, x, dx=h)

    d1 = forward(funcion, x, h)
    d2 = backwards(funcion, x, h)
    d3 = centered(funcion, x, h)

    e1 = abs((real - d1) / real) * 100
    e2 = abs((real - d2) / real) * 100
    e3 = abs((real - d3) / real) * 100

    print(f"\nh = {h}")
    print(f"Adelante: {d1:.6f} | Error: {e1:.2f}%")
    print(f"Atrás:    {d2:.6f} | Error: {e2:.2f}%")
    print(f"Centrada: {d3:.6f} | Error: {e3:.2f}%")

