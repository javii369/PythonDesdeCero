#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
#Escribir un algoritmo que determine la hora de llegada a la ciudad B.

hpartida = int(input('Hora de salida: '))
minpartida = int(input('Minutos de salida: '))
segpartida = int(input("segundos de salida:"))
segviaje = int(input("Tiempo que has tardado en segundos: "))

# Convertir la hora de salida en segundos
segundos = hpartida * 3600 + minpartida * 60 * segpartida
# Sumo los segundo q he tardado
sfinal = segundos + segviaje
# Convierto los segundo totales a hora, minuto y segundo
horallegada = sfinal // 3600
minllegada = (sfinal % 3600) // 60
segllegada = (sfinal % 3600) % 60

print("Hora de llegada: ", horallegada, ':', minllegada, ':', segllegada)