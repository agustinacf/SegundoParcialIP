# 1) Fila en ExactaBank (1 puntos)
# En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son representados por
# las tuplas (nombre, tipo afiliado) donde la pimera componente es el nombre y el tipo afiliado puede ser "comun" o "vip".
# Se nos pide implementar una función en python que dada una cola de clientes del banco, devuelva una nueva cola con los
# mismos clientes pero en donde los clientes vip están primero que los clientes comunes manteniendo el orden original de los 
# clientes vips y los comunes entre sí.

# problema reordenar_cola_priorizando_vips(in filaClientes: Cola<String x String>): Cola <String> {
# requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0}
# requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son "comun" o "vip"}
# requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre sí}
# asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes}
# asegura: {|res| = |filaCliente|}
# asegura: {res no tiene elementos repetidos}
# asegura: {No hay ningun cliente "comun" antes que un "vip" en res}
# asegura: {Para todo cliente c1 y cliente c2 de tipo "comun" perteneceientes a filaClientes si c1 aparece antes que c2 en
# filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res}
# asegura: {Para todo cliente c1 y cliente c2 de tipo "vip" perteneceintes a filaClientes si c1 aparece antes que c2 en filaClientes
# entonces el nombre de c1 aparece antes que el nombre de c2 en res}
# }

from queue import Queue as Cola

def reordenar_cola_priorizando_vips(filaClientes: Cola[str, str]) -> Cola[str]:
    cola_copiada: Cola = Cola()
    cola_copiada_aux: Cola = Cola()
    clientes_vip: Cola = Cola()
    clientes_comunes: Cola = Cola()
    clientes_ordenados: Cola = Cola()

    while not filaClientes.empty():
        elem = filaClientes.get()
        cola_copiada.put(elem)
        cola_copiada_aux.put(elem)
    
    while not cola_copiada.empty():
        cliente = cola_copiada.get()
        if cliente[1] == "vip":
            clientes_vip.put(cliente) # agrego en una cola a los clientes vip
        elif cliente[1] == "comun":
            clientes_comunes.put(cliente) # en otra cola distinta agrego a los clientes comunes
    
    while not cola_copiada_aux.empty():
        cliente = cola_copiada_aux.get()
        filaClientes.put(cliente) # restauro los elementos en la cola original

    while not clientes_vip.empty():
        cliente = clientes_vip.get()
        clientes_ordenados.put(cliente) # en la lista ordenada pongo primero los clientes vips
    
    while not clientes_comunes.empty():
        cliente = clientes_comunes.get()
        clientes_ordenados.put(cliente) # luego agrego a los clientes comunes
    
    return clientes_ordenados

filaClientes: Cola = Cola()
filaClientes.put(("juan", "vip")) #1
filaClientes.put(("ana", "vip")) #2
filaClientes.put(("seba", "comun")) #5
filaClientes.put(("rodo", "vip")) #3
filaClientes.put(("aejo", "comun")) #6
filaClientes.put(("leo", "comun")) #7
filaClientes.put(("bale", "vip")) #4
print(filaClientes.queue)
print(reordenar_cola_priorizando_vips(filaClientes))
print(filaClientes.queue)

#--------------------------------------------------------------------------------

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

def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    puntajes: dict[str, int] = {}

    for jugador in estrategias.items(): # busco la clave y valor de cada jugador en el diccionario estrategias
        puntajes[jugador[0]] = 0 # agrego el primer elemento de jugador(el jugador en si) en el diccionario de puntajes, con un puntaje = 0
        for contrincante in estrategias.items(): # vuelvo a buscar jugadores en estrategias, pero en este caso los llamo contrincantes
            if jugador != contrincante: # debo asegurarme que no tome el mismo jugador dos veces
                if jugador[1] == contrincante[1] and jugador[1] == "me la banco y no me desvío":
                    puntajes[jugador[0]] -= 5
                elif jugador[1] == contrincante[1] and jugador[1] == "me desvío siempre":
                    puntajes[jugador[0]] -= 10
                elif jugador[1] != contrincante[1] and jugador[1] == "me la banco y no me desvío":
                    puntajes[jugador[0]] += 10
                elif jugador[1] != contrincante[1] and jugador[1] == "me desvío siempre":
                    puntajes[jugador[0]] -= 15
    return puntajes

e1 = {"leo": "me desvío siempre", "rodo": "me la banco y no me desvío"}
# leo = -15
# rodo = 10
print(torneo_de_gallinas(e1))
e2 = {"leo": "me desvío siempre", "rodo": "me la banco y no me desvío", "bale": "me desvío siempre"}
# leo = -25
# rodo = 20
# bale = -25
print(torneo_de_gallinas(e2))
e3 = {"leo": "me desvío siempre", "rodo": "me la banco y no me desvío", "bale": "me desvío siempre", "nico": "me la banco y no me desvío"}
# leo = -40
# rodo = 15
# bale = -40
# nico = 15
print(torneo_de_gallinas(e3))
e4 = {"leo": "me desvío siempre", "rodo": "me la banco y no me desvío", "bale": "me desvío siempre", "nico": "me la banco y no me desvío", "ale": "me la banco y no me desvío"}
# leo = -55 
# rodo = 10
# bale = -55
# nico = 10
# ale = 10
print(torneo_de_gallinas(e4))

#--------------------------------------------------------------------------------

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

            
def quien_gano_el_tateti_facilito(tablero: list[str]) -> int:
    indice: int = 0

    while indice 



t1 = [["X","","O","",""],["X","O","","",""],["X","","","","O"]] #1
print(quien_gano_el_tateti_facilito(t1))






#--------------------------------------------------------------------------------

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

def es_palindromo(palabra: str) -> bool: # hago una funcion auxiliar que me indique si una palabra es palindromo o no
    for i in range(len(palabra)):
        if palabra[i] == palabra[len(palabra) - i - 1]:
            return True
        return False

def quitar_primera_letra(palabra: str) -> str: # hago una funcion auxiliar que quite la primer letra de un string, formando sufijos
    palabra_nueva: str = ""

    if len(palabra) > 0:
        for i in range(1, len(palabra)):
            palabra_nueva += palabra[i]
    return palabra_nueva

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    contador_sufijos: int = 0
    letras_palabras: int = len(texto)
    palabra: str = texto

    while letras_palabras != 0:
        if es_palindromo(palabra):
            contador_sufijos += 1
            palabra = quitar_primera_letra(palabra)
            letras_palabras -= 1
        else:
            palabra = quitar_primera_letra(palabra)
            letras_palabras -= 1
    return contador_sufijos

print(cuantos_sufijos_son_palindromos("diego"))
print(cuantos_sufijos_son_palindromos("asgus"))
print(cuantos_sufijos_son_palindromos("hannah"))
print(cuantos_sufijos_son_palindromos("anana"))

#--------------------------------------------------------------------------------

# 5) Preguntas teóricas (2 puntos)

# Conteste marcando la opción correcta.

# A) ¿Cuál es la función de un ciclo en Python? (0.75 puntos)
# ○ Ejecutar un conjunto de instrucciones una sola vez.
# ● Ejecutar repetidamente un conjunto de instrucciones hasta que una condición se evalúe como falsa.
# ○ Definir una constante que no puede ser cambiada.

# B) ¿Qué es una variable en Python? (0.75 puntos)
# ○ Una función que devuelve valores aleatorios.
# ● Un contenedor para almacenar datos que puede cambiar durante la ejecución del programa.
# ○ Un tipo de dato que solo puede contener números enteros.

# C) ¿Cuál es la finalidad de un Control Flow Graph en testing? (0.5 puntos)
# ○ Identificar todas las posibles salidas de un programa.
# ● Visualizar todos los posibles caminos de ejecución para asegurar la cobertura completa del código.
# ○ eterminar los puntos de entrada y salida del programa.