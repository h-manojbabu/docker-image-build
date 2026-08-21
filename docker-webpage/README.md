# Docker Static Web Page

A simple Docker project that serves a static HTML page using NGINX.

## Project Overview

This project demonstrates:

- Creating a custom Docker image
- Writing a Dockerfile
- Building Docker images
- Running Docker containers
- Publishing images to Docker Hub
- Managing source code in GitHub

## Project Structure

```text
staticwebpage/
├── Dockerfile
├── index.html
└── README.md
```

## Prerequisites

- Docker Installed
- Git Installed
- Docker Hub Account
- GitHub Account

## Build the Image

```bash
docker build -t staticwebpage:v1 .
```

Verify:

```bash
docker images
```

## Run the Container

```bash
docker run -d \
--name staticwebpage \
-p 8080:80 \
staticwebpage:v1
```

Verify:

```bash
docker ps
```

Access the application:

```text
http://localhost:8080
```

## Docker Hub Image

Pull Image:

```bash
docker pull hmanojbabu/staticwebpage:v1
```

Run Image:

```bash
docker run -d -p 8080:80 hmanojbabu/staticwebpage:v1
```

## Useful Commands

View running containers:

```bash
docker ps
```

View logs:

```bash
docker logs staticwebpage
```

Stop container:

```bash
docker stop staticwebpage
```

Remove container:

```bash
docker rm staticwebpage
```

Remove image:

```bash
docker rmi staticwebpage:v1
```

## Learning Outcomes

After completing this project, I learned:

- Docker Image Creation
- Dockerfile Basics
- Container Lifecycle Management
- Docker Hub Integration
- GitHub Source Control

## Author

**Manoj Naik**

Infra Technology Specialist | Cloud & DevOps Engineer

Technologies:
AWS • Azure • Docker • Kubernetes • Terraform • Ansible • Linux
