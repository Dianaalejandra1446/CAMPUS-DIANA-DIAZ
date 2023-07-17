Segundos = int(input("Ingrese la cantidad de segundos"))
Horas = Segundos // 3600
Minutos = (Segundos//60) % 60
Seconds = Segundos % 60
print(f"Horas={Horas}")
print(f"Minutos={Minutos}")
print(f"Segundoa={Seconds}")