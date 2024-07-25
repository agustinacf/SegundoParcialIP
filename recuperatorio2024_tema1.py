"""

1) Gestión de notas de estudiantes [2 puntos]
En una escuela llamada "Academia Futura", se desea desarrollar un programa para gestionar las notas de los 
estudiantes por materia. El programa debe procesar una lista de tuplas donde cada tupla contiene el nombre de un estudiante, el nombre de una materia 
y la nota final obtenida por el estudiante en esa materia.

Se pide implementar una función en python, que respete la siguiente especificación:

problema gestion_notas (in notas_estudiante_materia: seq⟨(String x String x Z)) : dict⟨String, seq⟨(String x Z)⟩⟩ {
  requiere: { Las primeras componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
  requiere: { Las segundas componentes de notas_estudiante_materia tienen longitud mayor estricto a cero}
  requiere: { Las terceras componentes de notas_estudiante_materia están entre 1 y 10, ambos inclusive }
  requiere: { No hay 2 tuplas en notas_estudiante_materia que tengan la primera y segunda componente iguales (mismo estudiante y misma materia) }
  asegura: {res tiene como claves solo los primeros elementos de las tuplas de notas_estudiante_materia (o sea, un estudiante)}
  asegura: {El valor en res de un estudiante es una lista de tuplas donde cada tupla contiene como primera componente el nombre de la materia y como 
            segunda componente la nota obtenida por el estudiante en esa materia según notas_estudiante_materia}
  asegura: { Para toda clave (estudiante) en res, en su valor (lista de tuplas) no hay 2 tuplas que tengan la misma primera componente (materia) }
}

2) Cantidad dígitos pares [2 puntos]
Se pide implementar una función en Python llamada cantidad_digitos_pares que respete la siguiente especificación:

problema cantidad_digitos_pares (in numeros: seq⟨Z⟩) : Z {
  requiere:{Todos los elementos de numeros son mayores iguales a 0}
  asegura: {res es la cantidad total de digitos pares que aparecen en cada uno de los elementos de numeros}
}
Por ejemplo, si la lista de números es [5434, 42, 811, 3139], entonces el resultado esperado sería 5 (los dígitos pares son 4, 4, 4, 2, y 8).

3) Priorizar cola de paquetes [2 puntos]
En una empresa de logística, se manejan paquetes que llegan a una bodega y deben ser procesados para su posterior distribución. Cada paquete está 
representado por una tupla (id_paquete, peso), donde id_paquete es un identificador único del paquete y peso representa el peso del paquete en kilogramos.

Se pide implementar una función en Python llamada reordenar_cola_primero_pesados que respete la siguiente especificación:

problema reordenar_cola_primero_pesados(in paquetes: Cola⟨(String x Z)⟩, in umbral:Z): Cola⟨(String x Z)⟩{
  requiere: {no hay repetidos en las primeras componentes (Ids) de paquetes}
  requiere: {todos las segundas componentes (pesos) de paquetes son mayores estricto a cero}
  requiere: {umbral es mayor o igual a cero}
  asegura: {los elementos de res son exactamente los mismos que los elementos de paquetes}
  asegura: {|res| = |paquetes|}
  asegura: {no hay un elemento en res, cuyo peso sea menor o igual que el umbral, que aparezca primero que otro elemento en res cuyo peso sea mayor que 
            el umbral)}
  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son menores o iguales que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en 
            paquetes entonces p1 aparece primero que p2 en res}
  asegura: {Para todo paquete p1 y paquete p2 cuyos pesos son mayores que el umbral y pertenecen a paquetes si p1 aparece primero que p2 en paquetes entonces 
            p1 aparece primero que p2 en res}
}

4) Matriz pseudo ordenada [2 puntos]
Se desea verificar si una matriz está pseudo ordenada por columnas. Esto es que el mínimo de cada columna sea menor estricto que el mínimo de la columna siguiente

Para ello se pide desarrollar una función en Python que implemente esta idea respetando la siguiente especificación:

matriz_pseudo_ordenada (in matriz: seq⟨seq⟨Z⟩⟩): Bool {
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {todos los elementos de matriz tienen la misma longitud}
  asegura: {res es igual a True <=> para todo 0<=i<|matriz[0]|-1, el mínimo de la columna i de matriz < el mínimo de la columna i + 1 de matriz }
}

5) Preguntas teóricas (2 puntos)
Conteste marcando la opción correcta.

A) ¿Cuál es el principal objetivo del testing de caja blanca? (0.75 punto)
 ○ Evaluar la funcionalidad del software desde la perspectiva del usuario final.
 ○ Verificar la lógica interna del código, estructuras de control, condiciones y flujo de datos.
 ○ Garantizar que la interfaz de usuario sea intuitiva y fácil de usar.
B) ¿Qué es un "alcance" (scope) en Python? (0.5 punto)
 ○ El contexto en el cual una variable es accesible.
 ○ El número de variables definidas en un programa.
 ○ El número de funciones definidas en un programa.
C) ¿Cuál es la principal diferencia entre una lista y una tupla en Python? (0.75 punto)
 ● Las listas permiten agregar y eliminar elementos después de su creación, mientras que las tuplas no.
 ○ Las listas se ordenan automáticamente, mientras que las tuplas mantienen el orden de inserción.
 ○ Las listas pueden contener elementos duplicados y las tuplas no.

"""
from queue import Queue as Cola

# 1)
def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    res: dict[str, list[tuple[str,int]]] = {}

    for tupla in notas_estudiante_materia: # veo cada tupla de la lista
        estudiante: str = tupla[0]
        if estudiante not in res.keys(): # agrego el estudiante al diccionario del res, evitando repeticiones
            res[estudiante] = []
    
    for tupla in notas_estudiante_materia:
        estudiante: str = tupla[0]
        materia_y_nota: tuple[str, int] = (tupla[1], tupla[2])
        res[estudiante].append(materia_y_nota) # agrego al diccionario cada tupla

    return res

n1 = [('Juan', 'Geografía', 5),('Ana', 'Matemática', 9),('Lucas', 'Lengua y Literatura', 6),('Ana', 'Lengua y Literatura', 4),('Juan', 'Matemática', 5)]
print(gestion_notas(n1))
n2 = [('Juan', 'Matemática', 5),('Juan', 'Lengua y Literatura', 6),('Juan', 'Computación', 9),('Juan', 'Arte', 9)]
print(gestion_notas(n2))
n3 = [("Pedro", "Geografía", 1), ("Lucía", "Historia", 10)]
print(gestion_notas(n3))

# 2)
def digitos_pares_por_numero(numero: int) -> int:
    cantidad_pares: int = 0

    num_string: str = str(numero) # como los int no son iterables, transformo el numero en un string
    for digito in num_string:
        dig_int: int = int(digito) # transformo el digito en un int para poder operar con el
        if dig_int % 2 == 0:
            cantidad_pares += 1
    return cantidad_pares

def cantidad_digitos_pares(numeros: list[int]) -> int:
    pares_totales: int = 0

    for numero in numeros:
        pares_totales += digitos_pares_por_numero(numero) # sumo a los pares totales la cantidad_pares de la funcion digitos_pares_por_numero
    return pares_totales

num1 = [5434, 42, 811, 3139] #5
print(cantidad_digitos_pares(num1))
num2 = [] #0
print(cantidad_digitos_pares(num2))
num3 = [421] #2
print(cantidad_digitos_pares(num3))
num4 = [5434, 42, 811, 3139, 1] #5
print(cantidad_digitos_pares(num4))
num5 = [111, 333, 555] #0
print(cantidad_digitos_pares(num5))
num6 = [2468, 284, 82] #9
print(cantidad_digitos_pares(num6))
num7 = [0, 20, 103] #4
print(cantidad_digitos_pares(num7))

# 3)
def reordenar_cola_primero_pesados(paquetes: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    paquetes_copia: Cola = Cola() # creo una cola para poner los elementos de paquetes
    debajo_umbral: Cola = Cola() # a esta cola van los paquetes que no superen el umbral
    cola_res: Cola = Cola() # esta es la cola final

    while not paquetes.empty(): # paso los elementos de paquetes a los de paquetes_copia
        paquete = paquetes.get()
        paquetes_copia.put(paquete)

    while not paquetes_copia.empty(): 
        paquete = paquetes_copia.get()
        paquetes.put(paquete) # voy restaurando paquetes
        if paquete[1] > umbral:
            cola_res.put(paquete) # si el paquete es mayor estricto al umbral, lo pongo en la cola del resultado
        else:
            debajo_umbral.put(paquete) # si es menor o igual al umbral, lo pongo en la cola debajo_umbral
    
    while not debajo_umbral.empty(): # pongo los elementos de debajo_umbral en el resultado, asi quedan ordenados
        paquete = debajo_umbral.get()
        cola_res.put(paquete)
    
    return cola_res.queue

c1: Cola[tuple[str,int]] = Cola()
c1.put(('A', 40))
c1.put(('B', 10))
c1.put(('C', 39))
c1.put(('D', 41))
print(reordenar_cola_primero_pesados(c1,39)) #([('A', 40), ('D', 41), ('B', 10), ('C', 39)])
c2 = Cola()
c2.put(("P1", 3))
c2.put(("P2", 2))
c2.put(("P3", 1))
print(reordenar_cola_primero_pesados(c2,5)) #[("P1", 3), ("P2", 2), ("P3", 1)]
c3 = Cola()
c3.put(("P1", 5))
c3.put(("P2", 10))
c3.put(("P3", 3))
print(reordenar_cola_primero_pesados(c3,0)) #[('P1', 5), ('P2', 10), ('P3', 3)]
c4 = Cola()
c4.put(("P1", 5))
c4.put(("P2", 5))
c4.put(("P3", 10))
print(reordenar_cola_primero_pesados(c4,5)) #[("P3", 10), ("P1", 5), ("P2", 5)]

# 4)
def minimo(columna: list[int]) -> int:
    minimo: int = columna[0]

    for numero in columna:
        if numero < minimo:
            minimo = numero
    return minimo

def crear_columna(matriz: list[list[int]], indice: int) -> list[int]:
    indice_interno: int = 0
    columna: list[int] = []

    while indice_interno < len(matriz):
        numero = matriz[indice_interno][indice]
        if numero != 0:
            columna.append(numero)
    return columna

def matriz_pseudo_ordenada(matriz: list[list[int]]) -> bool:
    for i in range(len(matriz)):
        