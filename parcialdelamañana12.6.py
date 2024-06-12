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
#def alarma_epidemiologica(registros: list[(int, str)], infecciosas: list[str], umbral: float) -> dict[str, float]:

# 3)
def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    empleados_maximos: list[int] = []
    indice: int = 0
    horas_maximas: int = 0
    cantidad_horas: int = 0

    for empleado in horas.values():
        for empleado[1] in range(len(empleado[1])):
            while indice < len(empleado[1]):
                cantidad_horas += empleado[1][indice]
                if cantidad_horas > horas_maximas:
                    horas_maximas = cantidad_horas
                indice += 1
            cantidad_horas = 0
            indice = 0
    empleados_maximos.append(empleado)
    return empleados_maximos

h1 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6]}
print(empleados_del_mes(h1))