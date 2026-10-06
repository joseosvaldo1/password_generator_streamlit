"""Domain layer for the password generator."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Final

from password_generator.generator import (
    MAX_PASSWORD_LENGTH,
    MIN_PASSWORD_LENGTH,
    generate_password as generate_password_by_keys,
)


class PasswordStrength(str, Enum):
    """Password strength evaluation categories."""

    WEAK = "weak"
    MEDIUM = "medium"
    STRONG = "strong"


@dataclass(frozen=True)
class PasswordRequest:
    """Request data used to generate a password."""

    length: int
    key1: str
    key2: str
    reference: str

    def __post_init__(self) -> None:
        if not isinstance(self.length, int):
            raise TypeError("Password length must be an integer.")

        if not MIN_PASSWORD_LENGTH <= self.length <= MAX_PASSWORD_LENGTH:
            raise ValueError(
                "Password length must be between "
                f"{MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}."
            )

        if not self.key1.strip() or not self.key2.strip() or not self.reference.strip():
            raise ValueError("All fields must be filled.")


def generate_password(request: PasswordRequest) -> str:
    """Generate a password using the existing password logic."""
    return generate_password_by_keys(
        request.length,
        request.key1,
        request.key2,
        request.reference,
    )


def evaluate_password_strength(password: str) -> PasswordStrength:
    """Estimate the password strength based on entropy and diversity."""
    if not isinstance(password, str):
        raise TypeError("The password must be a string.")

    if not password:
        return PasswordStrength.WEAK

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    charset_size = 0
    if has_uppercase:
        charset_size += 26
    if has_lowercase:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_symbol:
        charset_size += 32

    if charset_size == 0:
        return PasswordStrength.WEAK

    diversity_score = sum((has_uppercase, has_lowercase, has_digit, has_symbol))
    entropy_bits = len(password) * math.log2(charset_size)

    if len(password) >= 9 and diversity_score >= 3 and entropy_bits >= 55:
        return PasswordStrength.STRONG

    if len(password) >= 8 and diversity_score >= 2 and entropy_bits >= 40:
        return PasswordStrength.MEDIUM

    return PasswordStrength.WEAK
