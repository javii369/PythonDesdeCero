#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de 
#apariciones de cada carácter en la cadena.

dic = {}
cadena = input('Dame una cadena:')
for caracter in cadena:
    if caracter in dic:
        dic[caracter]+=1
    else:
        dic[caracter]=1

for campo,valor in dic.items():
    print(campo, "->", valor)


# Ejercicio 3
# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir 
# los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
''''
price = {"apple" : 2, "orange" : 1.5 , "banana" : 3}
while True:
    fruit = input("Dime la fruta que has vendido")
    if fruit.lower() not in price:
        print("Fruta no existe")
    else:

'''