import pytest

from password_generator.generator import generate_password


@pytest.mark.parametrize(
    ("length", "key1", "key2", "reference"),
    [
        (8, "alpha", "beta", "project"),
        (12, "one", "two", "three"),
        (15, "user", "pass", "ref"),
    ],
)
def test_generate_password_returns_valid_length_and_character_types(
    length: int, key1: str, key2: str, reference: str
) -> None:
    password = generate_password(length, key1, key2, reference)

    assert len(password) == length
    assert any(char.islower() for char in password)
    assert any(char.isupper() for char in password)
    assert any(char.isdigit() for char in password)
    assert any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in password)


def test_generate_password_raises_for_invalid_length() -> None:
    with pytest.raises(ValueError):
        generate_password(3, "a", "b", "c")


def test_generate_password_raises_for_missing_fields() -> None:
    with pytest.raises(ValueError):
        generate_password(8, "", "b", "c")
