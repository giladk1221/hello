#!/usr/bin/env python3
"""Hello World Python Application - KOKO-11

A collection of creative hello world functions demonstrating
various Python features and string manipulation techniques.
"""

import datetime
import random
import time
import textwrap


def hello_world():
    """Print a basic hello world message."""
    print("Hello, World!")


def hello_named(name="World"):
    """Print a personalized hello message.

    Args:
        name: The name to greet. Defaults to 'World'.
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
        times: Number of repetitions. Defaults to 3.
    """
    for i in range(1, times + 1):
        print(f"{i}. Hello, World!")


def hello_timestamp():
    """Print hello world with a timestamp."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Hello, World!")


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
    print(f"[{language}] {greetings[language]}")


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


def hello_countdown(seconds=3):
    """Print hello world after a countdown.

    Args:
        seconds: Number of seconds to count down. Defaults to 3.
    """
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Hello, World!")


def hello_custom(greeting="Hello", target="World", punctuation="!"):
    """Print a fully customizable hello world message.

    Args:
        greeting: The greeting word. Defaults to 'Hello'.
        target: The target of the greeting. Defaults to 'World'.
        punctuation: The ending punctuation. Defaults to '!'.
    """
    print(f"{greeting}, {target}{punctuation}")


def hello_multiline():
    """Print hello world across multiple formatted lines."""
    print(textwrap.dedent("""\
        ========================
          Welcome to the App!
          Hello, World!
          Have a great day!
        ========================"""))


def hello_char_by_char():
    """Print hello world one character at a time."""
    message = "Hello, World!"
    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()


def hello_leetspeak():
    """Print hello world in leetspeak."""
    leet_map = {
        "e": "3", "l": "1", "o": "0",
        "a": "4", "t": "7", "s": "5",
    }
    message = "Hello, World!"
    leet = "".join(leet_map.get(c.lower(), c) for c in message)
    print(leet)


def hello_alternating_case():
    """Print hello world with alternating upper/lower case."""
    message = "Hello, World!"
    result = "".join(
        c.upper() if i % 2 == 0 else c.lower()
        for i, c in enumerate(message)
    )
    print(result)


def hello_pig_latin():
    """Print hello world in pig latin."""
    def to_pig_latin(word):
        vowels = "aeiouAEIOU"
        if word[0] in vowels:
            return word + "yay"
        for i, char in enumerate(word):
            if char in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"

    words = "Hello World".split()
    pig = " ".join(to_pig_latin(w) for w in words)
    print(f"{pig}!")


def hello_emoji():
    """Print hello world with emojis."""
    print("👋 Hello, World! 🌍✨")


def main():
    """Run all hello world functions."""
    functions = [
        ("Basic", hello_world),
        ("Named", lambda: hello_named("Python Developer")),
        ("Uppercase", hello_uppercase),
        ("Lowercase", hello_lowercase),
        ("Reversed", hello_reverse),
        ("Repeated", lambda: hello_repeat(3)),
        ("Timestamp", hello_timestamp),
        ("Random Language", hello_random_language),
        ("ASCII Art", hello_ascii_art),
        ("Bordered", hello_bordered),
        ("Custom", lambda: hello_custom("Hey", "Universe", "!!")),
        ("Multiline", hello_multiline),
        ("Leetspeak", hello_leetspeak),
        ("Alternating Case", hello_alternating_case),
        ("Pig Latin", hello_pig_latin),
        ("Emoji", hello_emoji),
    ]

    for name, func in functions:
        print(f"\n--- {name} ---")
        func()


if __name__ == "__main__":
    main()
