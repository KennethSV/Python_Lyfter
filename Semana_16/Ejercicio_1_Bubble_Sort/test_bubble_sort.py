from Bubble_sort import bubble_sort
import pytest
from random import randint

def test_verify_if_works_with_small_list():
    # Arrange
    small_list = [2]

    # Act
    result = bubble_sort(small_list)
    sorted_list = sorted(small_list)
    
    # Assert
    assert result == sorted_list

def test_verify_if_works_with_more_100_elements():
    # Arrange
    big_list = []
    
    for x in range(0, randint(101,200)):
        big_list.append(randint(0,10000))

    # Act
    result = bubble_sort(big_list)
    sorted_list = sorted(big_list)

    # Assert
    assert result == sorted_list

def test_verify_if_works_with_empty_list():
    # Arrange
    empty_list = []

    # Act
    result = bubble_sort(empty_list)
    sorted_list = sorted(empty_list)
    
    # Assert
    assert result == sorted_list

def test_verify_if_works_without_parameters_from_a_list():
    # Arrange

    failed_list = 1

    # Act and Assert

    with pytest.raises(TypeError):
        bubble_sort(failed_list)