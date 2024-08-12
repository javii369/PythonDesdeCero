# Realiza un algoritmo que muestre la tabla de multiplicar de un numero introducido por el teclado.

tabla = int(input('Dime de que numero quieres la tabla de multiplicar'))
for num in range(1,11):
    print("%d + %d = %d" % (num, tabla, num*tabla))
