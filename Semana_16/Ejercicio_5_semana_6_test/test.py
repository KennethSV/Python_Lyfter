from ejercicio_5_semana_6_test import calcular_mayusculas_y_minusculas

def test_string_containing_only_uppercase():
    # Arrange
    text = "HOLA"
    # Act
    mayusculas, minusculas = calcular_mayusculas_y_minusculas(text)
    
    return minusculas

print(test_string_containing_only_uppercase())