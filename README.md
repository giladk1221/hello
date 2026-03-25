# Hello World Python App

**SCRUM-1221** — A Python hello world application with multiple greeting functions.

## Functions

| Function | Description |
|---|---|
| `hello_world()` | Basic "Hello, World!" |
| `hello_name(name)` | Greet a specific person by name |
| `hello_uppercase()` | Hello world in UPPERCASE |
| `hello_lowercase()` | Hello world in lowercase |
| `hello_reverse()` | Hello world printed in reverse |
| `hello_repeat(times)` | Print hello world multiple times |
| `hello_with_timestamp()` | Hello world with current UTC timestamp |
| `hello_random_language()` | Hello world in a random language |
| `hello_ascii_art()` | Hello world as ASCII art |
| `hello_bordered()` | Hello world inside a decorative border |
| `hello_countdown(start)` | Countdown before saying hello |
| `hello_custom(greeting, target, punctuation)` | Fully customizable greeting |

## Usage

Run the demo to see all functions in action:

```bash
python hello_world.py
```

Or import individual functions:

```python
from hello_world import hello_name, hello_random_language

hello_name("Alice")
hello_random_language()
```

## Requirements

- Python 3.6+
