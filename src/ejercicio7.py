def crearCarrito(carrito:dict, producto:str, precio:float)->dict:
    """Crea un diccionario donde la clave es la asignatura y el valor el credito que ofrece dicha asignatura.

    Args:
        nombre (str): nombre de la asignatura.
        creditos (int): los créditos que ofrece la asignatura.

    Returns:
        dict: el diccionario donde la clave es la asignatura y el valor el credito
    """
    carrito[producto] = precio
    return carrito
def calcularTotal(carrito:dict)->float:
    """calcula el total de los productos de un carrito.

    Args:
        carrito (dict): el carrito de la compra.

    Returns:
        float: el precio total de los productos de un carrito.
    """
    total = 0
    for precio in carrito.values():
        total += precio
    return round(total, 2)
def main():
    """Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
    """
    entrada = True
    carrito = {}
    while entrada:
        try:
            producto = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese la precio del producto: "))
            crearCarrito(carrito, producto, precio)
            entrada = input("Desea ingresar otro producto? (S/N): ").upper()
            if entrada == "S":
                entrada = True
            elif entrada == "N":
                entrada = False
            else:
                print("Debe ingresar S o N")
        except ValueError:
            print("No se ingresaron datos correctos")
    print("-"*100)
    print(f"Lista de la compra\n---------------------------")
    for producto, precio in carrito.items(): 
        print(f"{producto}\t\t {precio}€")
    print("-"*20)
    print(f"total\t\t {calcularTotal(carrito)}€")

if __name__ == "__main__":
    main()