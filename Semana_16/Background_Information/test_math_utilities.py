from main_utilities import sum_list_items

def test_sum_all_items():
    # AAA

    # Arrange (variables/inputs de la prueba)
    list_input = [3,4,5,6,7,8,9]
    # Act
    result = sum_list_items(list_input)
    # Assert
    assert result == 42

    
