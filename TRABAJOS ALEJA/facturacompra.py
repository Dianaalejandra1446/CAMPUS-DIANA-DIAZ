"""Se trata de escribir el algoritmo evaluque permita emitir la factura correspondiente a una compra de un
artículo determinado, del que se adquieren una o varias unidades. El IVA por aplicar es del 15 por
100 y si el precio bruto (precio venta más IVA) es mayor de 1.000 euros, se debe realizar un
descuento del 5 por 100.
"""
nomarti = input("Ingrese su articulo \n")
precioarti = float(input("Introduce el precio del articulo: \n"))
cantidad = int(input("Introduce la cantidad de articulos comprados: \n"))

#Calcular precio sin iva
siniva = precioarti * cantidad
#Calcular iva aplicado
coniva = siniva * 0.15
# Calcular el precio total con IVA incluído
preciototal = siniva + coniva
# Verificar si el precio total es mayor de 1000 euros para aplicar descuento
if preciototal > 1000:
    descuento = preciototal * 0.05
    preciodesc = preciototal - descuento
else:
    descuento = 0
    preciodesc =  preciototal - descuento
print("FACTURA \n")
print(f"Articulo: {nomarti}")
print("La cantidad total de articulos adquiridos es de: \n " + str(cantidad))
print(f"Su precio total a pagar con iva es\n: {preciodesc}")

