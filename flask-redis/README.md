# Flask Redis Application using Docker Compose

A simple multi-container application built using Flask, Redis and Docker Compose.

## Architecture

```text
User
  |
  v
Flask Application
  |
  v
Redis
```

## Project Structure

```text
flask-redis/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Build Image

```bash
docker build -t flask-redis-web .
```

## Start Application

```bash
docker compose up -d
```

## Verify

```bash
docker ps
```

## Test

```bash
curl http://localhost:5000
```

## Stop

```bash
docker compose down
```

## Docker Hub Image

```bash
docker pull hmanojbabu/flask-redis:v1
```

## Learning Outcomes

- Docker Compose
- Multi-container Applications
- Container Networking
- Service Discovery
- Flask Integration
- Redis Integration

## Author

Manoj Naik

CloudOps Chronicle
