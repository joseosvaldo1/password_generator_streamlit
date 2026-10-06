"""Core password generation logic."""

from __future__ import annotations

import hashlib
import random
import string

MIN_PASSWORD_LENGTH = 4
MAX_PASSWORD_LENGTH = 15
SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
CHARACTER_SETS = (
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits,
    SPECIAL_CHARACTERS,
)


def _validate_inputs(length: int, key1: str, key2: str, reference: str) -> None:
    if not isinstance(length, int):
        raise ValueError("Password length must be an integer.")

    if length < MIN_PASSWORD_LENGTH or length > MAX_PASSWORD_LENGTH:
        raise ValueError(
            "Password length must be between "
            f"{MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}."
        )

    if not key1.strip() or not key2.strip() or not reference.strip():
        raise ValueError("All fields must be filled.")


def generate_password(length: int, key1: str, key2: str, reference: str) -> str:
    """Generate a deterministic password from the provided keys and reference."""
    _validate_inputs(length, key1, key2, reference)

    seed = f"{key1}{key2}{reference}".strip()
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    rng = random.Random(digest)

    password_chars: list[str] = []
    for index, chars in enumerate(CHARACTER_SETS):
        password_chars.append(chars[int(digest[index], 16) % len(chars)])

    remaining_length = length - len(password_chars)
    all_characters = "".join(CHARACTER_SETS)

    for offset in range(remaining_length):
        password_chars.append(
            all_characters[int(digest[len(password_chars) + offset], 16) % len(all_characters)]
        )

    rng.shuffle(password_chars)
    return "".join(password_chars)
