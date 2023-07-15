#HORA INICIAL
hora = int(input("Ingrese su hora "))
minutos = int(input("Ingrese sus minutos "))
print(f"Su hora es {hora}:{minutos}")
minutosadicionales = int(input("Ingrese sus minutos adicionales "))

#TOTAL HORA INICIAL
sumatotalminutos= (hora*60) + minutos + minutosadicionales
hora= sumatotalminutos // 60
minutos= sumatotalminutos -(hora*60)

print(f"Su nueva hora es de {hora}:{minutos}")



