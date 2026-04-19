# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:05:55 2023

@author: alber
"""

import re

# Función para eliminar líneas con enlaces y líneas en blanco resultantes
def eliminar_lineas_con_enlaces(texto):
    # Patrón de expresión regular para detectar líneas con enlaces
    patron_linea_con_enlace = r'^.*https?://[^\s]+.*$'
    
    # Utilizamos la función sub() para reemplazar las líneas con enlaces por una cadena vacía
    texto_sin_lineas_con_enlaces = re.sub(patron_linea_con_enlace, '', texto, flags=re.MULTILINE)
    
    # Eliminamos las líneas en blanco resultantes
    lineas = texto_sin_lineas_con_enlaces.split('\n')
    lineas_sin_enlaces = [linea for linea in lineas if linea.strip()]
    
    # Concatenamos las líneas sin enlaces nuevamente en un solo texto
    resultado = '\n'.join(lineas_sin_enlaces)
    
    return resultado

# Nombre del archivo de entrada y salida
archivo_entrada = 'archivo_sin_media.txt'
archivo_salida = 'archivo_sin_enlaces.txt'

try:
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
        contenido = entrada.read()
    
    contenido_sin_lineas_con_enlaces = eliminar_lineas_con_enlaces(contenido)
    
    with open(archivo_salida, 'w', encoding='utf-8') as salida:
        salida.write(contenido_sin_lineas_con_enlaces)
    
    print(f'Se han eliminado las líneas con enlaces y las líneas en blanco resultantes. El resultado se ha guardado en "{archivo_salida}".')

except FileNotFoundError:
    print(f'El archivo "{archivo_entrada}" no se encuentra.')

except Exception as e:
    print(f'Ocurrió un error: {str(e)}')


