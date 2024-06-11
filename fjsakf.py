def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[(bool, bool)]:
    indice: int = 0
    indice_aux: int = 0
    mitad: int = int(len(grilla_horaria)/2)
    res_mitad_uno: list[str] = []
    res_mitad_dos: list[str] = []
    lista_bool: list[(bool, bool)] = []
    res = str

    while indice_aux < len(grilla_horaria[0]): # indice_aux me ayuda a recorrer la primer lista de grilla_horaria
        persona = grilla_horaria[0][indice_aux] # como las personas deben ser en todas las filas iguales, tomo las de la primer lista
        while indice < mitad: # como siempre |grilla_horaria| = 8, el limite de indice es 3 (no puede llegar a mitad = 4)
            if persona == grilla_horaria[indice][indice_aux]: # busco la persona en el mismo indice_aux pero en la siguiente lista
                res = True
                indice += 1
            else:
                res = False
                indice = mitad
        res_mitad_uno.append(res)
        indice_aux += 1
        indice = 0
        cantidad_iteraciones = 0
    
    indice_aux = 0
    indice = mitad
    while indice_aux < len(grilla_horaria[0]):
        persona = grilla_horaria[4][indice_aux]
        while indice < len(grilla_horaria):
            if persona == grilla_horaria[indice][indice_aux]:
                res = True
                indice +=1
            else:
                res = False
                indice = len(grilla_horaria)
        res_mitad_dos.append(res)
        indice_aux += 1
        indice = mitad
        cantidad_iteraciones = 0

    for i in range(len(res_mitad_uno)):
        if res_mitad_uno[i] and res_mitad_dos[i]:
            lista_bool.append((True, True))
        elif res_mitad_uno[i] == False and res_mitad_dos[i] == False:
            lista_bool.append((False, False))
        elif res_mitad_uno[i] and res_mitad_dos[i] == False:
            lista_bool.append((True, False))
        elif res_mitad_uno[i] == False and res_mitad_dos[i]:
            lista_bool.append((False, True))

    return lista_bool

g1 = [["ana", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"]]
print(un_responsable_por_turno(g1))
g2 = [["ana", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["ana", "res", "julio", "bool"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "pika", "kitty"]]
print(un_responsable_por_turno(g2))
g3 = [["ana", "julio", "res", "bool"],
      ["ana", "julio", "res", "bool"],
      ["ana", "res", "res", "bool"],
      ["ana", "julio", "julio", "bool"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "kitty", "pika"],
      ["luki", "po", "pika", "pika"],
      ["luki", "po", "kitty", "kitty"]]
print(un_responsable_por_turno(g3))
g4 = [["ana", "julio", "res"],
      ["ana", "julio", "res"],
      ["ana", "res", "res"],
      ["ana", "julio", "julio"], #TFF
      ["luki", "po", "kitty"],
      ["luki", "po", "kitty"],
      ["luki", "po", "pika"],
      ["luki", "po", "kitty"]] #TTF
print(un_responsable_por_turno(g4))
g5 = [["ana", "julio"],
      ["ana", "julio"],
      ["ana", "res"],
      ["ana", "julio"], #TF
      ["luki", "po"],
      ["luki", "po"],
      ["luki", "po"],
      ["luki", "po"]] #TT
print(un_responsable_por_turno(g5))
g6 = [["ana", "julio"],
      ["ana", "julio"],
      ["ana", "julio"],
      ["ana", "julio"], #TT
      ["luki", "po"],
      ["luki", "po"],
      ["luki", "po"],
      ["luki", "po"]] #TT
print(un_responsable_por_turno(g6))