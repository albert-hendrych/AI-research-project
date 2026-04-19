# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:59:39 2023

@author: alber
"""

# Nombre del archivo de entrada
archivo_entrada = "archivo_sin_fechas.txt"

# Nombre del archivo de salida
archivo_salida = "archivo_sin_media.txt"

# Abrir el archivo de entrada en modo lectura
with open(archivo_entrada, "r", encoding="utf-8") as entrada:
    # Leer todas las líneas del archivo
    lineas = entrada.readlines()

# Filtrar las líneas que no contienen "<Media omitted>"
lineas_filtradas = [linea for linea in lineas if "<Media omitted>" not in linea]

# Abrir el archivo de salida en modo escritura
with open(archivo_salida, "w", encoding="utf-8") as salida:
    # Escribir las líneas filtradas en el archivo de salida
    salida.writelines(lineas_filtradas)

print(f"Se ha creado el archivo '{archivo_salida}' sin las líneas con '<Media omitted>'.")
