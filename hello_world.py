#!/usr/bin/env python3
"""Hello World application with multiple greeting functions.

SCRUM-1221: Python hello world app with additional functions.
"""

import datetime
import random
import sys


def hello_world():
    """Print a basic hello world message."""
    print("Hello, World!")


def hello_name(name):
    """Greet a specific person by name.

    Args:
        name: The name of the person to greet.
    """
    print(f"Hello, {name}!")


def hello_uppercase():
    """Print hello world in uppercase."""
    print("HELLO, WORLD!")


def hello_lowercase():
    """Print hello world in lowercase."""
    print("hello, world!")


def hello_reverse():
    """Print hello world reversed."""
    message = "Hello, World!"
    print(message[::-1])


def hello_repeat(times=3):
    """Print hello world multiple times.

    Args:
        times: Number of times to print the greeting (default 3).
    """
    for i in range(times):
        print(f"({i + 1}) Hello, World!")


def hello_with_timestamp():
    """Print hello world with the current timestamp."""
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    print(f"[{now.isoformat()}] Hello, World!")


def hello_random_language():
    """Print hello world in a random language."""
    greetings = {
        "English": "Hello, World!",
        "Spanish": "¡Hola, Mundo!",
        "French": "Bonjour, le Monde!",
        "German": "Hallo, Welt!",
        "Italian": "Ciao, Mondo!",
        "Portuguese": "Olá, Mundo!",
        "Japanese": "こんにちは、世界！",
        "Chinese": "你好，世界！",
        "Korean": "안녕하세요, 세계!",
        "Russian": "Привет, мир!",
        "Arabic": "!مرحبا بالعالم",
        "Hindi": "नमस्ते, दुनिया!",
    }
    language = random.choice(list(greetings.keys()))
    print(f"{language}: {greetings[language]}")


def hello_ascii_art():
    """Print hello world as ASCII art."""
    art = r"""
  _   _      _ _         __        __         _     _ _
 | | | | ___| | | ___    \ \      / /__  _ __| | __| | |
 | |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |
 |  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
 |_| |_|\___|_|_|\___/      \_/\_/ \___/|_|  |_|\__,_(_)
"""
    print(art)


def hello_bordered():
    """Print hello world inside a decorative border."""
    message = "Hello, World!"
    border = "+" + "-" * (len(message) + 2) + "+"
    print(border)
    print(f"| {message} |")
    print(border)


def hello_countdown(start=3):
    """Print a countdown before saying hello world.

    Args:
        start: The number to start counting down from (default 3).
    """
    for i in range(start, 0, -1):
        print(f"{i}...")
    print("Hello, World!")


def hello_custom(greeting="Hello", target="World", punctuation="!"):
    """Print a customizable greeting.

    Args:
        greeting: The greeting word (default "Hello").
        target: Who or what to greet (default "World").
        punctuation: The punctuation to end with (default "!").
    """
    print(f"{greeting}, {target}{punctuation}")


def main():
    """Run all hello world functions as a demonstration."""
    functions = [
        ("Basic Hello World", hello_world),
        ("Hello with Name", lambda: hello_name("Python Developer")),
        ("Uppercase Hello", hello_uppercase),
        ("Lowercase Hello", hello_lowercase),
        ("Reversed Hello", hello_reverse),
        ("Repeated Hello", lambda: hello_repeat(3)),
        ("Hello with Timestamp", hello_with_timestamp),
        ("Random Language Hello", hello_random_language),
        ("ASCII Art Hello", hello_ascii_art),
        ("Bordered Hello", hello_bordered),
        ("Countdown Hello", lambda: hello_countdown(3)),
        ("Custom Hello", lambda: hello_custom("Greetings", "Universe", "!!!")),
    ]

    print("=" * 60)
    print("  Hello World App — SCRUM-1221 Demo")
    print("=" * 60)

    for title, func in functions:
        print(f"\n--- {title} ---")
        func()

    print("\n" + "=" * 60)
    print("  All functions demonstrated successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
