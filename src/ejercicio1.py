def detectarDivisa(divisa:str, diccionarioDivisas:dict)->bool:
    """Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

    Args:
        divisa (str): Es la divisa que se desea verificar.
        diccionarioDivisas (dict): El diccionario que contiene las divisas.

    Returns:
        bool: retorna True si la divisa está en el diccionario, False en otro caso.
    """
    if divisa.capitalize() in diccionarioDivisas:
        return True
    else: 
        return False
def main():
    diccionarioDivisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = input("Ingrese una divisa: ")
    if detectarDivisa(divisa, diccionarioDivisa):
        print(f"La divisa {divisa} es una divisa valida")
    else:
        print(f"La divisa {divisa} no es una divisa valida")
if __name__ == "__main__":
    main()