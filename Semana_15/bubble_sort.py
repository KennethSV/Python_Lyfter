def bubble_sort(lista):
    for y in range(0, len(lista)):
        for x in range(0, len(lista)-1):
            elemento_actual = lista[x]
            siguiente_elemento = lista[x+1]
            if elemento_actual > siguiente_elemento:
                lista[x] = siguiente_elemento
                lista[x+1] = elemento_actual
    return lista
        
lista = [10,90,30,5,85,70,41,23,98,56,25,0,54,25,87,98]
print(bubble_sort(lista))