def calcularPrecio(fruta:str, kilos:float)->float:
    """Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

    Args:
        fruta (str): La fruta que se quiere calcular el precio.
        kilos (float): Los kilos que se quiere calcular el precio.

    Returns:
        float: El precio de ese número de kilos de fruta.
    """
    frutas = {'platano':1.35, 'manzana':0.80, 'pera':0.85,'naranja':0.70}
    if fruta in frutas:
        precio = kilos * frutas[fruta]
        return round(precio, 2)
    else:
        return 0
def main():
    fruta = input("Ingrese una fruta: ")
    kilos = float(input("Ingrese un número de kilos: "))
    precio = calcularPrecio(fruta, kilos)
    if precio != 0:
        print(f"El precio de {fruta} es de {precio:.2f}")
    else:
        print("esa fruta no está en el diccionario debe introducir una fruta válida")
if __name__ == "__main__":
    main()