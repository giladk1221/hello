#!/usr/bin/env python3
"""
Hello World Application - SCRUM-1221
A Python application with multiple hello world functions.
"""

import datetime
import random


def hello_world():
    """Print a basic hello world message."""
    print("Hello, World!")


def hello_name(name):
    """Print a personalized hello message.

    Args:
        name: The name of the person to greet.
    """
    if not name or not name.strip():
        print("Hello, World!")
    else:
        print(f"Hello, {name}!")


def hello_multilingual(language="english"):
    """Print hello world in different languages.

    Args:
        language: The language for the greeting (default: english).

    Returns:
        The greeting string.
    """
    greetings = {
        "english": "Hello, World!",
        "spanish": "¡Hola, Mundo!",
        "french": "Bonjour, le Monde!",
        "german": "Hallo, Welt!",
        "italian": "Ciao, Mondo!",
        "portuguese": "Olá, Mundo!",
        "japanese": "こんにちは、世界！",
        "chinese": "你好，世界！",
        "korean": "안녕하세요, 세계!",
        "russian": "Привет, мир!",
        "arabic": "!مرحبا بالعالم",
        "hindi": "नमस्ते, दुनिया!",
        "hebrew": "!שלום, עולם",
    }
    greeting = greetings.get(language.lower(), f"Hello, World! ('{language}' not supported)")
    print(greeting)
    return greeting


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


def hello_repeated(times=3):
    """Print hello world multiple times.

    Args:
        times: Number of times to print (default: 3).

    Returns:
        The repeated greeting string.
    """
    if times < 1:
        times = 1
    message = ("Hello, World! " * times).strip()
    print(message)
    return message


def hello_with_timestamp():
    """Print hello world with the current timestamp.

    Returns:
        The greeting string with timestamp.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Hello, World! Current time: {now}"
    print(message)
    return message


def hello_ascii_art():
    """Print hello world as ASCII art."""
    art = r"""
  _   _      _ _         __        __         _     _ _
 | | | | ___| | | ___    \ \      / /__  _ __| | __| | |
 | |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |
 |  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
 |_| |_|\___|_|_|\___( )    \_/\_/ \___/|_|  |_|\__,_(_)
                      |/
"""
    print(art)
    return art


def hello_random_greeting():
    """Print a random hello world variation.

    Returns:
        The randomly selected greeting string.
    """
    greetings = [
        "Hello, World!",
        "Hey there, World!",
        "Greetings, World!",
        "Hi, World!",
        "Howdy, World!",
        "What's up, World!",
        "Yo, World!",
        "Salutations, World!",
        "Good day, World!",
        "Hiya, World!",
    ]
    message = random.choice(greetings)
    print(message)
    return message


def hello_bordered():
    """Print hello world inside a decorative border.

    Returns:
        The bordered greeting string.
    """
    text = "Hello, World!"
    border = "+" + "-" * (len(text) + 2) + "+"
    message = f"{border}\n| {text} |\n{border}"
    print(message)
    return message


def hello_countdown(start=5):
    """Print a countdown followed by hello world.

    Args:
        start: The number to count down from (default: 5).

    Returns:
        The final greeting string.
    """
    if start < 1:
        start = 1
    for i in range(start, 0, -1):
        print(f"{i}...")
    message = "Hello, World!"
    print(message)
    return message


def hello_letter_by_letter():
    """Print hello world one letter at a time.

    Returns:
        The complete greeting string.
    """
    message = "Hello, World!"
    for char in message:
        print(char, end="", flush=True)
    print()
    return message


def main():
    """Run all hello world functions."""
    print("=" * 50)
    print("  Hello World Application - SCRUM-1221")
    print("=" * 50)

    print("\n1. Basic Hello World:")
    hello_world()

    print("\n2. Personalized Hello:")
    hello_name("Python Developer")

    print("\n3. Multilingual Hello (French):")
    hello_multilingual("french")

    print("\n4. Uppercase Hello:")
    hello_uppercase()

    print("\n5. Lowercase Hello:")
    hello_lowercase()

    print("\n6. Reversed Hello:")
    hello_reverse()

    print("\n7. Repeated Hello (3 times):")
    hello_repeated(3)

    print("\n8. Hello with Timestamp:")
    hello_with_timestamp()

    print("\n9. ASCII Art Hello:")
    hello_ascii_art()

    print("\n10. Random Greeting:")
    hello_random_greeting()

    print("\n11. Bordered Hello:")
    hello_bordered()

    print("\n12. Countdown Hello:")
    hello_countdown(3)

    print("\n13. Letter-by-Letter Hello:")
    hello_letter_by_letter()

    print("\n" + "=" * 50)
    print("  All functions executed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
