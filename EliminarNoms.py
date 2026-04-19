# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:16:06 2023

@author: alber
"""

import re

# Abre el archivo de entrada y crea un nuevo archivo de salida
with open('archivo_sin_enlaces.txt', 'r', encoding='utf-8') as archivo_entrada, open('archivo_sin_nombres.txt', 'w', encoding='utf-8') as archivo_salida:
    # Lee el contenido del archivo de entrada línea por línea
    for linea in archivo_entrada:
        # Utiliza una expresión regular para eliminar los nombres seguidos de ':'
        linea_limpia = re.sub(r'^[A-Za-z\s]+:\s', '', linea)
        # Escribe la línea limpia en el archivo de salida
        archivo_salida.write(linea_limpia)

print("Proceso completado. Los nombres y los dos puntos se han eliminado del archivo.")

