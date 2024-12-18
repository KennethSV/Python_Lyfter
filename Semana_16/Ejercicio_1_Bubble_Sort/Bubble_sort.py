def bubble_sort(lista):
    if not isinstance(lista, list):
        raise TypeError("Input must be a list")
    else:
        for y in range(0, len(lista)):
            for x in range(0, len(lista)-1):
                elemento_actual = lista[x]
                siguiente_elemento = lista[x+1]
                if elemento_actual > siguiente_elemento:
                    lista[x] = siguiente_elemento
                    lista[x+1] = elemento_actual
        return lista