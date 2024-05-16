'''
2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera. No se puede ya que la variable unicamente está definida dentro de su funcion
    2.  Intente accesar a una variable global desde una función y cambiar su valor.
'''

primer_valor = int(input("Ingrese un valor\n"))
segundo_valor = int(input("Ingrese un valor\n"))
tercer_valor = 8

def sumar_dos_numeros():
    resultado = primer_valor + segundo_valor
    return resultado


print(f"El resultado de la suma es de: " + str(sumar_dos_numeros()))

def agregar_8():
    tercer_valor = sumar_dos_numeros() + 8
    return tercer_valor


print(f"El resultado del tercer valor es de: " + str(agregar_8()))