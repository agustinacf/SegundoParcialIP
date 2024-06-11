# 1) Códigos filtrados [2 puntos]
# El hijo del dueño de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos 
# cuyos código de barras terminimoan en números primos son especialmente auspiciosos y deben ser destacados
# en la tienda. Luego de convencer a su padre de esta idea, solicita una función en python que facilite
# esta gestión.

# Se pide implementar una función que, dada una secuencia de enteros, cada uno representando un código 
# de barras de un producto, cree y devuelva una nueva lista que contenga únicamente aquellos números de 
# la lista original cuyos últimos tres dígitos formen un número primo (por ejemplo, 101, 002 y 011).

# Nota: un número primo es aquel que solo es divisible por si mismo y por 1. Algunos ejemplos de hasta 
# tres dígitos son 2, 3, 4, 101, 103, 107, etc.

# problema filtrar_codigos_primos(in codigos_barra: seq<Z>) : seq<Z> {
# requiere: {Todos los enteros de codigos_barra tienen, por lo menos, 3 dígitos}
# requiere: {No hay elementos repetidos en codigos_barra}
# asegura: {los últimos 3 dígitos de cada uno de los elementos de res forman un número primo}
# asegura: {Todos los elementos de codigos_barra cuyos últimos 3 dígitos forman un número primo 
# están en res}
# asegura: {Todos los elementos de res están en codigos_barra}
# }

def divisores(numero: int) -> list[int]:
    lista_divisores: list[int] = []
    numero_rango: int = numero + 1

    for i in range(1, numero_rango, 1):
        if numero % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def sacar_primer_numero(numero: int) -> int:
    numero_str: str = str(numero)
    numero_nuevo: int = ""

    if len(numero_str) > 0:
        for i in range(1, len(numero_str)):
            numero_nuevo += numero_str[i]
    return numero_nuevo

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    lista_primos: list[int] = []
    lista_divisores: list[int] = []

    for i in range(len(codigos_barra)):
        numero: int = codigos_barra[i]
        longitud_numero: int = len(str(numero))
        while longitud_numero != 3:
            numero = sacar_primer_numero(numero)
            longitud_numero: int = len(str(numero))
        numero = int(numero)
        lista_divisores = divisores(numero)
        if len(lista_divisores) == 2:
            numero: int = codigos_barra[i]
            lista_primos.append(numero)
    return lista_primos

c1 = [11111002, 214013, 849032, 38491005]
print(filtrar_codigos_primos(c1))
c2 = [101, 38435028, 4742019, 95472986]
print(filtrar_codigos_primos(c2))

#--------------------------------------------------------------------------------

# 2) Cambios de stock de stock_productos [2 puntos]

# En la veterinaria "Exacta's pets", al finalizar cada día, el personal registra en papeles los nombres y
# la cantidad actual de los productos cuyo stock ha cambiado. Para mejorar la gestión, desde la dirección
# de la veterinaria han pedido desarrollar una solución en Python que les permita analizar las
# fluctuaciones del stock.

# Se pide implementar una función que reciba una lista de tuplas, donde cada tupla contiene el nombre de 
# un producto y su stock en ese momento. La función debe procesar esta lista y devolver un diccionario 
# que tenga como clave el nombre del producto y como valor una tupla con su mínimo y máximo stock histórico
# registrado.

# problema stock_productos(in stock_cambios: seq<<String X Z>>): dict<String, <Z X Z>>{
# requiere: {Todos los elementos de stock_cambios están formados por un string no vacío y un entero >= 0}
# asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock_cambios (o sea, un
# producto)}
# asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock_cambios}
# asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor 
# cantidad de ese producto en stock_cambios y como segundo valor el mayor}
# }

def stock_productos(stock_cambios: list[(str, int)]) -> dict[str,(int, int)]:
    extremos: dict[str,(int, int)] = {}
    indice: int = 0
    indice_aux: int = 0
    
    for tuplas in stock_cambios:
        producto: str = tuplas[0]
        if producto not in extremos.keys():
            minimo: int = tuplas[1]
            maximo: int = tuplas[1]
            indice_aux = 0
            while indice_aux < len(stock_cambios):
                if stock_cambios[indice_aux][0] == producto:
                    if stock_cambios[indice_aux][1] < minimo:
                        minimo = stock_cambios[indice_aux][1]
                    elif stock_cambios[indice_aux][1] > maximo:
                        maximo = stock_cambios[indice_aux][1]
                indice_aux += 1
            extremos[producto] = (minimo, maximo)
    return extremos

sc1 = [("galletita", 12),("galletita", 10),("galletita", 1),("hueso",120),("hueso",3),("hueso",10)] #{"galletita":(1,12), "hueso":(3,120)}
print(stock_productos(sc1))
sc2 = [("pato", 12),("pato",0),("pato",13),("collar",300),("collar",20),("collar",17),("comida",100),("comida",29)]
#{"pato":(0,13), "collar":(17,300), "comida": (29,100)}
print(stock_productos(sc2))
sc3 = [("correa", 10),("comida",140),("comida",49),("shampoo",2),("shampoo",39),("shampoo",50)]
#{"corra": (10,10), "comida":(2,140), "shampoo": (2,50)}
print(stock_productos(sc3))

#--------------------------------------------------------------------------------

# 3) Matriz de responsables por turnos [2 puntos]

# Las personas responsables de los turnos están anotadas en una matriz donde las columnas representan los
# días, en orden de lunes a domingo, y cada fila a un rango de una hora. Hay cuatro filas para los turnos 
# de la mañana (9, 10, 11 y 12 hs) y otras cuatro para la tarde (14, 15, 16 y 17).

# Para hacer más eficiente el trabajo del personal de la veterinaria, se necesita analizar si quienes 
# quedan de responsables, están asignadas de manera continuada en los turnos de cada día.

# Para ello se pide desarrollar una función en Python que, dada la matriz de turnos, devuelva una lista
# de tuplas de Bool, una por cada día. Cada tupla debe contener dos elementos. El primer elemento debe ser
# True sí y solo sí todos los valores de los turnos de la mañana para ese día son iguales entre sí. El 
# segundo elemento debe ser True sí y solo sí todos los valores de los turnos de la tarde para ese día 
# son iguales entre sí. Siempre hay una persona responsable en cualquier horario de la veterinaria.

# problema un_responsable_por_turno(in grilla_horaria: seq<seq<String>>): seq<(Bool x Bool)> {
# requiere: {|grilla_horaria| = 8}
# requiere: {Todos los elementos de grilla_horaria tienen el mismo tamaño (mayor a 0 y menor a 8)}
# requiere: {No hay cadenas vacías en las listas de grilla_horaria}
# asegura: {|res| = |grilla_horaria[0]|}
# asegura: {El primer valor de la tupla en res[i], con i:Z, 0 <= i < |res| es igual a True <==> los primeros
# 4 valores de la columna i de grilla_horaria son iguales entre sí}
# asegura: {El segundo valor de la tupla en res[i], con i:Z, 0 <= i < |res| es igual a True <==> los últimos
# 4 valores de la columna i de grilla_horaria son iguales entre sí}
# }

def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[(bool, bool)]:
    indice: int = 0
    indice_aux: int = 0
    mitad: int = int(len(grilla_horaria)/2)
    res_mitad_uno: list[str] = []
    res_mitad_dos: list[str] = []
    lista_bool: list[(bool, bool)] = []
    res = str
    cantidad_iteraciones: int = 0

    while indice_aux < len(grilla_horaria[0]):
        persona = grilla_horaria[0][indice_aux]
        while indice < mitad:
            if persona == grilla_horaria[indice][indice_aux]:
                res = True
                cantidad_iteraciones += 1
                indice = cantidad_iteraciones
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
                cantidad_iteraciones += 1
                indice = mitad + cantidad_iteraciones
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
      ["ana", "julio"], #Tt
      ["luki", "po"],
      ["luki", "po"],
      ["luki", "po"],
      ["luki", "po"]] #TT
print(un_responsable_por_turno(g6))

#--------------------------------------------------------------------------------

# 4) Subsecuencia más larga [2 puntos]

# Con el objetivo de organizar el flujo de pacientes, en la veterinaria se anotan los tipos de mascotas
# que van ingresando al local. Se necesita identificar las consultas que involucran solo a perros y gatos.
# Por eso, se decide desarrollar una función en Python que encuentre la secuencia más larga de consultas
# consecutivas que solo contenga los tipos de mascota "perro" o "gato".

# Se pide implementar una función que, dada una secuencia de Strings, que representan los tipos de animales
# atendidos, devuelva el índice donde comienza la subsecuencia más larga que cumpla con estas condiciones.

# problema subsecuencia_mas_larga(in tipos_pacientes_atendidos: seq<String>): Z{
# requiere: {tipos_pacientes_atendidos tiene, por lo menos, un elemento "perro" o "gato"}
# asegura: {res es el índice donde empieza la subsecuencia más larga de tipos_pacientes_atendidos que
# contenga solo elementos "perro" o "gato"}
# asegura: {Si hay más de una subsecuencia de tamaño máximo, res tiene el índice de la primera}
# }

def primer_numero_secuencia_mas_larga(lista: list[int]) -> int:
    longitud_actual: int = 0
    max_longitud: int = 0
    primer_numero = int

    for i in range(len(lista)):
        if i + 1 < len(lista) and lista[i] + 1 == lista[i + 1]:
            if longitud_actual == 0:
                primer_numero = lista[i]
            longitud_actual += 1
        else:
            if longitud_actual > max_longitud:
                max_longitud = longitud_actual
            longitud_actual = 0
    return primer_numero

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    lista_indices: list[int] = []
    indice_res = int

    for i in range(len(tipos_pacientes_atendidos)):
        if tipos_pacientes_atendidos[i] == "perro" or tipos_pacientes_atendidos[i] == "gato":
            lista_indices.append(i)    
    print(lista_indices)
    indice_res = primer_numero_secuencia_mas_larga(lista_indices)
    return indice_res

tpa1 = ["pato","perro","gato","perro","leon","perro"]
print(subsecuencia_mas_larga(tpa1))
tpa2 = ["pato","perro","gato","perro","leon","perro","perro","gato","perro"]
print(subsecuencia_mas_larga(tpa2))
