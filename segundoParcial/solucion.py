"""
Nota: 8.87 / 10.0 (APROBADO)

puntaje ej1: 1
puntaje ej2: 2
puntaje ej3: 2
puntaje ej4: 1.87
puntaje ej5: 0.75
puntaje ej6: 0.75
puntaje ej7: 0.5

Enunciado
Parcial Python - Tema 2

Un grupo de amigos apasionados por las salas de escape, esas aventuras inmersivas donde tienen 60 minutos para salir de una habitación resolviendo enigmas, llevan un 
registro meticuloso de todas las salas de escape que hay en Capital. Este registro indica si han visitado una sala y si pudieron o no salir de ella. Un 0 significa 
que no fueron, un 61 que no lograron salir a tiempo, y un número entre 1 y 60 representa los minutos que les tomó escapar exitosamente. Con estos datos, pueden comparar 
sus logros y desafíos en cada nueva aventura que emprenden juntos.

1) Escape de sala más veloz [1 punto]
Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital, escribir una función en Python que devuelva la posición 
(índice) en la cual se encuentra el tiempo más rápido, excluyendo las salas en las que no haya salido (0 o mayor a 60).

problema tiempo_mas_rapido (in tiempos_salas: seq⟨Z⟩): Z {
  requiere: {Hay por lo menos un elemento en tiempos_salas entre 1 y 60 inclusive}
  requiere: {Todos los tiempos en tiempos_salas están entre 0 y 61 inclusive}
  asegura: {res es la posición de la sala en tiempos_salas de la que más rápido se salió (en caso que haya más de una, devolver la primera, osea la de menor índice)}
}

2) Velocidad de cada amigo [2 puntos]
Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) registrados para cada sala de escape en Capital, escribir 
una función en Python que devuelva un diccionario. En este nuevo diccionario, las claves deben ser los nombres de los amigos y los valores deben ser tuplas que indiquen la 
cantidad de salas de las que cada persona logró salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir)

problema promedio_de_salidas (in registro: dict⟨String, seq⟨Z⟩⟩) : dict⟨String, ⟨Z x R⟩⟩ {
  requiere: {registro tiene por lo menos un integrante}
  requiere: {Todos los integrantes de registro tiene por lo menos un tiempo}
  requiere: {Todos los valores de registro tiene la misma longitud}
  requiere: {Todos los tiempos de los valores de registro están entre 0 y 61 inclusive}
  asegura: {res tiene las mismas claves que registro}
  asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores 
            de registro}
  asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que salió es mayor a 0: es el promedio de salas con tiempo mayor 
            estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino es 0.0}
}

3) Escape en solitario [2 puntos]
Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los tiempos (en minutos) registrados para cada 
sala (0 si no fueron, 61 si no salieron, y un número entre 1 y 60 si salieron), escribir una función en Python que devuelva los índices de todas las filas (que representan 
las salas) en las cuales el primer, segundo y cuarto amigo no fueron (0), pero el tercero sí fue (independientemente de si salió o no).

problema escape_en_solitario (in amigos_por_salas: seq⟨seq⟨Z⟩⟩): seq⟨Z⟩ {
  requiere: {Hay por lo menos una sala en amigos_por_salas}
  requiere: {Hay 4 amigos en amigos_por_salas}
  requiere: {Todos los tiempos en cada sala de amigos_por_salas están entre 0 y 61 inclusive}
  asegura: {La longitud de res es menor igual que la longitud de amigos_por_salas}
  asegura: {Por cada sala en amigos_por_salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de 0, la posición de dicha sala en amigos_por_salas 
            debe aparecer res}
  asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos_por_salas[i] es 0, y el tercer valor es distinto de 0}
}

4) Subsecuencia más larga de salidas [3 puntos]
Dada una lista con los tiempos (en minutos) registrados para cada sala de escape a la que fue una persona, escribir una función en Python que devuelva una tupla con el índice 
de inicio y el índice de fin de la subsecuencia más larga de salidas exitosas de salas de escape consecutivas.

problema racha_mas_larga (in tiempos: seq⟨Z⟩): ⟨Z x Z⟩ {
  requiere: {Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive}
  requiere: {Todos los tiempos en tiempos están entre 0 y 61 inclusive}
  asegura: {En la primera posición de res está la posición (índice de la lista) de la sala que inicia la racha más larga}
  asegura: {En la segunda posición de res está la posición (índice de la lista) de la sala que finaliza la racha más larga}
  asegura: {El elemento de la primer posición de res en tiempos es mayor estricto 0 y menor estricto que 61}
  asegura: {El elemento de la segunda posición de res en tiempos es mayor estricto 0 y menor estricto que 61}
  asegura: {La primera posición de res es menor o igual a la segunda posición de res }
  asegura: {No hay valores iguales a 0 o a 61 en tiempos entre la primer posición de res y la segunda posición de res}
  asegura: {No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que está entre la primer posición de res y la segunda posición de res}
  asegura: {Si hay dos o más subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera de ellas.}
}

5) Preguntas teóricas (2 puntos)

Conteste marcando la opción correcta.

A) ¿Qué hace la sentencia 'break' en un ciclo en Python? (0.75 punto)
 ○ Reinicia el ciclo desde el principio.
 ● Termina el ciclo inmediatamente.
 ○ Salta la siguiente iteración del ciclo.

B) ¿Cuál es el propósito de la sentencia 'else' en una estructura 'if' en Python? (0.75 punto)
 ○ Definir una variable local.
 ● Ejecutar un bloque de código si todas las condiciones anteriores son falsas.
 ○ Iniciar un ciclo 'while'.

C) ¿Qué diferencia hay entre coverage de sentencias y coverage de branches? (0.5 punto)
 ● Coverage de sentencias verifica cada línea de código, mientras que coverage de branches verifica las posibles salidas de las decisiones lógicas.
 ○ Coverage de branches verifica cada línea de código, mientras que coverage de sentencias verifica las posibles salidas de las decisiones lógicas.
 ○ No hay diferencia, ambos se refieren al mismo concepto.

"""

# 1)
def tiempo_mas_rapido (tiempos_salas: list[int])-> int:
    indice_minimo: int = 0
    tiempo_minimo: int = 999

    for i in range(len(tiempos_salas)):
        numero: int = tiempos_salas[i]
        if 0 < numero < 61:
            if tiempos_salas[i] < tiempo_minimo:
                indice_minimo = i
                tiempo_minimo = tiempos_salas[i]
    return indice_minimo

# print(tiempo_mas_rapido([12,14,90,45,10])) #4
# print(tiempo_mas_rapido([12,10,90,45,10])) #1
# print(tiempo_mas_rapido([0,61,7,12,54,23])) #2
# print(tiempo_mas_rapido([0,0,60,61])) #2
# print(tiempo_mas_rapido([1,23,34,1,1,1,0,61])) #0
# print(tiempo_mas_rapido([0,0,61,0,61,12,2])) #6

# 2)
def promedio_de_salidas (registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res: dict[str, tuple[int, float]] = {}

    for amigo in registro.items():
        cant_escapes: int = 0
        tiempo_total: int = 0
        tiempo_promedio = int
        for i in range(len(amigo[1])):
            tiempo: int = amigo[1][i]
            if 0 < tiempo < 61:
                tiempo_total += tiempo
                cant_escapes += 1
        if cant_escapes != 0:
            tiempo_promedio = float(tiempo_total/cant_escapes)
        else: 
            tiempo_promedio = float(0)
        if amigo[0] not in res.keys():
            res[amigo[0]] = (cant_escapes,tiempo_promedio)
    return res

# r1 = {"agus": [0,21,3,61], "leo": [34,0,12,61]} #{"agus":(2,12.0), "leo":(2,23.0)}
# print(promedio_de_salidas(r1))
# r2 = {"agus": [0,21,3,61], "leo": [61,0,61,61]} #{"agus":(2,12.0), "leo":(0,0.0)}
# print(promedio_de_salidas(r2))
# r3 = {"agus": [0,61,13,12,45,34,12,61], "leo": [35,46,21,31,21,23,25,38,], "ale": [61,61,61,61,61,61,61,61]}
# #{"agus":(5,23.2), "leo":(8,30.0), "ale":(0,0.0)}
# print(promedio_de_salidas(r3))
# r4 = {"agus": [58,58,58,0,61,58], "leo": [0,0,0,0,61,54], "ale": [14,13,0,61,10,12]}
# #{"agus":(4,58), "leo":(1,54), "ale":(4,12.25)}
# print(promedio_de_salidas(r4))

# 3)
def escape_en_solitario (amigos_por_salas: list[list[int]])-> list[int]:
    lista_res: list[int] = []

    for i in range(len(amigos_por_salas)):
        numero: int = amigos_por_salas[i][2]
        if 1 <= numero <= 61:
            if amigos_por_salas[i][0] == 0 and amigos_por_salas[i][1] == 0 and amigos_por_salas[i][3] == 0:
                lista_res.append(i)
    return lista_res

# aps1 = [[0,0,1,4],
#         [0,0,21,0]]
# print(escape_en_solitario(aps1)) #[1]
# aps2 = [[0,0,1,0],
#         [0,0,21,0],
#         [1,2,54,1],
#         [0,0,5,1]]
# print(escape_en_solitario(aps2)) #[0,1]
# aps3 = [[0,0,61,61],
#         [12,32,0,0],
#         [35,21,26,21]]
# print(escape_en_solitario(aps3)) #[]
# aps4 = [[0,0,0,0],
#         [0,0,61,0],
#         [0,0,21,0],
#         [0,0,0,0]]
# print(escape_en_solitario(aps4)) #[1,2]
# aps5 = [[0,0,34,0],
#         [0,0,61,0],
#         [0,0,21,0],
#         [0,0,54,0]]
# print(escape_en_solitario(aps5)) #[0,1,2,3]

# 4)
# acá el error me dio cuando tengo una lista de longitud = 1, en ese caso creo que se arreglaría
# agregando un if en el que, si |lista| = 1, devuelva una tupla con el elemento dos veces, por
# ejemplo, si la lista es [2], debería devolver (2,2)
def indices_inicio_fin(lista: list[int]) -> tuple[int, int]:
    longitud_maxima: int = 0
    longitud_actual: int = 0
    indice_max: int = 0
    indice_min: int = 0
    indice_min_actual = int

    for i in range(len(lista)):
        if i + 1 < len(lista) and lista[i] + 1 == lista[i + 1]:
            if longitud_actual == 0:
                indice_min = lista[i]
            longitud_actual += 1
            if longitud_actual > longitud_maxima:
                longitud_maxima = longitud_actual
                indice_min_actual = indice_min
                indice_max = lista[i] + 1
        else:
            longitud_actual = 0
    return (indice_min_actual, indice_max)

def racha_mas_larga (tiempos: list[int])-> tuple[int, int] :
    indices_salida: list[int] = []

    for i in range(len(tiempos)):
        minutos: int = tiempos[i]
        if 0 < minutos < 61:
            indices_salida.append(i)
    return(indices_inicio_fin(indices_salida))

# t1 = [0,12,0,45,12,25,38,0,1,2,4] #(3,6)
# print(racha_mas_larga(t1))
# t2 = [0,0,61,5,6,7,21,0,61,1,2,3] #(3,6)
# print(racha_mas_larga(t2))
# t3 = [1,2,3,4,0,61,12,13,5,3,1,2,54,0] #(6,12)
# print(racha_mas_larga(t3))
# t4 = [1,2,3,4,0,1,2,3,4] #(0,3)
# print(racha_mas_larga(t4))
# t5 = [0,0,61,12,12,0] #(3,4)
# print(racha_mas_larga(t5))