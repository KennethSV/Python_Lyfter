from Ejercicio_3_semana_6 import sumador_de_listas
import pytest
from random import randint

def test_verify_if_works_with_small_list():
    # Arrange
    small_list = [2]

    # Act
    result = sumador_de_listas(small_list)
    sum_list = sum(small_list)

    # Assert
    assert result == sum_list

def test_verify_if_works_with_more_100_elements():
    # Arrange
    big_list = []
    
    for x in range(0, randint(101,200)):
        big_list.append(randint(0,10000))

    # Act
    result = sumador_de_listas(big_list)
    sum_list = sum(big_list)

    # Assert
    assert result == sum_list

def test_verify_if_works_with_empty_list():
    # Arrange
    empty_list = []

    # Act
    result = sumador_de_listas(empty_list)
    sum_list = sum(empty_list)
    
    # Assert
    assert result == sum_list

def test_verify_if_works_without_parameters_from_a_list():
    # Arrange

    failed_list = 1

    # Act and Assert

    with pytest.raises(TypeError):
        sumador_de_listas(failed_list)

def test_verify_if_works_with_values_other_than_integers():
    # Arrange

    failed_list = ['a','b','c','d']

    # Act and Assert

    with pytest.raises(ValueError):
        sumador_de_listas(failed_list)