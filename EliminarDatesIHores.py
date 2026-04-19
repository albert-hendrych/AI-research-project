# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:45:29 2023

@author: alber
"""

import re

# Function to remove dates and times
def remove_dates_times(text):
    # Date and time pattern (dd/mm/yy, hh:mm)
    pattern = r'\d{1,2}/\d{1,2}/\d{1,2}, \d{1,2}:\d{1,2} - '

    # Use the re.sub function to replace the pattern with an empty string
    text_without_dates = re.sub(pattern, '', text)
    
    return text_without_dates

# Read the input file with UTF-8 encoding
with open('WhatsApp_Chat_with_Arnau_Ciurana.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()

# Call the function to remove dates and times
content_without_dates = remove_dates_times(content)

# Write the content without dates and times to a new file with UTF-8 encoding
with open('archivo_sin_fechas.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(content_without_dates)

print("Dates and times have been removed, and the new file has been created.")
