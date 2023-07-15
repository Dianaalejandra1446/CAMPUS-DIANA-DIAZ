"""Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una compra de un
artículo determinado, del que se adquieren una o varias unidades. El IVA por aplicar es del 15 por
100 y si el precio bruto (precio venta más IVA) es mayor de 1.000 euros, se debe realizar un
descuento del 5 por 100.
"""
factura = input("Ingrese el numero de factura: \n ")
uni = input("Articulo \n")
preciobruto = int(input("Ingrese su precio bruto: \n"))
iva= 0
if preciobruto > 1000:
    ivatotal = iva
    iva = preciobruto * 5 / 100
    print(f"Su factura es {factura} y su iva es de: {iva}")
elif preciobruto <= 1000:
    ivatotal = iva
    iva = preciobruto * 15 / 100
    print(f"Su factura es {factura} y su iva es de: {iva}")


