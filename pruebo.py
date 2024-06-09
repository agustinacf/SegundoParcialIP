def columnas_repetidas(mat: list[list[int]]) -> bool:
    longitud: int = len(mat[0])
    mitad_de_longitud: int = int(longitud/2)
    indice: int = 0
    primer_indice: int = 0
    segundo_indice: int = mitad_de_longitud
    lista_primera_mitad: list[int] = []
    lista_segunda_mitad: list[int] = []

    while indice < len(mat):
        for i in range(primer_indice, mitad_de_longitud):
            lista_primera_mitad.append(i)
        for i in range(mitad_de_longitud, len(mat)):
            lista_segunda_mitad.append(i)
    
    print(lista_primera_mitad)
    print(lista_segunda_mitad)

    for i in range(len(lista_primera_mitad)):
        if i in lista_segunda_mitad:
            return True
        return False
    
m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
print(columnas_repetidas(m))