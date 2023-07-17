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


#MOSTRAR SUELDOBRUTO,DESCUENTOS,SUELDO,NETO X CADA EMPLEADO
for empleados in range(0,nempleados):
    numero = input("Ingrese el nombre de los empleados: ")
    horas = int(input("Ingrese el numero de horas trabajadas: "))
    sueldobruto = valorhora * horas
    eps = sueldobruto * 0.04
    pension = sueldobruto * 0.04
    descuento = (eps + pension)
    sueldoneto = sueldobruto - descuento
    if empleados >= 0 and empleados<= nempleados:
        print(f"El sueldo bruto del empleado {numero} es {sueldobruto},sus descuentos son {descuento}, y su sueldo neto es {sueldoneto}\n")
#MOSTRAR TOTALES 
        #ESTADISTICAS
        print("-"*45)
        totaleps = eps * nempleados
        print(f"La estadistica total de eps de los {nempleados} empleados es: {totaleps}")
        totalbruto = sueldobruto * nempleados
        print(f"La estadistica total de la pension de los {nempleados} empleados es: {totalbruto}")
        totalpension = pension * nempleados
        print(f"La estadistica total de la pension de los {nempleados} empleados es: {totalpension}")
        totalneto = sueldoneto * nempleados
        print(f"La estadistica total de sueldo neto de los {nempleados} empleados es: {totalneto}")
#PROMEDIO


    
