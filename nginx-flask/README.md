# NGINX Reverse Proxy with Flask

This project demonstrates how NGINX can act as a reverse proxy in front of a Flask application using Docker Compose.

## Architecture

```text
User
  |
  v
NGINX :80
  |
  v
Flask App :5000
```

NGINX receives requests on port 80 and forwards them to the Flask application running on port 5000.

## Files

```text
nginx-flask/
├── app.py
├── requirements.txt
├── Dockerfile
├── nginx.conf
├── docker-compose.yml
└── README.md
```

## Build

```bash
docker build -t nginx-flask-web .
```

## Run

```bash
docker compose up -d
```

## Verify

```bash
docker ps
```

Expected containers:

```text
nginx-proxy
flask-app
```

## Test

```bash
curl http://localhost
```

Expected output:

```html
CloudOps Chronicle
NGINX Reverse Proxy Demo
```

## Stop

```bash
docker compose down
```

## Docker Hub

```bash
docker pull hmanojbabu/nginx-flask:v1
```

## What we can Learn

- Docker Compose
- Multi-container applications
- NGINX Reverse Proxy
- Container Networking
- Service Discovery
- Flask Application Deployment
