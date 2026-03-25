#!/usr/bin/env python3
"""Hello World Python Application - Scrum-1221

A collection of hello world greeting functions demonstrating
different ways to say hello.
"""

import datetime
import random


def hello_world():
    """Return a basic hello world greeting."""
    return "Hello, World!"


def hello_name(name):
    """Return a personalized greeting for the given name.

    Args:
        name: The name to greet.

    Returns:
        A personalized greeting string.
    """
    return f"Hello, {name}!"


def hello_greeting(name, greeting="Hello"):
    """Return a customizable greeting for the given name.

    Args:
        name: The name to greet.
        greeting: The greeting word to use (default: 'Hello').

    Returns:
        A custom greeting string.
    """
    return f"{greeting}, {name}!"


def hello_time(name):
    """Return a time-appropriate greeting based on the current hour.

    Args:
        name: The name to greet.

    Returns:
        A time-aware greeting string.
    """
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    return f"{greeting}, {name}!"


def hello_upper(name):
    """Return an uppercase greeting for the given name.

    Args:
        name: The name to greet.

    Returns:
        An uppercase greeting string.
    """
    return f"HELLO, {name.upper()}!"


def hello_lower(name):
    """Return a lowercase greeting for the given name.

    Args:
        name: The name to greet.

    Returns:
        A lowercase greeting string.
    """
    return f"hello, {name.lower()}!"


def hello_repeat(name, times=3):
    """Return a greeting repeated a given number of times.

    Args:
        name: The name to greet.
        times: Number of times to repeat the greeting (default: 3).

    Returns:
        A string with the greeting repeated.
    """
    return " ".join([f"Hello, {name}!"] * times)


def hello_random(name):
    """Return a greeting in a randomly chosen language.

    Args:
        name: The name to greet.

    Returns:
        A greeting in a random language.
    """
    greetings = [
        "Hello",     # English
        "Hola",      # Spanish
        "Bonjour",   # French
        "Hallo",     # German
        "Ciao",      # Italian
        "Shalom",    # Hebrew
        "Konnichiwa",  # Japanese
        "Namaste",   # Hindi
    ]
    return f"{random.choice(greetings)}, {name}!"


def hello_reverse(name):
    """Return a greeting with the name reversed.

    Args:
        name: The name to greet.

    Returns:
        A greeting with the reversed name.
    """
    return f"Hello, {name[::-1]}!"


def main():
    """Run all hello world functions and print results."""
    print(hello_world())
    print(hello_name("DevopsTeam"))
    print(hello_greeting("DevopsTeam", "Welcome"))
    print(hello_time("DevopsTeam"))
    print(hello_upper("DevopsTeam"))
    print(hello_lower("DevopsTeam"))
    print(hello_repeat("DevopsTeam", 2))
    print(hello_random("DevopsTeam"))
    print(hello_reverse("DevopsTeam"))


if __name__ == "__main__":
    main()
