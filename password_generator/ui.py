"""Graphical user interface for the password generator."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

try:
    import pyperclip
except ImportError:  # pragma: no cover - handled at runtime for the GUI app.
    pyperclip = None

from .generator import MAX_PASSWORD_LENGTH, MIN_PASSWORD_LENGTH, generate_password


class PasswordGeneratorApp:
    """Encapsulates the GUI and application behavior."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("320x440")
        self.root.resizable(False, False)

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.title_label = tk.Label(
            self.root, text="Password Generator", font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        self.length_label = tk.Label(self.root, text=f"Password Length ({MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH}):")
        self.length_label.pack(pady=5)
        self.entry_length = tk.Entry(self.root)
        self.entry_length.pack()

        self.key1_label = tk.Label(self.root, text="Key 1:")
        self.key1_label.pack(pady=5)
        self.entry_key1 = tk.Entry(self.root)
        self.entry_key1.pack()

        self.key2_label = tk.Label(self.root, text="Key 2:")
        self.key2_label.pack(pady=5)
        self.entry_key2 = tk.Entry(self.root)
        self.entry_key2.pack()

        self.reference_label = tk.Label(self.root, text="Reference:")
        self.reference_label.pack(pady=5)
        self.entry_reference = tk.Entry(self.root)
        self.entry_reference.pack()

        self.generate_button = tk.Button(
            self.root,
            text="Generate Password",
            command=self.generate_password,
            width=20,
            bg="#4CAF50",
            fg="white",
        )
        self.generate_button.pack(pady=10)

        self.copy_button = tk.Button(
            self.root,
            text="Copy Password",
            command=self.copy_password,
            width=20,
            bg="#2196F3",
            fg="white",
        )
        self.copy_button.pack(pady=5)

        self.clear_button = tk.Button(
            self.root,
            text="Clear Fields",
            command=self.clear_fields,
            width=20,
            bg="#FF5722",
            fg="white",
        )
        self.clear_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def generate_password(self) -> None:
        try:
            length = int(self.entry_length.get())
        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid number for the password length.",
            )
            return

        try:
            password = generate_password(
                length,
                self.entry_key1.get(),
                self.entry_key2.get(),
                self.entry_reference.get(),
            )
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))
            return

        self.result_label.config(text=f"Password: {password}")

    def copy_password(self) -> None:
        if not self.result_label.cget("text").startswith("Password: "):
            messagebox.showwarning("No Password", "No password to copy!")
            return

        if pyperclip is None:
            messagebox.showwarning(
                "Clipboard unavailable",
                "Install pyperclip to enable copying to the clipboard.",
            )
            return

        password = self.result_label.cget("text").split(": ", maxsplit=1)[1]
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    def clear_fields(self) -> None:
        self.entry_length.delete(0, tk.END)
        self.entry_key1.delete(0, tk.END)
        self.entry_key2.delete(0, tk.END)
        self.entry_reference.delete(0, tk.END)
        self.result_label.config(text="")

    def run(self) -> None:
        self.root.mainloop()


def build_interface() -> None:
    """Create and run the application window."""
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    app.run()
