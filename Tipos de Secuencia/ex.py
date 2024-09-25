'''
# Realiza un programa que compruebe si una cadena de leída por teclado comienza por una subcadea introducida por teclado
EX 1 
cad = input("Introduce una cadena: ")
subcad = input('Introduce una subcad: ')

if cad.startswith(subcad):
    print('Empieza por la subcadena')
else:
    print('No comienza por la subcadena')

if cad in subcad:
    print("Empieza por la subcadena)
else:
    print("La cadena no contiene la subcadena")
'''

'''
EX 2
# Pide una cadena por teclado (valida q sea un caracter) y mustra cuantas veces aparece el caracter en la cadena

while True:
    car = input('Introduce un caracter: ')
    if len(car)>1:
        print('Un solo caracter')
    if len(car) == 1: break

print("En la cadena ", cad," aparecen ",cad.count(car), "veces el caracter")
'''

'''
EX 2
# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios)
# realiza un programa que cuente cuantas palabras tiene
SOLUCIÓN 1 ---------------------------------------------------------------------------
# Si contamos palabras necitamos un contador
cont = 0
posicion = 0
# Elimino los posibles espacios que haya al principio y al final de la cadena
cad = cad.strip()
# Voy buscando los espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
    cont += 1
    # No tengo en cuenta los posibles espacios que haya entre las palabras
    while cad[posicion + 1] == " ":
        posicion += 1
    posicion = cad.find(" ", posicion + 1)
print('La frase tiene ', cont + 1, ' palabras.')

SOLUCIÓN 2 -------------------------------------------------------------------------------
# Eliminar espacios en blanco al principio y al final
cadena = cad.strip()
# Dividir la cadena en palabras
palabras = cadena.split()
# Contar el número de palabras
numero_palabras = len(palabras)
# Imprimir el resultado
print('La frase tiene', numero_palabras, 'palabras.')
'''

'''
LISTAS
.append() = añadir
.extend() =  concaternar dos listas
.insert(0, 1) = añadir elemento desde la posicion a donde añadir
.pop() = devuelve ultimo elemento y elimina
.pop(1) = devuelve el numero de la lista y lo eliminar
.remove(3) = elimina el numero 3
.reverse() = inveretir
.sort() = ordenar
.sort(reverse=True) = ordena de manera inversa
.count() = cuantas veces aparece el elemento
.index() = en que posicion esta el numero q buscas
'''

'''
Realiza un programa que inicialice una lista de 10 valores aleatorios y posteriormiente muestre
en pantalla cada elemento de una lista junto a su cubo

import random

list_num = []
for i in range(1,11):
    list_num.append(random.randint(1, 10))
for num in list_num:
    print(num," ", num ** 2," ", num ** 3)

'''

'''
Ejercicio 2
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra 
sus elementos por la pantalla.

# Paso 1: Crear lista e inicializarla con 5 cadenas
lista_original = []
for i in range(5):
    cadena = input("Introduce una cadena de caracteres: ")
    lista_original.append(cadena)

# Paso 2: Crear una lista en orden inverso
lista_invertida = lista_original[::-1]

# Paso 3: Mostrar los elementos de la lista invertida
for elemento in lista_invertida:
    print(elemento)
'''

'''
Ejercicio 3
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por 
un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, 
la nota media, la nota más alta que ha sacado y la menor.

# Inicializamos la lista para almacenar las notas
notasAlum = []

# Bucle para pedir 5 notas
for i in range(5):
    while True:  # Bucle infinito hasta que el usuario ingrese una nota válida
        notas = input(f"Dime la nota del examen {i + 1}: ")
        try:
            nota_float = float(notas)  # Intentamos convertir a número flotante
            if 0 <= nota_float <= 10:  # Validamos que la nota esté entre 0 y 10
                notasAlum.append(nota_float)
                break  # Si es válida, salimos del bucle
            else:
                print("Error: la nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: la nota debe ser un número. Inténtalo de nuevo.")

# Cálculo de la media
media = sum(notasAlum) / len(notasAlum)
nota_max = max(notasAlum)
nota_min = min(notasAlum)

# Mostrar la media con dos decimales
print(f"La media de tus notas es: {media:.2f}")
print(f"La nota más alta es: {nota_max}")
print(f"La nota más baja es: {nota_min}")

''' 

'''
Ejercicio 4
Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número 
negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).

# Declaramos una lista
lista = []

while True:
    numero = int(input("Introduce un número (negativo para terminar): "))
    # Si el número es negativo, salimos del bucle
    if numero < 0:
        break
    # Si el número es positivo o cero, lo añadimos a la lista
    lista.append(numero)

print("Los números que introdujiste son:", lista)
'''

'''
Ejercicio 5
Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), 
y posterior ordene los elementos de menor a mayor.

import random
num = []
for i in range(1, 11):
    num.append(random.randint(1,10))
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
'''

'''
Ejercicio 6
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y 
diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. 
Para simplificarlo vamos a suponer que febrero tiene 28 días.

import calendar
year = int(input("Dime el año: "))
month = int(input("Dime el numero del mes: "))
_, num_days = calendar.monthrange(year, month)

print(f"El mes {month} del año 2024 tiene {num_days} días")
'''

'''
Ejercicio 7
Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, 
pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

import random

# Inicializar listas vacías
l1 = []
l2 = []
l3 = []

# Rellenar las listas con 5 enteros aleatorios
for _ in range(5):
    l1.append(random.randint(0, 100000))  # Añadir números a lista1
    l2.append(random.randint(9999, 100000))  # Añadir números a lista2

# Calcular lista3 como la suma de lista1 y lista2
l3 = [a + b for a, b in zip(l1, l2)]

# Imprimir las listas
print("Lista 1:", l1)
print("Lista 2:", l2)
print("Lista 3 (suma de lista1 y lista2):", l3)

'''
 
'''
Ejercicio 8
Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa 
que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará 
cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
'''
alumnos = []

addName = input("Name: ")
addSurname = input("Surname: ")

alumnos.extend(addSurname)


print(alumnos)


'''
Todos lo alumnos mayores de edad.
Los alumnos mayores (los que tienen más edad)
Ejercicio 9
Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:

La temperatura media de cada día
Los días con menos temperatura
Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
Ejercicio 10
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
Carga la tabla con valores numéricos enteros.
Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.
Ejercicio 11
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
Muestra el contenido de la tabla en pantalla.
Ejercicio 12
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.

  111111111111111
  100000000000001
  100000000000001
  100000000000001
  111111111111111
Visualiza el contenido de la matriz en pantalla.

Ejercicio 13
De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.

Para guardar esta información se van a utilizar dos arreglos:

Nombre: Lista para guardar los nombres de los conductores.
kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.

Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

Ejercicio 14
Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:

Las cantidades totales de cada articulo.
La cantidad de artículos en la sucursal 2.
La cantidad del articulo 3 en la sucursal 1.
La recaudación total de cada sucursal.
La recaudación total de la empresa.
La sucursal de mayor recaudación.
Ejercicio 15
Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:

Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
de la tabla anterior, y en la segunda los goles del otro equipo.
El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?

Ejercicio 16
Vamos a crear un programa que tenga el siguiente menú:

Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
Longitud de la lista: te muestra el número de elementos de la lista.
Eliminar el último número: Muestra el último número de la lista y lo borra.
Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
Mostrar números: Muestra los números de la lista
Salir
Ejercicio 17
Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

Ejercicio 18
Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
Eliminar: Me pide una cadena, y la elimina de la lista.
Mostrar: Muestra la lista de cadenas
Terminar
'''




