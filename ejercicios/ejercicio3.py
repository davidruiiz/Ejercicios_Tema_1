
def elementos_repetidos(lista_1, lista_2):
    # Creamos un conjunto vacío para almacenar los elementos repetidos
    repetidos = set()

    # Creamos una lista vacía para almacenar los elementos que aparecen en ambas listas
    resultado = []

    # Iteramos sobre los elementos de la lista 1
    for elemento in lista_1:
        # Si el elemento está en la lista 2 y no está en la lista de resultados, lo añadimos a la lista de resultados
        if elemento in lista_2 and elemento not in resultado:
            resultado.append(elemento)
            # Añadimos el elemento al conjunto de elementos repetidos
            repetidos.add(elemento)

    # Iteramos sobre los elementos de la lista 2
    for elemento in lista_2:
        # Si el elemento está en la lista 1 y no está en la lista de resultados, lo añadimos a la lista de resultados
        if elemento in lista_1 and elemento not in resultado:
            resultado.append(elemento)
            # Si el elemento ya estaba en el conjunto de elementos repetidos, lo eliminamos de la lista de resultados
            if elemento in repetidos:
                resultado.remove(elemento)

    # Retornamos la lista de resultados
    return resultado



if __name__=="__main__":
    lista_1 = ["h", 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
    lista_2 = ["h", 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a']

    resultado = elementos_repetidos(lista_1, lista_2)

    print(resultado)