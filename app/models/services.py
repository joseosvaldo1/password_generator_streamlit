"""Service layer for password generation and validation."""

from __future__ import annotations

from dataclasses import dataclass

from app.models.domain import (
    PasswordRequest,
    PasswordStrength,
    evaluate_password_strength,
    generate_password,
)


@dataclass(frozen=True)
class PasswordServiceResult:
    """Service result returned after generation."""

    password: str
    strength: PasswordStrength


class PasswordService:
    """Coordinates generation and strength evaluation."""

    def generate(self, request: PasswordRequest) -> PasswordServiceResult:
        """Generate a password and evaluate its strength."""
        password = generate_password(request)
        strength = evaluate_password_strength(password)
        return PasswordServiceResult(password=password, strength=strength)
