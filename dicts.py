female_baby_names_2012 = {1: 'EMMA', 2: 'LEAH', 3: 'SARAH', 4: 'SOPHIA', 5: 'ESTHER', 6: 'RACHEL', 7: 'CHAYA', 8: 'AVA', 9: 'CHANA', 10: 'MIRIAM', 11: 'ELLA', 12: 'EMILY', 13: 'MIA', 14: 'SARA', 15: 'CHARLOTTE', 16: 'ISABELLA', 17: 'MAYA', 18: 'ELIZABETH', 19: 'ABIGAIL', 20: 'ALEXANDRA', 21: 'VICTORIA', 22: 'LILY', 23: 'SOFIA', 24: 'RIVKA', 25: 'ZOE', 26: 'JULIA', 27: 'SOPHIE', 28: 'GABRIELLA', 29: 'HANNAH', 30: 'GRACE', 31: 'AVERY', 32: 'STELLA', 33: 'SHAINDY', 34: 'FAIGY', 35: 'GITTY', 36: 'MADISON', 37: 'MALKY', 38: 'EVA', 39: 'MALKA', 40: 'ALEXA', 41: 'MADELINE', 42: 'PENELOPE', 43: 'TOBY', 44: 'RIVKY', 45: 'NICOLE', 46: 'VIOLET', 47: 'NATALIE', 48: 'REBECCA', 49: 'MARIA', 50: 'YITTY', 51: 'NINA', 52: 'KATHERINE', 53: 'RILEY', 54: 'SIENNA', 55: 'SYDNEY', 56: 'VIVIENNE', 57: 'VALENTINA', 58: 'TALIA', 59: 'JOSEPHINE', 60: 'FRANCESCA', 61: 'ZISSY', 62: 'SURY', 63: 'NAOMI', 64: 'YIDES', 65: 'SKYLAR', 66: 'VERONICA', 67: 'TAYLOR', 68: 'ZOEY', 69: 'LILIANA', 70: 'YAEL', 71: 'SAVANNAH', 72: 'VANESSA', 73: 'SIMONE', 74: 'SLOANE', 75: 'VERA', 76: 'YEHUDIS', 77: 'SYLVIA', 78: 'SIMA', 79: 'SHAINA', 80: 'TZIPORA', 81: 'YITTA', 82: 'TZIVIA', 83: 'YARA'}


# Create an empty dictionary: names_by_rank

names_by_rank = {}
# Loop over the girl names
for rank, name in female_baby_names_2012.items():
    # Add each name to the names_by_rank dictionary using rank as the key
    names_by_rank[rank] = name
    
# Sort the names_by_rank dict by rank in descending order and slice the first 10 items
for rank in sorted(names_by_rank, reverse=True)[:10]:
    # Print each item
    print(names_by_rank[rank])

print('*' * 50)
#other exercise:

'''
Python proporciona una herramienta más rápida y versátil para ayudar con este problema en forma de .get() método.
El .get()método le permite proporcionar el nombre de una clave y, opcionalmente, lo que le gustaría que se devolviera si no se encuentra la clave.

'''
# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.get(105, 'Not Found'))


'''
Tratar con datos anidados
Un diccionario puede contener otro diccionario como el valor de una clave, y esta es una forma muy común de lidiar con estructuras de datos repetidas, como datos anuales, mensuales o semanales. Se aplican las mismas reglas al crear o acceder al diccionario.

Por ejemplo, si tuviera un diccionario que tuviera una clasificación de mi consumo de cookies por año y tipo de cookie. Podría parecer cookies = {'2017': {'chocolate chip': 483, 'peanut butter': 115}, '2016': {'chocolate chip': 9513, 'peanut butter': 6792}}. Pude acceder a la cantidad de galletas con chispas de chocolate que comí en 2016 usando cookies['2016']['chocolate chip'].

Al explorar un diccionario nuevo, puede resultar útil utilizar el .keys()método para tener una idea de los datos que podrían estar disponibles en el diccionario. También puede iterar sobre un diccionario y devolverá cada clave en el diccionario para que las use dentro del ciclo. Aquí, boy_namesse ha cargado un diccionario llamado en su espacio de trabajo. Consiste en todos los nombres masculinos en 2013 y 2014 .

Instrucciones

Imprime las claves del boy_namesdiccionario.
Imprime las claves del boy_namesdiccionario del año 2013.
Recorra el boy_namesdiccionario.
Dentro del bucle, imprima de forma segura el año y el tercer nombre clasificado. Imprimir 'Unknown'si no se encuentra el tercer nombre clasificado.

'''


# Print a list of keys from the boy_names dictionary
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(boy_names[2013].keys())

# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, 'Unknown'))
