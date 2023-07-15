#SUELDO BRUTO
valorhora = 20000
cantidadhoras =int(input("Ingrese la cantidad de horas trabajadas "))
#DESCUENTOS
sueldobruto= valorhora * cantidadhoras
valortotaleps = sueldobruto* 0.04
valortotalpension = sueldobruto* 0.04
#SUELDO NETO
sueldoneto = (sueldobruto)-valortotalpension-valortotaleps

print(f'Su cantidad de horas trabajadas son {cantidadhoras}\n Su valor por eps es {valortotaleps}\n Su valor por pension es{valortotalpension}\n Su sueldo bruto es {sueldobruto}\n Su sueldo neto es{sueldoneto}')