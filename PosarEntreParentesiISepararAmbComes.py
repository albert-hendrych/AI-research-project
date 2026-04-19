# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:51:11 2023

@author: alber
"""

# Abre el archivo de entrada para lectura
with open('archivo_sin_nombres.txt', 'r', encoding='utf-8') as archivo_entrada:
    # Lee las líneas del archivo de entrada
    lineas = archivo_entrada.readlines()

# Abre el archivo de salida para escritura
with open('archivo_final.txt', 'w', encoding='utf-8') as archivo_salida:
    # Itera sobre cada línea y escribe la línea con comillas y coma en el archivo de salida
    for linea in lineas:
        # Elimina los caracteres de nueva línea al final de cada línea y agrega comillas
        linea_formateada = f'"{linea.strip()}",'
        archivo_salida.write(linea_formateada + '\n')

print("Proceso completado. El archivo de salida 'salida.txt' ha sido creado.")
