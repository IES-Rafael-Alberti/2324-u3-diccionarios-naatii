def totalCreditos(diccionario:dict)->int:
    """Función que devuelve el total de creditos de un diccionario donde la clave es la asignatura y el valor el credito que ofrece dicha asignatura.

    Args:
        diccionario (dict): diccionario donde la clave es la asignatura y el valor el credito

    Returns:
        int: el total de creditos del curso.
    """
    return sum(diccionario.values())
def crearCurso(cursos:dict,nombre:str, creditos:int)->dict:
    """Crea un diccionario donde la clave es la asignatura y el valor el credito que ofrece dicha asignatura.

    Args:
        nombre (str): nombre de la asignatura.
        creditos (int): los créditos que ofrece la asignatura.

    Returns:
        dict: el diccionario donde la clave es la asignatura y el valor el credito
    """
    cursos[nombre] = creditos
    return cursos
def main():
    """Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
    """
    asignaturas = 0
    curso = {}
    while asignaturas < 4:
        nombre = input("Ingrese el nombre del curso: ")
        creditos = int(input("Ingrese los créditos del curso: "))
        crearCurso(curso, nombre, creditos)
        asignaturas += 1
    print("-"*100)
    for nombre, creditos in curso.items():
        print(f"{nombre} tiene {creditos} créditos")
    print(f"total de creditos del curso: {totalCreditos(curso)}")
    
if __name__ == "__main__":
    main()