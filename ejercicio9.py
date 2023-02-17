"""9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad."""

#Librerias
from datetime import datetime
#variables
opcion = ""
# metodo recepción de datos del empleado
def agregar_empleado():
    # Fecha y año actuales
    date = datetime.now()
    year_now = date.year
    # Ingreso de datos
    print("")
    name = input("Ingrese su nombre: ")
    last_name = input("Ingrese sus apellidos: ")
    phone = input("Ingrese su numero telefonico: ")
    age = input("Ingrese su edad: ")
    year_in = int(input("Ingrese el año de ingreso a la empresa: "))
    # Validando que el año ingresado sea menor a la fecha actual
    while(year_in > year_now):
        print("Año de ingreso incorrecto, vuelva a ingresar el dato.")
        year_in = int(input("Ingrese el año de ingreso a la empresa: "))
    # Devolución de datos
    print("")
    print("Sus datos son:")
    print("Nombre: ", f"{name}")
    print("Apellidos: ", f"{last_name}")
    print("Años de Antiguedad: ", f"{year_now - year_in}")
    print("")

print("Bienvenido al sistema de registro de empleados")
print("")
#### Recepción de Opciones ###
while(opcion != "2"):
    print("Digite la opción que desee: ")
    print("1. Ingresar un nuevo empleado.")
    print("2. Salir.")
    opcion = input()
    
    if(opcion == "1"):
        agregar_empleado()
    if(opcion == "2"):
        print("Gracias por ingresar")
    if (opcion != "1" and opcion != "2"):
        print("Opción no valida")