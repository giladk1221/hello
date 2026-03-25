# Hello World Python App

**Jira Ticket:** Scrum-1221

A Python application with multiple hello world greeting functions.

## Functions

| Function | Description |
|---|---|
| `hello_world()` | Returns a basic "Hello, World!" greeting |
| `hello_name(name)` | Returns a personalized greeting for the given name |
| `hello_greeting(name, greeting)` | Returns a customizable greeting with a chosen greeting word |
| `hello_time(name)` | Returns a time-appropriate greeting (morning/afternoon/evening) |
| `hello_upper(name)` | Returns an uppercase greeting |
| `hello_lower(name)` | Returns a lowercase greeting |
| `hello_repeat(name, times)` | Returns a greeting repeated a specified number of times |
| `hello_random(name)` | Returns a greeting in a randomly chosen language |
| `hello_reverse(name)` | Returns a greeting with the name reversed |

## Usage

```bash
python3 hello_world.py
```

### Import in your own code

```python
from hello_world import hello_name, hello_time

print(hello_name("Alice"))       # Hello, Alice!
print(hello_time("Bob"))         # Good morning, Bob!  (varies by time of day)
```
