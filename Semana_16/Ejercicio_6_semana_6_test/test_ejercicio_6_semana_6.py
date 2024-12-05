from Ejercicio_6_semana_6_test import ordenar_texto_por_item
import pytest

def test_unsorted_string():
    # Arrange
        unsorted = "Computer-Laptop-Manga-Comic-Anime"
        expected = "Anime-Comic-Computer-Laptop-Manga"
    # Act
        sorted = ordenar_texto_por_item(unsorted)
    # Assert
        assert expected == sorted

def test_already_sorted_string():
    # Arrange
        unsorted = "Anime-Comic-Computer-Laptop-Manga-Snake"
        expected = "Anime-Comic-Computer-Laptop-Manga-Snake"
    # Act
        sorted = ordenar_texto_por_item(unsorted)
    # Assert
        assert expected == sorted

def test_single_item_in_string():
    # Arrange
        unsorted = "Anime"
        expected = "Anime"
    # Act
        sorted = ordenar_texto_por_item(unsorted)
    # Assert
        assert expected == sorted

def test_empty_string():
    # Arrange
        unsorted = ""
        expected = ""
    # Act
        sorted = ordenar_texto_por_item(unsorted)
    # Assert
        assert expected == sorted

def test_sort_with_special_characters_including_spaces_and_numbers_string():
    # Arrange
        unsorted = "@rriba-Abajo -D3r echa-1zqu!3rda"
        expected = "1zqu!3rda-@rriba-Abajo -D3r echa"
    # Act
        sorted = ordenar_texto_por_item(unsorted)
    # Assert
        assert expected == sorted

def test_case_sensitive_string():
    # Arrange
        unsorted = "computer-Laptop-Manga-Comic-Anime-iPad"
        expected = "Anime-Comic-computer-iPad-Laptop-Manga"
    # Act
        sorted = ordenar_texto_por_item(unsorted)
    # Assert
        assert expected == sorted

def test_duplicate_items_inside_string():
    # Arrange
        unsorted = "computer-computer-Laptop-Manga-Comic-Anime-iPad"
        expected = "Anime-Comic-computer-computer-iPad-Laptop-Manga"
    # Act
        sorted = ordenar_texto_por_item(unsorted)
    # Assert
        assert expected == sorted

def test_numbers_as_strings():
    # Arrange
        unsorted = "95-68-52-12-1-7-102"
        expected = "1-7-12-52-68-95-102"
    # Act
        sorted = ordenar_texto_por_item(unsorted)
    # Assert
        assert expected == sorted

def test_given_value_is_string():
    # Arrange
        unsorted = 1
        
    # Act && Assert
        with pytest.raises(TypeError):
            ordenar_texto_por_item(unsorted)