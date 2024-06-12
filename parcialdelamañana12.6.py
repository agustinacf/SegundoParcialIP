# 1) Atención por guardia
from queue import Queue as Cola

def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    urgentes_copia: Cola[int] = Cola()
    urgentes_aux: Cola[int] = Cola()
    postergables_copia: Cola[int] = Cola()
    postergables_aux: Cola[int] = Cola()
    cola_ordenada: Cola[int] = Cola()
    indice: int = 0

    while not urgentes.empty():
        paciente: int = urgentes.get()
        urgentes_copia.put(paciente)
        urgentes_aux.put(paciente)
    
    while not postergables.empty():
        paciente: int = postergables.get()
        postergables_copia.put(paciente)
        urgentes_aux.put(paciente)

    while not urgentes_aux.empty():
        paciente = urgentes_aux.get()
        urgentes.put(paciente)

    while not postergables_aux.empty():
        paciente = postergables_aux.get()
        postergables.put(paciente)

    while not urgentes_copia.empty() and not postergables_copia.empty():
        urgente: int = urgentes_copia.get()
        cola_ordenada.put(urgente)
        postergable: int = postergables_copia.get()
        cola_ordenada.put(postergable)
    
    return cola_ordenada.queue

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

# 2) Alarma epidemiológica
def alarma_epidemiologica(registros: list[(int, str)], infecciosas: list[str], umbral: float) -> dict[str, float]:
    res: dict[str, float] = {}
    enf_totales: int = len(registros)

    for enfermedad in infecciosas:
        atendidos_enfermedad: int = 0
        porcentaje: float = 0.0
        for i in range(len(registros)):
            if registros[i][1] == enfermedad:
                atendidos_enfermedad += 1
        porcentaje = (atendidos_enfermedad/(enf_totales))
        if porcentaje > umbral:
            if enfermedad not in res:
                res[enfermedad] = porcentaje
    return res

registros = [(111,"sifilis"),(222,"sifilis"),(333,"kpoper"),(444,"sifilis"),(555,"kpoper"),(666,"lolero")]
infecciosas = ["sifilis", "kpoper", "lolero"]
umbral = 0.3
print(alarma_epidemiologica(registros, infecciosas, umbral))

# 3)
def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    indice: int = 0
    cantidad_horas: int = 0
    suma_horas: dict[int, int] = {}
    mismo_max: list[(int,int)] = []
    tupla_max: list[(int,int)] = []
    lista_max: list[int] = []

    for empleado in horas.items():
        cantidad_horas = 0
        indice = 0
        while indice < len(empleado[1]):
            cantidad_horas += empleado[1][indice]
            suma_horas[empleado[0]] = cantidad_horas
            indice += 1
    
    max_horas: int = 0
    for empleado in suma_horas.items():
        if empleado[1] > max_horas:
            max_horas = empleado [1]
            max_trabajador = empleado[0]
        elif empleado[1] == max_horas:
            mismo_max.append((empleado[0],empleado[1]))
    tupla_max.append((max_trabajador,max_horas))
    lista_max.append(max_trabajador)

    for i in range(len(mismo_max)):
        if mismo_max[i][1] == tupla_max[0][1]:
            if mismo_max[i][0] not in lista_max:
                lista_max.append(mismo_max[i][0])
    
    return lista_max

h1 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6]}
print(empleados_del_mes(h1)) #["333"]
h2 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6], "444": [4,5,6]}
print(empleados_del_mes(h2)) #["333","444"]
h3 = {"111": [1, 2, 3], "444": [6,7,8], "222": [2, 3, 4], "333": [4,5,6]}
print(empleados_del_mes(h3)) #["444"]

# 4) Nivel de ocupacion del hospital
def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    lista_porcentajes: list[float] = []
    camas_totales_fila: int = len(camas_por_piso[0])

    for filas in range(len(camas_por_piso)):
        camas_ocupadas_fila: int = 0
        for columna in camas_por_piso[filas]:
            if columna == True:
                camas_ocupadas_fila += 1
        lista_porcentajes.append((camas_ocupadas_fila/camas_totales_fila)*100)
    return lista_porcentajes

cp1 = [[True, True, False],
       [False, True, True]]
print(nivel_de_ocupacion(cp1))
cp2 = [[True, True, False, True],
       [False, True, True, True],
       [False, False, False, True]]
print(nivel_de_ocupacion(cp2))
