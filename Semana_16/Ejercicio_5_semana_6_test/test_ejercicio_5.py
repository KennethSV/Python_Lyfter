from ejercicio_5_semana_6_test import calcular_mayusculas_y_minusculas
import pytest

def test_string_containing_only_uppercase():
    # Arrange
    text = "HOLA"
    # Act
    mayusculas, minusculas = calcular_mayusculas_y_minusculas(text)
    # Assert
    assert mayusculas == 4
    assert minusculas == 0

def test_string_containing_only_lowercase():
    # Arrange
    text = "hola"
    # Act
    mayusculas, minusculas = calcular_mayusculas_y_minusculas(text)
    # Assert
    assert mayusculas == 0
    assert minusculas == 4

def test_string_containing_mix_of_lowercase_and_uppercase():
    # Arrange
    text = "HOla"
    # Act
    mayusculas, minusculas = calcular_mayusculas_y_minusculas(text)
    # Assert
    assert mayusculas == 2
    assert minusculas == 2

def test_empty_string():
    # Arrange
    text = ""
    # Act
    mayusculas, minusculas = calcular_mayusculas_y_minusculas(text)
    # Assert
    assert mayusculas == 0
    assert minusculas == 0

def test_no_alphabetic_characters():
    # Arrange
    text = "@!$%^& 1234"
    # Act
    mayusculas, minusculas = calcular_mayusculas_y_minusculas(text)
    # Assert
    assert mayusculas == 0
    assert minusculas == 0

def test_special_characters_and_accented_letters():
    # Arrange
    text = "@!$%^& Esdrújula"
    # Act
    mayusculas, minusculas = calcular_mayusculas_y_minusculas(text)
    # Assert
    assert mayusculas == 1
    assert minusculas == 8

def test_string_containing_whitespace_only():
    # Arrange
    text = "    "
    # Act
    mayusculas, minusculas = calcular_mayusculas_y_minusculas(text)
    # Assert
    assert mayusculas == 0
    assert minusculas == 0

def test_long_string():
    # Arrange
    text = "A" * 500000 + "b" * 300000
    # Act
    mayusculas, minusculas = calcular_mayusculas_y_minusculas(text)
    # Assert
    assert mayusculas == 500000
    assert minusculas == 300000

def test_long_string():
    # Arrange
    text = 1234

    # Act && Assert

    with pytest.raises(TypeError):
        calcular_mayusculas_y_minusculas(text)