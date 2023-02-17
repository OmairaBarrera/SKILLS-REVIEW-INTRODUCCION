"""Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados."""

print("Condicionales anidados")
x=int(input(f'Ingresa Primer Numero: '))
y=int(input(f'Ingresa Segundo Numero: '))

if x>y:
    r=x*y
    print(f'Se multiplican los numeros {x}*{y}={r}')
    if r>6:
        print(f'Se realiza subasta')
    else:
        print(f'Sigue intentando')
elif x<y:
    r=x+y
    print(f'Se suman los numeros {x}+{y}={r}')
    if r==3:
        print(f'Se realiza donación')
    else:
        print(f'sigue intentando')
else:
    print(f'sigue intentando')