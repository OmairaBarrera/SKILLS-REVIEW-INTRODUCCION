""" Cuál es la diferencia entre un condicional simple y un
condicional compuesto? """
x=int(input("Ingresa un numero: "))
print(f'Un condicional simple, es aquel que ejecuta un proceso solo si la condición se cumple')
if x>5:
    print(f'El numero es mayor que cinco')
print(f'Un condicional compuesto, es aquel que ejecuta proceso si se cumple o no la condición')
if x>5:
    print(f'El numero es mayor que cinco')
else:
    print(f'El numero es menor que cinco')
