"""3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
    1. Ejemplos:
    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`"""

my_list = [
    4, 
    3, 
    6, 
    1, 
    7
]

#Way using pop and Insert
final = my_list.pop(len(my_list)-1)
inicio = my_list.pop(0)
my_list.insert(0, final)
my_list.insert(len(my_list), inicio)

for index in my_list:
    print(index)