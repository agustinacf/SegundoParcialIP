def quien_gano_el_tateti_facilito(tablero: list[str]) -> int:
    indice: int = 0
    indice_aux: int = 0
    indices_x: list[int] = []
    indices_o: list[int] = []
    res_x = bool
    res_o = bool

    while indice < len(tablero):
        for i in range(len(tablero[0])):
            if tablero[indice][i] == "X":
                indices_x.append(i)
            elif tablero[indice][i] == "O":
                indices_o.append(i)
        indice += 1
    
    iguales_x: int = 0
    indice_mayor: int = len(indices_x) - 1
    indice_menor: int = indice_mayor - 1
    while indice_mayor >= 0:
        if indices_x[indice_mayor] == indices_x[indice_menor]:
            res_x = True
            iguales_x += 1
            indice_mayor -= 1
        else:
            indice_mayor -= 1

    iguales_o: int = 0
    indice_mayor: int = len(indices_o) - 1
    indice_menor: int = indice_mayor - 1
    while indice_mayor >= 0:
        if indices_o[indice_mayor] == indices_o[indice_menor]:
            res_o = True
            iguales_o += 1
            indice_mayor -= 1
        else:
            indice_mayor -= 1
    
    if iguales_x >= 3:
        res_x = True
    res_x = False

    if iguales_o >= 3:
        res_o = True
    res_o = False

    if res_x and not res_o:
        return 1
    
    if not res_x and not res_o:
        return 2
    
    if res_x and res_o:
        return 3

t1 = [["X","","O","",""],["X","O","","",""],["X","","","","O"]] #1
print(quien_gano_el_tateti_facilito(t1))