"""La empresa ACME desea calcular el valor de la nómina de N empleados (estos N empleados son
ingresados por el usuario), tanto el sueldo bruto como el sueldo neto. El sueldo bruto se calcula a partir
del valor de la hora y la cantidad de horas trabajadas. A esto se le descuenta el valor de la EPS que es el
4%, el valor de la Pensión que es el 4%. El sueldo neto es el sueldo bruto menos los descuentos. Por
cada empleado se quiere mostrar, el valor del sueldo bruto, cada uno de los descuentos y el valor del
sueldo Neto. Para este ejercicio el valor de la hora es $20.000.
Al final se debe mostrar una estadística con los totales de los salarios brutos, EPS, Pensión y salarios
netos. Luego mostrar el empleado que más gana en salario neto (nombre y salario neto), el empleado
que menos gana en salario neto (nombre y salario neto) y los promedios de sueldos brutos y sueldos
netos.
"""
nempleados = int(input("Ingrese el numero de empleados: "))
valorhora = 20000

nombremayor = ""
nombremenor = ""
valoreps = 0
sueldobrutototal = 0
pensiontotal = 0
sueldonetotal = 0
sueldonetomenor = 0
sueldonetomayor =0


#MOSTRAR SUELDOBRUTO,DESCUENTOS,SUELDO,NETO X CADA EMPLEADO
for empleados in range(nempleados):
    
    numero = input("Ingrese el nombre de los empleados: ")
    horas = int(input("Ingrese el numero de horas trabajadas: "))

    sueldobruto = valorhora * valorhora
    eps = sueldobruto * 0.04
    pension = sueldobruto * 0.04
    descuento = (eps + pension)
    sueldoneto = sueldobruto -eps- descuento
    print("Nombre: ", numero)
    print("Salario bruto: $", sueldobruto)
    print("EPS: $", eps)
    print("Pension: $", pension)
    print("Salario neto: $", sueldoneto)

    if empleados >= 0 and empleados<= nempleados:
        
        #ESTADISTICAS
        sueldobrutototal += sueldoneto
        valoreps += eps
        pensiontotal += pension
        sueldonetotal += sueldoneto
      # busqueda del salario neto mayor y menor
    if sueldoneto > sueldonetomenor:
        sueldonetomayor = sueldoneto
        nombremayor = numero
    if empleados == 0 or sueldoneto < sueldonetomenor:
        salarioNetoMenor = sueldoneto
        nombremenor = numero
        
        
#PROMEDIO
# calculo de los promedios    
        promediosueldobruto= sueldobrutototal / nempleados
        promediosueldoneto = sueldonetotal / nempleados

print("-"*45)
print(f"El sueldo bruto total es: ${sueldobrutototal}")
print(f"El sueldo neto total es: ${sueldonetotal}")
print(f"El valor total de la eps es: ${valoreps}")
print(f"La pension total es{pensiontotal}")
print(f"El empleado {nombremayor} tiene el mayor salario neto {sueldonetotal}")
print(f"El empleado {nombremenor} tiene el menor salario neto {sueldonetotal}")

    
