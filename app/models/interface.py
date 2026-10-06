"""Streamlit interface for the password generator."""

from __future__ import annotations

import math

import streamlit as st

from app.models.domain import (
    MAX_PASSWORD_LENGTH,
    MIN_PASSWORD_LENGTH,
    PasswordRequest,
    PasswordStrength,
    evaluate_password_strength,
)
from app.models.services import PasswordService


def estimate_break_time(password: str) -> str:
    """Estimate the time required to crack a password offline."""
    if not password:
        return "Less than 1 second"

    charset_size = 94
    entropy_bits = len(password) * math.log2(charset_size)
    guesses_per_second = 10**10
    seconds_to_crack = (2**entropy_bits) / guesses_per_second

    if seconds_to_crack < 1:
        return "Less than 1 second"
    if seconds_to_crack < 60:
        return f"{seconds_to_crack:.1f} seconds"
    if seconds_to_crack < 3600:
        return f"{seconds_to_crack / 60:.1f} minutes"
    if seconds_to_crack < 86400:
        return f"{seconds_to_crack / 3600:.1f} hours"
    if seconds_to_crack < 31536000:
        return f"{seconds_to_crack / 86400:.1f} days"
    return f"{seconds_to_crack / 31536000:.1f} years"


def build_interface() -> None:
    """Render the password generator form and results."""
    st.set_page_config(page_title="Password Generator", page_icon="🔐")
    st.title("Password Generator")
    st.caption("Generate a secure password using the same logic as the original app.")

    with st.form("password_form"):
        length = st.slider(
            "Password length",
            min_value=MIN_PASSWORD_LENGTH,
            max_value=MAX_PASSWORD_LENGTH,
            value=12,
            step=1,
        )
        key1 = st.text_input("Key 1")
        key2 = st.text_input("Key 2")
        reference = st.text_input("Reference")
        submitted = st.form_submit_button("Generate password")

    if not submitted:
        return

    try:
        request = PasswordRequest(
            length=length,
            key1=key1,
            key2=key2,
            reference=reference,
        )
        result = PasswordService().generate(request)
    except ValueError as exc:
        st.error(str(exc))
        return

    st.success("Password generated successfully!")
    st.code(result.password, language="text")

    strength = evaluate_password_strength(result.password)
    st.subheader("Password analysis")
    col1, col2 = st.columns(2)
    col1.metric("Strength", strength.value.title())
    col2.metric("Estimated time to crack", estimate_break_time(result.password))

    score = 25 if strength == PasswordStrength.WEAK else 50 if strength == PasswordStrength.MEDIUM else 100
    st.progress(score)
    st.caption(f"Strength score: {score}/100")
