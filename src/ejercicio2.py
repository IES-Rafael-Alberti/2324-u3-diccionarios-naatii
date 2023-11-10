def registroUsuario(nombre:str, edad:int, direccion:str, telefono:int)->dict:
    """Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

    Args:
        nombre (str): El nombre del usuario.
        edad (int): La nombre del usuario
        direccion (str): La dirección del usuario.
        telefono (int): El número de teléfono del usuario.

    Returns:
        dict: El diccionario que contiene los datos del usuario.
    """
    diccionarioUsuario = {
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono
    }
    return diccionarioUsuario
def main():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    direccion = input("Ingrese su dirección: ")
    telefono = int(input("Ingrese su número de teléfono: "))
    diccionarioUsuario = registroUsuario(nombre, edad, direccion, telefono)
    print(diccionarioUsuario)
    print(f"{diccionarioUsuario['nombre']} tiene {diccionarioUsuario['edad']} años, vive en {diccionarioUsuario['direccion']} y su número de teléfono es {diccionarioUsuario['telefono']}")
if __name__ == "__main__":
    main()