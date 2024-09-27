<h1 align="center"><em>Docker</em></h1>

# Table of Contents

- 🐳 [Introduction to Docker](#introduction-to-docker)
- 💻 [Docker vs Virtual machines ](#docker-vs-virtual-machines)
- 🎼 [Docker composer](#docker-compose)
- ⌨️  [Important Docker Commands](#important-docker-commands)


## Introduction to Docker

  # Introduction to Docker

Docker is an open-source platform that enables developers to automate the deployment, scaling, and management of applications within lightweight, portable containers. It simplifies the process of building, running, and shipping applications by packaging all dependencies, libraries, and configuration files together in an isolated environment.

## What is a Docker Image?

- **Docker Image**: A Docker image is a lightweight, standalone, and executable package that contains everything needed to run a piece of software, including the code, runtime, libraries, environment variables, and configuration files.
- Images are **read-only** and serve as the blueprint or template for creating containers.
- **Layers**: Docker images consist of multiple layers, which represent changes or instructions defined in the Dockerfile (e.g., adding files, installing software).
- **Dockerfile**: This is a script containing a series of commands to build a Docker image.

### Key Points:
- Images are stored in a **Docker registry** like Docker Hub.
- Images can be **shared, versioned, and reused**, which makes collaboration easier.

## What is a Docker Container?

- **Docker Container**: A container is a runtime instance of a Docker image. It includes everything defined in the image and can be run in isolated environments, allowing applications to behave the same way regardless of where they are deployed.
- Containers are lightweight and share the host operating system's kernel, but run in isolated processes.
- Unlike images, containers are **mutable**: changes can be made and saved as new images if needed.

### Key Points:
- Containers are **portable**: they can be easily moved between different environments (e.g., local machine, cloud, etc.).
- Containers are **isolated** from each other, providing security and consistency between deployments.
  
## Why is Docker Used?

- **Portability**: Docker allows applications to run consistently across different environments, such as development, testing, and production, without compatibility issues.
- **Efficiency**: Docker containers are lightweight, using fewer system resources (CPU, memory) than traditional virtual machines. Multiple containers can run on the same host without the overhead of a full OS for each one.
- **Isolation**: Applications running in containers are isolated from one another, preventing conflicts between dependencies and environments.
- **Scalability**: Docker enables easy scaling of applications. You can run multiple instances of containers across various servers, which is useful for microservices architecture.
- **Fast Deployment**: Since containers share the OS kernel and do not need to boot an entire OS, they start up much faster than virtual machines.
- **Consistency**: Docker ensures that your application runs the same way, no matter where it's deployed. This reduces the "it works on my machine" problem during development.

### Key Use Cases:
- **Microservices Architecture**: Docker is ideal for running microservices, where each service runs in its own container.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Docker helps automate the testing, building, and deployment of applications in a consistent environment.
- **DevOps**: Docker bridges the gap between development and operations by providing a consistent platform for both teams.



# 🚀 Docker vs. Virtual Machines (VMs)

Both Docker and Virtual Machines (VMs) are used to create isolated environments for applications, but they work in fundamentally different ways.

## Docker 🐳

- **Containers**: Docker uses containers to package applications and their dependencies into isolated units.
- **Lightweight**: Containers share the host OS kernel, making them much more lightweight and faster to start up compared to VMs.
- **Portability**: Docker containers can run anywhere—on different systems, in the cloud, or locally—without modification.
- **Efficiency**: Because containers share the OS, they use fewer system resources (CPU, RAM) than VMs, enabling you to run more containers on the same hardware.

## Virtual Machines (VMs) 💻

- **Full OS**: Each VM runs its own entire operating system, including a separate kernel, on top of the host OS via a hypervisor.
- **Heavyweight**: Because each VM includes a full OS, they are larger, slower to boot, and require more system resources.
- **Greater Isolation**: VMs offer stronger isolation because they are fully virtualized, making them ideal for running completely independent systems.

## Key Differences:

- **Performance**: Docker is faster and uses fewer resources due to its lightweight nature.
- **Isolation**: VMs offer stronger isolation, but Docker's isolation is typically sufficient for most application scenarios.
- **Use Case**: Use Docker for microservices, scaling, and fast deployment. Use VMs when you need to run different OSes or when full isolation is critical.

In short, Docker is great for speed and efficiency, while VMs offer more robust isolation but come with greater resource overhead.


# Docker compose 

Docker Compose is a tool used for defining and managing multi-container Docker applications. It allows you to define a stack of containers that work together in a single YAML file (`docker-compose.yml`) and easily manage, start, or stop them with a single command.

## What is Docker Compose?

- **Docker Compose**: It is a command-line tool that helps define, configure, and manage multiple Docker containers as a single service.
- With Compose, you can define all of your application's services, networks, and volumes in a `docker-compose.yml` file, allowing you to run complex applications with just a single command.
  
## Key Features of Docker Compose

- **Multi-Container Applications**: Docker Compose makes it easy to manage applications that consist of multiple containers, each running different services (e.g., web server, database, cache, etc.).
- **YAML Configuration**: The `docker-compose.yml` file is used to define the configuration of the entire stack, including services, volumes, networks, and other options.
- **Simplified Commands**: You can use `docker-compose up` to start all services and `docker-compose down` to stop and remove containers, networks, and volumes.

## Structure of a `docker-compose.yml` File

A `docker-compose.yml` file typically includes:

1. **Services**: Each service represents a container (e.g., a web server, a database).
2. **Networks**: Define communication between services within the stack.
3. **Volumes**: Persistent data storage shared across services.

### Example of a `docker-compose.yml` File:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db

  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw
```

## Example Breakdown:

- Two services are defined: `web` (running Nginx) and `db` (running PostgreSQL).
- The `db` service uses a volume (`db-data`) for persistent storage.
- The `web` service exposes port 80 on the host.

## Common Docker Compose Commands

- **`docker-compose up`**: Creates and starts containers as defined in the `docker-compose.yml` file.
- **`docker-compose down`**: Stops and removes containers, networks, volumes, and images created by `up`.
- **`docker-compose build`**: Builds images defined in the `docker-compose.yml` file.
- **`docker-compose logs`**: Shows logs from all running services in the stack.
- **`docker-compose scale`**: Scales the number of containers for a specific service.

## Benefits of Docker Compose

- **Ease of Use**: Managing multi-container applications becomes simpler, with all configuration centralized in a YAML file.
- **Automation**: Compose automates the process of starting and stopping services, networks, and volumes, saving time and effort.
- **Portability**: The `docker-compose.yml` file can be shared across environments (development, testing, production), ensuring consistency.
- **Isolation**: Each service runs in its own container, maintaining isolation between them, which helps prevent dependency conflicts.
- **Local Development**: Docker Compose is particularly useful for local development environments, enabling developers to easily spin up the full application stack with a single command.

## Use Cases for Docker Compose

- **Microservices**: Compose is ideal for applications following a microservices architecture where multiple containers (services) need to work together.
- **CI/CD Pipelines**: Docker Compose can be used in CI/CD pipelines to spin up the entire application stack for testing before deployment.
- **Local Development Environments**: It provides an easy way to mirror production environments locally by defining all services in a single file.
- **Testing and Staging**: Easily create isolated environments for testing or staging applications with Compose, allowing each environment to have its own configuration.



# Important Docker Commands

## Important Docker Commands

| Command                          | Description                                                                                   |
| --------------------------------- | --------------------------------------------------------------------------------------------- |
| `docker build [OPTIONS] PATH`     | Builds a Docker image from a Dockerfile in the specified path.                                 |
| `docker pull [IMAGE]`             | Pulls a Docker image from a registry (e.g., Docker Hub).                                       |
| `docker push [IMAGE]`             | Pushes a Docker image to a registry.                                                          |
| `docker run [OPTIONS] IMAGE`      | Runs a container from the specified image with optional parameters (e.g., ports, volumes).     |
| `docker ps`                       | Lists all running containers.                                                                 |
| `docker ps -a`                    | Lists all containers, including stopped ones.                                                  |
| `docker stop [CONTAINER]`         | Stops a running container.                                                                    |
| `docker start [CONTAINER]`        | Starts a stopped container.                                                                   |
| `docker restart [CONTAINER]`      | Restarts a running or stopped container.                                                      |
| `docker rm [CONTAINER]`           | Removes a stopped container.                                                                  |
| `docker rmi [IMAGE]`              | Removes a Docker image.                                                                       |
| `docker logs [CONTAINER]`         | Shows the logs for a specific container.                                                      |
| `docker exec -it [CONTAINER] sh`  | Starts an interactive shell inside a running container.                                        |
| `docker inspect [CONTAINER/IMAGE]`| Shows detailed information about a container or image.                                        |
| `docker-compose up`               | Creates and starts all containers defined in a `docker-compose.yml` file.                     |
| `docker-compose down`             | Stops and removes containers, networks, and volumes defined in `docker-compose.yml`.           |
| `docker-compose logs`             | Shows logs from all running services in a `docker-compose` setup.                             |
| `docker network ls`               | Lists all Docker networks.                                                                    |
| `docker volume ls`                | Lists all Docker volumes.                                                                     |

