"""
todo: contar dinero que queda por pagar y que se ha gastado.
"""
def crearDiccionarioFacturas(diccionario:dict, factura:int, costoFactura:float)->dict:
    """Crea un diccionario con el código de la factura y el costo de la factura.

    Args:
        diccionario (dict): diccionario con el código de la factura y el costo de la factura.
        factura (int): el código de la factura.
        costoFactura (float): el costo de la factura.

    Returns:
        dict: diccionario con el código de la factura y el costo de la factura.
    """
    diccionario[factura] = costoFactura
    return diccionario
def pagar(diccionario:dict, factura:int)->bool:
    """Operación que realiza el pago de una factura.

    Args:
        diccionario (dict): diccionario con el código de la factura y el costo de la factura.
        factura (int): el costo de la factura.

    Returns:
        bool: True si la factura fue pagada, False en caso contrario. 
    """
    if factura in diccionario:
        return True
    else:
        return False
def main():
    """
    Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
    """
    help = (
        """
        Esta es la ayuda del programa.
            [*] 1 -> añadir: añade una nueva factura a la lista de facturas pendientes de cobro.
            [*] 2 -> pagar: paga una factura de la lista de facturas pendientes de cobro.
            [*] 3 -> salir: termina el programa.
        """
        )
    diccionarioFacturas = {}
    entrada = 0
    costo = []
    pagado = 0
    while entrada != 3:
        try:
            print(help)
            entrada = int(input("Introduzca una orden: "))
            if entrada == 1:
                numeroFactura = int(input("Ingrese el número de factura: "))
                costoFactura = float(input("Ingrese el costo de la factura: "))
                pagado += costoFactura
                crearDiccionarioFacturas(diccionarioFacturas, numeroFactura, costoFactura)
            elif entrada == 2:
                numeroFactura = int(input("Ingrese el número de factura: "))
                print(diccionarioFacturas)
                if(pagar(diccionarioFacturas, numeroFactura)):
                    costo.append(diccionarioFacturas.pop(numeroFactura))
                    print("La factura fue pagada.")
                    print(f"pendiente de cobro: {sum(diccionarioFacturas.values())}€")
                    print(f"cobrado: {sum(costo):.2f}€")
                else:
                    print("La factura no fue pagada.")
                    print(f"pendiente de cobro: {sum(diccionarioFacturas.values()):.2f}€")
                    print(f"cobrado: {sum(costo):.2f}€")
            else:
                print(help)
        except ValueError:
            print("No se ingresaron datos correctos")
    print(diccionarioFacturas)
if __name__ == "__main__":
    main()