# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 00:03:10 2025

@author: Asus
"""
import numpy as np
import matplotlib.pyplot as plt


valores_x = np.linspace(0, 2 * np.pi, 500)

# --- Trazado de las Funciones ---

plt.figure(figsize=(10, 6)) 

plt.plot(valores_x, np.sin(valores_x), label="Función Seno ($\sin(x)$)", color='steelblue', linestyle='-')

plt.plot(valores_x, np.cos(valores_x), label="Función Coseno ($\cos(x)$)", color='darkorange', linestyle='--')


tan_y = np.tan(valores_x)
tan_y[tan_y > 10] = np.nan 
tan_y[tan_y < -10] = np.nan 
plt.plot(valores_x, tan_y, label="Función Tangente ($\tan(x)$)", color='mediumseagreen', linestyle='-.')

# --- Personalización Adicional del Gráfico ---

plt.ylim(-5, 5) 
plt.xlabel("Valor de x (radianes)", fontsize=12)
plt.ylabel("Valor de y", fontsize=12)
plt.title("Gráfico de Funciones Trigonométricas Básicas", fontsize=16)

plt.legend(loc='upper right', fontsize=10) # Ubicamos la leyenda para no superponerse
plt.grid(True, linestyle=':', alpha=0.7) # Cuadrícula más suave

plt.axvline(x=np.pi/2, color='gray', linestyle=':', linewidth=0.8, label='Asíntota en $\pi/2$')
plt.axvline(x=3*np.pi/2, color='gray', linestyle=':', linewidth=0.8)
plt.text(np.pi/2 + 0.1, 4, r'Asíntota en $\frac{\pi}{2}$', fontsize=10, color='dimgray')


plt.tight_layout() 
plt.show()