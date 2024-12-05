from login_utilities import try_login
import pytest

def test_try_login_with_correct_credentials_return_true():
    # Arrange
    email_input = "a@gmail.com"
    password_input = "123"
    
    # Act

    result = try_login(email_input, password_input)

    # Assert

    assert result

def test_try_login_with_incorrect_email():
    # Arrange
    email_input = "b@gmail.com"
    password_input = "123"
    
    # Act & Assert
    with pytest.raises(ValueError):
        try_login(email_input, password_input)