#!/usr/bin/env python3
"""
Hello World Python Application
JIRA Ticket: SCRUM-1221
"""


def hello_world():
    """
    Basic hello world function that returns a greeting message.

    Returns:
        str: A hello world greeting message
    """
    return "Hello World!"


def hello_world_print():
    """
    Prints hello world message to console.
    """
    print(hello_world())


def hello_world_custom(name="World"):
    """
    Returns a customized hello message with a given name.

    Args:
        name (str): The name to greet. Defaults to "World".

    Returns:
        str: A personalized greeting message
    """
    return f"Hello {name}!"


def hello_world_multiple_languages():
    """
    Returns hello world greetings in multiple languages.

    Returns:
        dict: A dictionary of greetings in different languages
    """
    greetings = {
        "English": "Hello World!",
        "Spanish": "¡Hola Mundo!",
        "French": "Bonjour le Monde!",
        "German": "Hallo Welt!",
        "Italian": "Ciao Mondo!",
        "Portuguese": "Olá Mundo!",
        "Japanese": "こんにちは世界!",
        "Chinese": "你好世界!",
    }
    return greetings


def hello_world_uppercase():
    """
    Returns hello world message in uppercase.

    Returns:
        str: Hello world message in uppercase
    """
    return hello_world().upper()


def hello_world_lowercase():
    """
    Returns hello world message in lowercase.

    Returns:
        str: Hello world message in lowercase
    """
    return hello_world().lower()


def hello_devops_team():
    """
    Returns a greeting for the DevOps team (matching the HTML content).

    Returns:
        str: A greeting for the DevOps team
    """
    return "Hello DevopsTeam!"


if __name__ == "__main__":
    # Demo all functions when script is run directly
    print("=== Hello World Python Application ===")
    print()

    print("1. Basic hello world:")
    hello_world_print()
    print()

    print("2. Custom greeting:")
    print(hello_world_custom("Python Developer"))
    print()

    print("3. Multiple languages:")
    languages = hello_world_multiple_languages()
    for lang, greeting in languages.items():
        print(f"   {lang}: {greeting}")
    print()

    print("4. Uppercase:")
    print(hello_world_uppercase())
    print()

    print("5. Lowercase:")
    print(hello_world_lowercase())
    print()

    print("6. DevOps Team greeting:")
    print(hello_devops_team())
