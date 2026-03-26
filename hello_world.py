#!/usr/bin/env python3
"""Hello World Python Application with multiple greeting functions."""

import datetime
import random
import time


def hello_world():
    """Print a basic hello world message."""
    message = "Hello, World!"
    print(message)
    return message


def hello_named(name):
    """Print a personalized hello message.

    Args:
        name: The name to greet.
    """
    message = f"Hello, {name}!"
    print(message)
    return message


def hello_uppercase():
    """Print hello world in uppercase."""
    message = "HELLO, WORLD!"
    print(message)
    return message


def hello_lowercase():
    """Print hello world in lowercase."""
    message = "hello, world!"
    print(message)
    return message


def hello_reverse():
    """Print hello world reversed."""
    message = "!dlroW ,olleH"
    print(message)
    return message


def hello_repeat(count=3):
    """Print hello world repeated a specified number of times.

    Args:
        count: Number of times to repeat the greeting.
    """
    messages = []
    for i in range(1, count + 1):
        msg = f"{i}. Hello, World!"
        print(msg)
        messages.append(msg)
    return messages


def hello_timestamp():
    """Print hello world with the current timestamp."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{now}] Hello, World!"
    print(message)
    return message


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
    message = f"{language}: {greetings[language]}"
    print(message)
    return message


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
    return art


def hello_bordered():
    """Print hello world inside a decorative border."""
    message = "Hello, World!"
    border = "+" + "-" * (len(message) + 2) + "+"
    result = f"{border}\n| {message} |\n{border}"
    print(result)
    return result


def hello_countdown(seconds=3):
    """Print a countdown before saying hello world.

    Args:
        seconds: Number of seconds to count down from.
    """
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    message = "Hello, World!"
    print(message)
    return message


def hello_custom(greeting="Hello", target="World", punctuation="!"):
    """Print a fully customizable hello world message.

    Args:
        greeting: The greeting word.
        target: The target of the greeting.
        punctuation: The punctuation to end with.
    """
    message = f"{greeting}, {target}{punctuation}"
    print(message)
    return message


def hello_multiline():
    """Print hello world across multiple lines with decoration."""
    lines = [
        "╔══════════════════╗",
        "║  H E L L O       ║",
        "║      W O R L D ! ║",
        "╚══════════════════╝",
    ]
    result = "\n".join(lines)
    print(result)
    return result


def main():
    """Run all hello world functions."""
    print("=== Basic Hello World ===")
    hello_world()
    print()

    print("=== Named Hello ===")
    hello_named("Python Developer")
    print()

    print("=== Uppercase Hello ===")
    hello_uppercase()
    print()

    print("=== Lowercase Hello ===")
    hello_lowercase()
    print()

    print("=== Reversed Hello ===")
    hello_reverse()
    print()

    print("=== Repeated Hello (3x) ===")
    hello_repeat(3)
    print()

    print("=== Timestamped Hello ===")
    hello_timestamp()
    print()

    print("=== Random Language Hello ===")
    hello_random_language()
    print()

    print("=== ASCII Art Hello ===")
    hello_ascii_art()
    print()

    print("=== Bordered Hello ===")
    hello_bordered()
    print()

    print("=== Custom Hello ===")
    hello_custom("Greetings", "Universe", "!!!")
    print()

    print("=== Multiline Hello ===")
    hello_multiline()
    print()

    print("=== Countdown Hello (skipping delay) ===")
    hello_countdown(0)


if __name__ == "__main__":
    main()
