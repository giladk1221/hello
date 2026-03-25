# Hello World Application

This repository contains a simple Hello World application with both web and Python implementations.

## JIRA Ticket
- **Ticket Number**: SCRUM-1221
- **Description**: Create Python app with additional hello world functions

## Contents

### Web Application
- `index.html` - Simple HTML page displaying "Hello DevopsTeam!"
- `cloud_skills.jpg` - Image displayed on the web page
- `Dockerfile` - Docker configuration for nginx web server
- `manifests/` - Kubernetes deployment and service manifests

### Python Application
- `hello_world.py` - Python application with multiple hello world functions

## Python Application Functions

The Python application (`hello_world.py`) includes the following functions:

1. **`hello_world()`** - Returns basic "Hello World!" message
2. **`hello_world_print()`** - Prints hello world to console
3. **`hello_world_custom(name)`** - Returns personalized greeting with custom name
4. **`hello_world_multiple_languages()`** - Returns greetings in 8 different languages
5. **`hello_world_uppercase()`** - Returns hello world in uppercase
6. **`hello_world_lowercase()`** - Returns hello world in lowercase
7. **`hello_devops_team()`** - Returns greeting for DevOps team

## Running the Python Application

```bash
# Make the script executable (optional)
chmod +x hello_world.py

# Run the application
python3 hello_world.py
```

## Using the Functions

```python
from hello_world import hello_world, hello_world_custom, hello_world_multiple_languages

# Basic usage
print(hello_world())  # Output: Hello World!

# Custom greeting
print(hello_world_custom("Alice"))  # Output: Hello Alice!

# Multiple languages
languages = hello_world_multiple_languages()
print(languages["Spanish"])  # Output: ¡Hola Mundo!
```

## Docker Deployment

```bash
# Build the Docker image
docker build -t hello-app .

# Run the container
docker run -p 8080:80 hello-app
```

## Kubernetes Deployment

```bash
# Apply the deployment and service
kubectl apply -f manifests/deployment.yml
kubectl apply -f manifests/service.yml
```
