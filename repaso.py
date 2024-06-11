
# 3) Columnas repetidas [3 puntos]
# Implementar la función columnas_repetidas, que dada una matriz no vacía de m
# columnas (con m par y m ≥ 2) devuelve True si las primeras m/2 columnas son
# iguales que las últimas m/2 columnas. Definimos a una secuencia de secuencias
# como matriz si todos los elementos de la primera secuencia tienen la misma
# longitud.

# problema columnas_repetidas(in mat:seq<seq<Z>>) : Bool {
#     requiere: {|mat| > 0}
#     requiere: {todos los elementos de mat tienen igual longitud m, con m > 0
#     (los elementos de mat son secuencias)}
#     requiere: {todos los elementos de mat tienen longitud par (la cantidad de
#     columnas de la matriz es par)}
#     asegura: {(res = true) <=> las primeras m/2 columnas de mat son iguales a
#     las últimas m/2 columnas}
# }

# Por ejemplo, dada la matriz
# m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
# se debería devolver res = true
# TIP: para dividir un número entero x por 2 y obtener como resultado un número
# entero puede utilizarse la siguiente instrucción: int(x/2)

# 4) Rugby 4 naciones [3 puntos]
# Desde hace más de 10 años existe en el mundo del rugby un torneo que disputan
# anualmente 4 selecciones del sur global (Argentina, Australia, Nueva Zelanda y
# Sudáfrica). Este torneo se llama "The rugby championship" o comunmente "4
# naciones", ya que suplantó al viejo "3 naciones".

# Implementar la función cuenta_posiciones_por_nacion que dada la lista de
# naciones que compiten en el torneo, y el diccionario que tiene los resultados
# de los torneos anuales en el formato año:posiciones_naciones, donde año es un
# número entero y posiciones_naciones es una lista de strings con los nombres de
# las naciones, genere un diccionario de naciones:#posiciones, que para cada
# Nación devuelva la lista de cuántas veces salió en esa posición.

# Tip: para crear una lista con tantos ceros como naciones se puede utilizar la
# siguiente sintaxis lista_ceros = [0]*len(naciones)

# problema cuenta_posiciones_por_nacion(in naciones: seq<String>, in torneos:
# dict<Z,seq<String>>: dict<String,seq<Z>> {
#     requiere: {naciones no tiene elementos repetidos}
#     requiere: {Los valores del diccionario torneos son permutaciones de la
#     lista naciones (es decir, tienen exactamente los mismos elementos que
#     naciones, en cualquier orden posible)}
#     asegura: {res tiene como claves los elementos de naciones}
#     asegura: {El valor en res de una nación es una lista de |naciones|
#     elementos que indica en la posición i cuántas veces salió esa nación en la
#     i-ésima posición.}
# }
# Por ejemplo, dados
# naciones= ["arg", "aus", "nz", "sud"]
# torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
# se debería devolver res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0],
# "sud": [0,2,0,0]}

# 4) Cuántos palíndromos sufijos (2 puntos)
# Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. Se nos pide
# programar en python la siguiente función:

# problema cuantos_sufijos_son_palindromos(in texto:String) : Z{
# requiere: -
# asegura: {res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto}
# }

# Nota: un sufijo es una subsecuencia de texto que va desde una posición cualquiera hasta el final de la palabra. Ej: "Diego",
# el conjunto de sufijos es: "Diego", "iego", "ego", "go", "o". Para este ejercicio no consideramos a "" como sufijo de ningún
# texto.

# 2) Chicken Game (3 puntos)
# El juego del gallina es una competición en la que dos participantes conducen un vehículo en dirección al del contrario; si
# alguno se desvía de la trayectoria de choque pierde y es humillado por comportarse como un "gallina". Se hizo un torneo
# para ver quién es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando. Si dos jugadores 
# juegan y se chocan entre sí, entonces pierde cada uno 5 puntos por haberse dañado. Si ambos jugadores se desvían, pierde
# cada uno 10 puntos por gallinas. Si uno no se desvía y el otro sí, el gallina pierde 15 puntos por ser humillado y el ganador
# suma 10 puntos! En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se 
# desvía, o nunca lo hace. Se debe programar la función 'torneo_de_gallinas' que recibe un diccionario (donde las claves
# representan los nombres de los participantes que se anotaron en el torneo, y los valores sus respectivas estrategias) y 
# devuelve un diccionario con los puntajes obtenidos por cada jugador.

# problema torneo_de_gallinas(in estrategias: dict<String, String>) : dict<String,Z> {
# requiere: {estrategias tiene por lo menos 2 elementos(jugadores)}
# requiere: {Las claves de estrategias tienen longitud mayor a 0}
# requiere: {Los valores de estrategias sólo pueden ser los strings "me desvío siempre" ó "me la banco y no me desvío"}
# asegura: {Las claves de res y las claves de estrategias son iguales}
# asegura: {para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al
# finalizar el torneo, dado que jugó una vez contra cada otro jugador}
# }

# 3) Cuasi Ta-Te-Ti (2 puntos)
# Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su
# ficha en cada turno. Juegan intercaladamente y comienza Ana. Ana pone siempre una "X" en su turno y Beto pone una "O" en 
# el suyo. Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. SI el tablero está completo y no ganó
# nadie, entonces se declara un empate. El tablero comienza vacío, representado por " " en cada posición.
# Notar que dado que juegan por turnos y comienza Ana poniendo una "X" se cumple que la cantidad de "X" es igual a la 
# cantidad de "O" o bien la cantidad de "X" son uno más que la cantidad de "O".
# Se nos pide implementar una función en python 'problema_quien_gano_el_tateti_facilito' que determine si ganó alguno, o si
# Beto hizo trampa (puso una 'O' cuando Ana ya había ganado).

# problema quien_gano_el_tateti_facilito(in tablero: seq<seq<Char>>) : Z{
# requiere: {tablero es una matriz cuadrada}
# requiere: {5 <= |tablero[0]| <= 10]}
# requiere: {tablero sólo tiene 'X', 'O' y '' (espacio vacío) como elementos}
# requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de
# 'O'}
# asegura: {res = 1 <==> hay tres 'X' consecutivas en forma vertical (misma columna) y no hay tres 'O' consecutivas en forma
# vertical(misma columna)}
# asegura: {res = 0 <==> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical}
# asegura: {res = 3 <==> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa)}
# }