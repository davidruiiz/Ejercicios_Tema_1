
def agregar_una_vez(lista,el):

    # Si el elemento no está en la lista, lo agrega.
    if el not in lista:
            lista.append(el)
    # Si el elemento está en la lista, lanza un error.
    else:
        raise ValueError ('Error: Imposible añadir elementos duplicados => [elemento].')

    # Devuelve la lista con el elemento añadido.
    return lista

# Ejecución del código principal.
if __name__ == '__main__':
    lista = [1, 2, 3]
    print(agregar_una_vez(lista, 4))
    print(agregar_una_vez(lista, 4))
    