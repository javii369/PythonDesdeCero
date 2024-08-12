#Ejercicios estructuras alternativas

"""
Ejercicio 1
Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

num1 = int(input('Dame un numero de dos cifras: '))
n_str = str(num1)
a = int(n_str[0])
b = int(n_str[1])

if a > b:
    print('El numero ', a, ' es mas grande que el', b)
print('El numero ', b, ' es mas grande que el ', a)

"""

"""
Ejercicio 2
Algoritmo que pida un número y diga si es positivo, negativo o 0.

num = int(input('Dame un número: '))
if num == 0:
    print('El numero es 0')
else:
    if num > 0:
        print('Es positivo')
    else:
        print('Es negativo')
"""

"""
Ejercicio 3
Escribe un programa que lea un número e indique si es par o impar.

num = int(input('Dame un número: '))
a = num % 2

if a == 0: 
    print('Es par')
else: print('Es inpar')
"""


"""
Ejercicio 4
Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, 
o un mensaje de aviso en caso contrario.
n1 = int(input('Dame el primer numero: '))
n2 = int(input('Dame el segundo numero: '))


if n2 == 0: 
    print('El segundo numero es 0, repitelo')
else: 
    a = n1 / n2
    print(a)
"""

"""
Ejercicio 5
Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.


user = str(input("Nombre de usuario: "))
psw = str(input("Contraseña: "))

if user == 'Pepe' and psw == '1234':
    print('Has entrado al sistema')
else:
    print('Usuario o contraseña incorrecto')

psw2 = '1234'
clave = input('Dime la clave')
        
while clave != psw2:
    print('Clave incorrecta')
    otra = input('¿Quieres introducir otra contrseña (S/N): ')
    if otra.upper() == "N":
        break;
    clave = input('Dime la clave')
if clave == psw2:
    print('Bienvenido!')
"""

"""
Ejercicio 6
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

leter = str(input('Dame una letra: '))

if leter == leter.upper():
    print('La letra es layuscula')
else: print('error')
"""

"""
Ejercicio 7
Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
- El exponente sea positivo, sólo tienes que imprimir la potencia.
- El exponente sea 0, el resultado es 1.
- El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = int(input('Dame un número: '))
exponente = int(input('Dame el exponente: '))

if exponente > 0:
    potencia = base ** exponente
    print(potencia)
elif exponente == 0:
    potencia = 1
    print(potencia)
else:  # exponente < 0
    potencia = base ** exponente
    print(potencia)
"""


"""
Ejercicio 8
Algoritmo que pida dos números "nota" y "edad" y un carácter "sexo" y muestre el
mensaje "ACEPTADA" si la nota es mayor o igual a cinco, la edad es mayor o igual a
dieciocho y el sexo es "F". En caso de que se cumpla lo mismo, pero el sexo sea "M", debe
imprimir "POSIBLE". Si no se cumplen dichas condiciones se debe mostrar "NO ACEPTADA".

nota = int(input('Dame tu nota: '))
edad = int(input('Dame tu edad: '))
sexo = input('Dame tu sexo (F o M): ').strip().upper()

if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print('ACEPTADA')
    elif sexo == 'M':
        print('POSIBLE')
    else:
        print('NO ACEPTADA')
else:
    print('NO ACEPTADA')
"""

"""
Ejercicio 9
Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

n1 = int(input('1r num:'))
n2 = int(input('2n num:'))
n3 = int(input('3r num:'))

list = [n1, n2, n3]
list.sort()
print('El orden es', list)
"""

"""
Ejercicio 10
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
circunferencias y las clasifique en uno de estos estados:

exteriores
tangentes exteriores
secantes
tangentes interiores
interiores
concéntricas

import math

x1 = int(input('Dame x1: '))
x2 = int(input('Dame x2: '))
r1 = int(input('Dame r1: '))

y1 = int(input('Dame y1: '))
y2 = int(input('Dame y2: '))
r2 = int(input('Dame r2: '))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Clasificar la relación entre las circunferencias
if d > r1 + r2:
    estado = "Exteriores"
elif d == r1 + r2:
    estado = "Tangentes exteriores"
elif abs(r1 - r2) < d < r1 + r2:
    estado = "Secantes"
elif d == abs(r1 - r2):
    estado = "Tangentes interiores"
elif d < abs(r1 - r2):
    estado = "Interiores"
else:  # d == 0 y r1 == r2 se considera como concéntricas si los radios son diferentes
    if d == 0 and r1 != r2:
        estado = "Concéntricas"
    else:
        estado = "Coincidentes"  # Para el caso d == 0 y r1 == r2

# Imprimir el resultado
print(f"Las circunferencias son: {estado}")

"""

"""
Ejercicio 11
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

Si se cumple Pitágoras entonces es triángulo rectángulo
Si sólo dos lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""

"""
Ejercicio 12
Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, 
excepto que también sea divisible por 400.

from datetime import date

# Solicitar al usuario que ingrese el día, el mes y el año
dia = int(input("Día: "))
mes = int(input("Mes: "))
year = int(input("Año: "))

# Función para determinar si un año es bisiesto
def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Validar la fecha utilizando datetime.date
try:
    fecha = date(year, mes, dia)
    print("Fecha correcta")
    if es_bisiesto(year):
        print(f"El año {year} es bisiesto.")
    else:
        print(f"El año {year} no es bisiesto.")
except ValueError:
    print("Fecha incorrecta")
"""

"""
Ejercicio 13
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

from datetime import date

# Solicitar al usuario que ingrese el día, el mes y el año
dia = int(input("Día: "))
mes = int(input("Mes: "))
year = int(input("Año: "))

try:
    fecha = date(year, mes, dia)
    print("Fecha correcta")
except ValueError:
    print("Fecha incorrecta")
"""

"""
Ejercicio 14
La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, 
ésta es de utamaño,n solo tipo y  se requiere determinarcuánto recibirá un productor por la uva que entrega en un embarque,
considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando 
es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es 
de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
"""



"""
Ejercicio 15
El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno
y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más,
el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son
menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.
"""

"""
Ejercicio 16
La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
"""

"""
Ejercicio 17
Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
Ejemplo:

Introduzca número del dado: 5
En la cara opuesta está el "dos".
"""

"""
Ejercicio 18
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.
"""

"""
Ejercicio 19
Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
"""
