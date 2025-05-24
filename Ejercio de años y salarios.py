# -*- coding: utf-8 -*-
"""
Created on Mon May 19 00:05:20 2025

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

data_url = 'https://raw.githubusercontent.com/ybfoundation/Dataset/main/Salary_Data.csv'
try:
    data_frame = pd.read_csv(data_url)
except Exception:
    fallback_data = """Experience Years,Salary
1.1,39343
1.2,42774
1.3,46205
1.5,37731
2.0,43525
2.2,39891
2.5,48266
2.9,56642
3.0,60150
3.2,54445
3.2,64445
3.5,60000
3.7,57189
3.8,60200
3.9,63218
4.0,55794
4.0,56957
4.1,57081
4.3,59095
4.5,61111
4.7,64500
4.9,67938
5.1,66029
5.3,83088
5.5,82200
5.9,81363
6.0,93940
6.2,91000
6.5,90000
6.8,91738
7.1,98273
7.9,101302
8.2,113812
8.5,111620
8.7,109431
9.0,105582
9.5,116969
9.6,112635
10.3,122391
10.5,121872
"""
    data_frame = pd.read_csv(StringIO(fallback_data))

years_exp = data_frame['Experience Years']
income = data_frame['Salary']
lin_reg_slope, lin_reg_intercept = np.polyfit(years_exp, income, 1)

print(f"Ecuación de Regresión Lineal: Salario = {lin_reg_slope:.2f} * Años de Experiencia + {lin_reg_intercept:.2f}")
print("\nPredicciones de Salario:")
for experience_years in [15, 30, 50]:
    predicted_salary = lin_reg_slope * experience_years + lin_reg_intercept
    print(f"Para {experience_years} años: Salario previsto = ${predicted_salary:,.0f}")

plt.figure(figsize=(10, 6))
plt.scatter(years_exp, income, color='blue', label='Datos Originales')
regression_line_x = np.array([years_exp.min(), years_exp.max()])
plt.plot(regression_line_x, lin_reg_slope * regression_line_x + lin_reg_intercept, color='red', linestyle='--', label='Línea de Regresión')
plt.title('Salario vs. Años de Experiencia')
plt.xlabel("Años de Experiencia")
plt.ylabel("Salario")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()
