#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
#Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

p1 = float(input("Dime la nota del parcial 1: "))
p2 = float(input("Dime la nota del parcial 2: "))
p3 = float(input("Dime la nota del parcial 3: "))

final = float(input("Dime la nota del examen final: "))
tr = float(input("Dime la nota del trabajo final: "))

nota = ((p1 + p2 + p3) / 3) * 0.55 + final * 0.3 + tr * 0.15

print("Nota: %.2f" %nota)