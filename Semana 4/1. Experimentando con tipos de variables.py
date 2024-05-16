'''
Por ejemplo:
    1. string + string → ?
        Experimentando con tipos de datos
        Hola + Hola = HolaHola
    2. string + int → ?
        Experimentando con tipos de datos
        2 + 2 = 4
    3. int + string → ?
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
    4. list + list → ?
        Experimentando con tipos de datos
        ['mundo', 17, '45.7', 'manzana'] + ['mundo', 17, '45.7', 'manzana'] = ['mundo', 17, '45.7', 'manzana', 'mundo', 17, '45.7', 'manzana']
    5. string + list → ?
        TypeError: can only concatenate str (not "list") to str
    6. float + int → ?
        Experimentando con tipos de datos
        2 + 18.21 = 20.21
    7. bool + bool → ?
        True + True = 2
        True + False = 1
'''
v_string = 'Hola'
v_int = 2
v_list = ['mundo', 17, '45.7', 'manzana']
v_float = 18.21

print('Experimentando con tipos de datos')
print(f"True + False =", True + False)