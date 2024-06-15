# 1) Atención por guardia (1 punto)
# Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la información que maneja
# sobre los pacientes y el personal de salud. En primer lugar debemos resolver en qué orden se deben atender los pacientes
# que llegan a la guardia. En enfermería, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y
# otra postergable (esto se llama hacer triage). A partir de dichas colas que contienen la identificación del paciente, se pide
# devolver una nueva cola según la siguiente especificación.

# problema orden_de_atencion (in urgentes: cola <Z>, in postergables: cola <Z>): cola <Z> {
# requiere: {no hay elementos repetidos en urgentes}
# requiere: {no hay elementos repetidos en postergables}
# resquiere: {la intersección entre postergables y urgentes es vacía}
# requiere: {|postergables| = |urgentes|}
# asegura: {no hay repetidos en res}
# asegura: {res es permutación de la concatenación de urgentes y postergables}
# asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
# asegura: {En res no hay dos seguidos de urgentes}
# asegura: {En res no hay dos seguidos de postergables}
# asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1
# aparece antes que c2 en res}
# asegura: {Para todo c1 y c2 de tipó "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables
# entonces c1 aparece antes que c2 en res}
# }

from queue import Queue as Cola

def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    urgentes_copia: Cola[int] = Cola() # hago una copia de la cola de urgentes
    urgentes_aux: Cola[int] = Cola() # se puede hacer con una sola copia de la cola original pero me quiero asegurar
    postergables_copia: Cola[int] = Cola() # hago una copia de la cola de postergables
    postergables_aux: Cola[int] = Cola() # hago una copia de postergables
    cola_ordenada: Cola[int] = Cola() # se puede hacer con una sola copia de la cola original pero me quiero asegurar

    while not urgentes.empty(): # saco los elementos de urgentes para meterlos a las otras dos colas auxiliares
        paciente: int = urgentes.get()
        urgentes_copia.put(paciente)
        urgentes_aux.put(paciente)
    
    while not postergables.empty(): # saco los elementos de postergables para meterlos a las otras dos colas auxiliares
        paciente: int = postergables.get()
        postergables_copia.put(paciente)
        urgentes_aux.put(paciente)

    while not urgentes_aux.empty(): # restauro los elementos de urgentes
        paciente = urgentes_aux.get()
        urgentes.put(paciente)

    while not postergables_aux.empty(): # restauro los elementos de postergables
        paciente = postergables_aux.get()
        postergables.put(paciente)

    while not urgentes_copia.empty() and not postergables_copia.empty(): # ahora debo meter los elementos de urgentes y postergables al res
        urgente: int = urgentes_copia.get()
        cola_ordenada.put(urgente) # primero pongo un elemento de urgentes
        postergable: int = postergables_copia.get()
        cola_ordenada.put(postergable) # luego pongo un elemento de postergables
    
    return cola_ordenada.queue # para el resultado no sé si va cola_ordenada o cola_ordenada.queue, pero con .queue se pueden ver los elementos

urgentes = Cola()
urgentes.put(1)
urgentes.put(2)
urgentes.put(3)
print(urgentes.queue)
postergables = Cola()
postergables.put(4)
postergables.put(5)
postergables.put(6)
print(postergables.queue)
print(orden_de_atencion(urgentes, postergables))

#--------------------------------------------------------------------------------

# 2) Alarma epidemiológica (3 puntos)
# Necesitamos detectar la aparición de posibles epidemias. Para esto contamos con una lista de enfermedades infecciosas y
# los registros de atención por guardia dados por una lista de expedientes. Cada expediente es una tupla con ID paciente y
# enfermedad que motivó la atención. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su
# valor es la proporción de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo 
# aquellas enfermedades infecciosas cuya proporción supere cierto umbral.

# problema alarma_epidemiologica(registros: seq<ZxString>, infecciosas: seq<String>, umbral: R): dict<String,R>{
# requiere: {0 < umbral < 1}
# asegura: {claves de res pertenecen a infecciosas}
# asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
# enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje}
# asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
# enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res}
# }

def alarma_epidemiologica(registros: list[(int, str)], infecciosas: list[str], umbral: float) -> dict[str, float]:
    res: dict[str, float] = {}
    enf_totales: int = len(registros) # necesito este numero para calcular el porcentaje

    for enfermedad in infecciosas: # recorro la lista de registros
        atendidos_enfermedad: int = 0
        porcentaje: float = 0.0
        for i in range(len(registros)):
            if registros[i][1] == enfermedad: # veo si el segundo elemento de la tupla coincide con la enfermedad
                atendidos_enfermedad += 1 # si coinciden, sumo 1 al contador atendidos_enfermedad
        porcentaje = (atendidos_enfermedad/(enf_totales)) # calculo el porcentaje de la enfermedad
        if porcentaje > umbral:
            if enfermedad not in res:
                res[enfermedad] = porcentaje # si el porcentaje supera al umbral, lo agrego al diccionario del resultado
    return res

registros = [(111,"sifilis"),(222,"sifilis"),(333,"neumonia"),(444,"sifilis"),(555,"neumonia"),(666,"lolero")]
infecciosas = ["sifilis", "neumonia", "lolero"]
umbral = 0.3
print(alarma_epidemiologica(registros, infecciosas, umbral))
registros1 = [(111,"sifilis"),(222,"sifilis"),(333,"sifilis"),(444,"lolero"),(555,"gripe"),(666,"gripe"),(777,"neumonia"),(888,"neumonia"),(999,"gripe")]
infecciosas1 = ["sifilis", "neumonia", "lolero"]
umbral1 = 0.3
print(alarma_epidemiologica(registros1, infecciosas1, umbral1))

#--------------------------------------------------------------------------------

# 3) Empleados del mes (2 puntos)
# Dado un diccionaio con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es
# una lista de las horas trabajadas por día, queremos saber quienes trabajaron más para darles un premio. Se deberá buscar
# la o las claves para la cual se tiene el máximo valor de cantidad total de horas, y devolverlas en una lista.

# problema empleados_del_mes(horas: dicc<Z,seq<Z>>): seq<Z> {
# requiere: {No hay valores en horas que sean listas vacías}
# asegura: {Si ID pertenece a res entonces ID pertenece a las claves de horas}
# asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos
# los otros IDs}
# asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los
# otros IDs, entonces ID pertenece a res}
# }

def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    indice: int = 0
    cantidad_horas: int = 0
    suma_horas: dict[int, int] = {} # hago un diccionario paralelo para poner el trabajador y el total de horas trabajadas
    mismo_max: list[(int,int)] = []
    tupla_max: list[(int,int)] = []
    lista_max: list[int] = []

    for empleado in horas.items(): # recorro las claves e indices del diccionario horas
        cantidad_horas = 0
        indice = 0
        while indice < len(empleado[1]): # empleado[1] se refiere a la lista de horas trabajadas
            cantidad_horas += empleado[1][indice] # sumo cada hora al contador cantidad_horas
            suma_horas[empleado[0]] = cantidad_horas # voy actualizando la cantidad de horas trabajadas del empleado en suma_horas
            indice += 1
    
    max_horas: int = 0 # introduzco la variable max_horas
    for empleado in suma_horas.items(): # recorro las claves e indices de suma_horas
        if empleado[1] > max_horas: # empleado[1] se refiere a la cantidad de horas totales
            max_horas = empleado [1] 
            max_trabajador = empleado[0] # empleado[0] se refiere al trabajador en si
        elif empleado[1] == max_horas:
            mismo_max.append((empleado[0],empleado[1])) # si hay dos empleados con el mismo maximo, los sumo a una lista de mismo_max
    tupla_max.append((max_trabajador,max_horas)) # sumo a otra lista la tupla del trabajador con la mayor cantidad de horas trabajadas 
    lista_max.append(max_trabajador) # sumo a lista_max el ID del trabajador final con la mayor cantidad de horas

    for i in range(len(mismo_max)): # recorro la lista de mismo_max
        if mismo_max[i][1] == tupla_max[0][1]: # comparo el segundo elemento de cada tupla de mismo_max con el segundo elemento de tupla_max
            if mismo_max[i][0] not in lista_max: # evito repeticiones
                lista_max.append(mismo_max[i][0]) 
    
    return lista_max

h1 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6]}
print(empleados_del_mes(h1)) #["333"]
h2 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6], "444": [4,5,6]}
print(empleados_del_mes(h2)) #["333","444"]
h3 = {"111": [1, 2, 3], "444": [6,7,8], "222": [2, 3, 4], "333": [4,5,6]}
print(empleados_del_mes(h3)) #["444"]
h4 = {"111": [1, 2, 3], "444": [6,7,8], "222": [8,9,10], "333": [4,5,6], "444": [8,9,10], "555": [6,7,8]}
print(empleados_del_mes(h4)) #["222","444"] o ["444","222"] (en los asegura no se habla del orden)

#--------------------------------------------------------------------------------

# 4) Nivel de ocupacion del hospital
# Queremos saber qué porcentaje de ocupación de camas hay en el hospital. El hospital se representa por una matriz en
# donde las filas son los pisos, y las columnas son las camas. Los valores de la matriz son booleanos que indican si la cama
# está ocupada o no. Si el valor es verdadero (True) indica que la cama está ocupada. Se nos pide programar en python una
# función que devuelve una secuencia de enteros, indicando la proporción de camas ocupadas en cada piso.

# problema nivel_de_ocupacion(camas_por_piso: seq<Seq<Bool>>): seq<R> {
# requiere: {Todos los pisos tienen la misma cantidad de camas}
# requiere: {Hay por lo menos 1 piso en el hospital}
# requiere: {Hay por lo menos una cama por piso}
# asegura: {|res| = |camas|}
# asegura: {Para todo 0 <= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido del total
# de camas del piso i}
# }

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    lista_porcentajes: list[float] = []
    camas_totales_fila: int = len(camas_por_piso[0]) # como todos los pisos tienen la misma cantidad de camas, da igual el indice elegido

    for filas in range(len(camas_por_piso)): # recorro camas_por_piso
        camas_ocupadas_fila: int = 0
        for columna in camas_por_piso[filas]: # la columna representa cada cama
            if columna == True:
                camas_ocupadas_fila += 1
        lista_porcentajes.append((camas_ocupadas_fila/camas_totales_fila)*100) # el porcentaje se puede hacer sin el *100
    return lista_porcentajes

cp1 = [[True, True, False],
       [False, True, True]]
print(nivel_de_ocupacion(cp1))
cp2 = [[True, True, False, True],
       [False, True, True, True],
       [False, False, False, True]]
print(nivel_de_ocupacion(cp2))
cp3 = [[True, True, False, True],
       [False, True, True, True],
       [False, False, False, True],
       [False, False, False, False]]
print(nivel_de_ocupacion(cp3))

#--------------------------------------------------------------------------------

# 5) Preguntas teóricas (2 puntos)

# Conteste marcando la opción correcta.

# A) ¿Qué es una variable con 'scope local' en Python? (0.75 puntos)
# ○ Una variable definida fuera de cualquier función y accesible en todo el programa.
# ● Una variable definida dentro de una función, que solo puede ser utilizada dentro de esa función.
# ○ Una variable que puede ser utilizada en cualquier módulo importado.

# B) ¿Qué es una estructura de control en Python? (0.75 puntos)
# ○ Una herramienta que permite la ejecución condicional y repetitiva de bloques de código.
# ● Un tipo esencial de variable que almacena datos complejos.
# ○ Una librería utilizada para manipular archivos en el sistema operativo.

# C) ¿Qué representa un nodo en un Control Flow Graph? (0.5 puntos)
# ○ Una variable utilizada en el programa.
# ● Una condición lógica o una instrucción en el código.
# ○ Un archivo de datos externo.