def crearDiccionarioUsuarios(diccionarioUsuarios:dict, usuarios:int, nombre:str, edad:int, sexo:str, telefono:int, correo:str)->dict:
    """Crea un diccionario donde la clave es la asignatura y el valor el credito que ofrece dicha asignatura.

    Args:
        nombre (str): nombre de la asignatura.
        creditos (int): los créditos que ofrece la asignatura.

    Returns:
        dict: el diccionario donde la clave es la asignatura y el valor el credito
    """
    diccionarioUsuarios["usuario"+str(usuarios)] = [nombre, edad, sexo, telefono, correo] 
    return diccionarioUsuarios
def main():
    """Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
    """
    usuarios = 0
    diccionarioUsuarios = {}
    while usuarios < 4:
        try:
            nombre = input("Ingrese el nombre del usuario: ")
            edad = int(input("Ingrese la edad del usuario: "))
            sexo = input("Ingrese el sexo del usuario: ")
            telefono = int(input("Ingrese el número de teléfono del usuario: "))
            correo = input("Ingrese el correo del usuario: ")
            crearDiccionarioUsuarios(diccionarioUsuarios, usuarios, nombre, edad, sexo, telefono, correo)
            usuarios += 1
            print(diccionarioUsuarios)
        except ValueError:
            print("No se ingresaron datos correctos")
if __name__ == "__main__":
    main()