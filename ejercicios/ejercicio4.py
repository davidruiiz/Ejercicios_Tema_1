
def cola_tareas(tareas):
    # Ordenamos la lista de tareas por prioridad (el segundo elemento de cada tupla)
    tareas.sort(key=lambda x: x[1])

    # Creamos una cola vacía para almacenar las tareas
    cola_tareas = []

    # Añadimos las tareas a la cola, pero sin el número de orden
    for tarea in tareas:
        cola_tareas.append(tarea[0])

    # Retornamos la cola de tareas
    return cola_tareas


if __name__=="__main__":
    tareas = [("Tarea 1", 2), ("Tarea 2", 1), ("Tarea 3", 3), ("Tarea 4", 1)]

    cola = cola_tareas(tareas)

    print(cola)
    