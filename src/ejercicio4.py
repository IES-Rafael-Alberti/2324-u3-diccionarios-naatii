def calcularMes(mes:int)->str:
    """Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

    Args:
        mes (int): El número de mes que se quiere calcular el nombre 

    Returns:
        str: El mes en formato string.
    """
    meses = {1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"}
    if mes in meses: return meses[mes]
    else: return ""
def main():
    fecha = input("Ingrese una fecha con formato dd/mm/aaaa: ").split("/")
    mes = calcularMes(int(fecha[1]))
    if mes!= "":
        print(f"{fecha[0]} de {mes} de {fecha[2]}")
    else:
        print("El formato de la fecha ingresada no es correcto.")
if __name__ == "__main__":
    main()