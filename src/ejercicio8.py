def traducir(diccionario:dict, cadena:list)->str:
    """Traduce una frase usando un diccionario español a inglés.

    Args:
        diccionario (dict): diccionario español a inglés.
        cadena (str): caneda a traducir.

    Returns:
        str: frase traducida.
    """
    mensaje = ""
    for palabra in cadena:
        if palabra in diccionario:
            mensaje+=diccionario[palabra]+" "
        else:
            mensaje+= palabra +" "
    return mensaje
def crearDiccionario(diccionario:dict, significado:list)->dict:
    """Crea un diccionario donde la clave es la palabra en español y el valor la palabra en inglés.

    Args:
        diccionario (dict): diccionario en español a inglés.
        significado (str): pares de palabras en español-inglés.

    Returns:
        dict: diccionario en español a inglés.
    """
    diccionario[significado[0]] = significado[1]
    return diccionario
def main():
    """Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una palabra (por ejemplo palabra en español, palabra en inglés, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
    """
    seguir = ""
    diccionario = {}
    while seguir!= "salir":
        try:
            palabra = input("Ingrese una palabra en formato <español:inglés>: ").split(":")
            seguir = input("Desea traducir la frase? (si/no): ").lower()
            if seguir == "si":
                diccionario = crearDiccionario(diccionario, palabra)
            else:
                diccionario = crearDiccionario(diccionario, palabra)
                seguir = "salir" 
                
        except ValueError:
            print("No se ingresaron datos correctos")
    frase = input("Ingrese la frase a traducir: ").split(" ")
    print(traducir(diccionario, frase))
    
if __name__ == "__main__":
    main()