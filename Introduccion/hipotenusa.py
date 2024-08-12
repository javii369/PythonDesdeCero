# Dados los catetos de un triangulo rectangulo, calcula su hipotenusa.

import math

c1= float(input('Introduce el cateto 1: '))
c2= float(input('Introduce el cateto 2: '))
h = math.sqrt(c1 ** 2 + c2 ** 2)
print('La hipotenusa es: %.2f ' %h)