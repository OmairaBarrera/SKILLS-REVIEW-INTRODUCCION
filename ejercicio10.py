"""10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato"""

mes=input("Ingresa el mes: ")
valor=float(input("Ingresa el valor de Kw: "))
kw=int(input("Ingresa consumo del mes en Kw: "))
estrato=input("Ingresa el extrato: ")

if estrato==1 or estrato==2:
    valorPagar=valor*kw
    print(f'El valor a pagar en el mes de {mes} es: {valorPagar-(valorPagar*0.6)}')
elif estrato==3:
    valorPagar=valor*kw
    print(f'El valor a pagar en el mes de {mes} es: {valorPagar-(valorPagar*0.15)}')
else:
    valorPagar=valor*kw
    print(f'El valor a pagar en el mes de {mes} es: {valorPagar}')