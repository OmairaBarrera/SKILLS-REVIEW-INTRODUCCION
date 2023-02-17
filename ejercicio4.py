""" 4. Que son las expresiones regulares en Python? """
import re

print(f'Expresiones regulares')
print(f'se puede considerar un mini leguaje de programacion dentro de otro, son secuencias de caracteres que forman un patron de busqueda')
print(f'Expresion regular para hacer una busqueda y localizarlo donde coincida')
cadena="Investigacion de expresiones regulares"
print(re.search("regulares", cadena))


