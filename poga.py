def valores_extremos(cotizaciones_diarias: dict[str, list[(int, float)]]) -> dict[str,(float, float)]:
    minimo_maximo: dict = {}
    indice_cot: int = 0
    indice_tupla: int = 0

    for empresa in cotizaciones_diarias.keys():
        if empresa not in minimo_maximo.keys():
            minimo_maximo[empresa] = ()

    for empresa in cotizaciones_diarias.keys():
        while indice_cot < len(cotizaciones_diarias[empresa]):
            min_cot: int = cotizaciones_diarias[empresa][indice_tupla][1]
            max_cot: int = cotizaciones_diarias[empresa][indice_tupla][1]
            while indice_tupla < len(cotizaciones_diarias[empresa]):
                if cotizaciones_diarias[empresa][indice_tupla][1] < min_cot:
                    min_cot = cotizaciones_diarias[empresa][indice_tupla][1]
                indice_tupla += 1
            indice_cot += 1
            indice_tupla = 0
            while indice_tupla < len(cotizaciones_diarias[empresa]):
                if cotizaciones_diarias[empresa][indice_tupla][1] > max_cot:
                    max_cot = cotizaciones_diarias[empresa][indice_tupla][1]
                indice_tupla += 1
                minimo_maximo[empresa] = (min_cot,max_cot)
            indice_cot += 1
            indice_tupla = 0
        indice_cot = 0
        indice_tupla = 0
            
    return minimo_maximo

cotizaciones_diarias = {"YPF" : [(1,10),(15, 3),(31,100)], "ALUA" : [(1,0), (20, 50),(31,30)]} #{"YPF":(3,100), "ALUA": (0, 50)}
print(valores_extremos(cotizaciones_diarias))
cotizaciones_diarias2 = {"YPF" : [(1,10),(15, 3),(31,100)], "ALUA" : [(1,0), (20, 50),(31,30)], "MELI" : [(1,40), (5,10),(27, 9)]}
#{"YPF": (3,100), "ALUA": (0, 50), "MELI": (9,40)}
print(valores_extremos(cotizaciones_diarias2))