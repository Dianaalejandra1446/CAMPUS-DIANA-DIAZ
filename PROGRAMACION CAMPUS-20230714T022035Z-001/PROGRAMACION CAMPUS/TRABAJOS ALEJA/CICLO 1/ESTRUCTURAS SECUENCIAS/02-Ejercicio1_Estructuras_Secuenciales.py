nombre =(input("Ingrese su nombre "))
placa = (input("Ingrese su placa "))
valorpasajes = int(input("Ingrese el valor total de pasajes "))
valorencomienda = int(input("Ingrese el valor total por ecomiendas "))

valortotalpasajes  = valorpasajes * 0.25
valortotalencomiendas = valorencomienda * 0.15
valortotalconductor= valortotalencomiendas + valortotalpasajes

print("Su nombre es",nombre)
print ("Su numero de placa es",placa)
print ("El valor de total de pasajes es",valorpasajes)
print("El valor total por concepto de pasaje es",valortotalpasajes)
print ("El valor de ecomienda es",valorencomienda)
print("El valor total por concepto de encomiendas",valortotalencomiendas)


print("El valor total del conductor es",valortotalconductor)


