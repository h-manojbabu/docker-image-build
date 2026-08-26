# Flask Application with Docker Volume

This project demonstrates how Docker Volumes can be used to persist application data even after containers are removed and recreated.

## Architecture

```text
User
  |
  v
Flask Container
  |
  v
Docker Volume
  |
  v
counter.txt
```

The application stores a visitor counter in a file inside a Docker Volume.

## Project Structure

```text
flask-volume/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Build Image

```bash
docker build -t flask-volume:v1 .
```

## Create Volume

```bash
docker volume create visit-data
```

## Run Container

```bash
docker run -d \
--name flask-volume-test \
-p 5000:5000 \
-v visit-data:/data \
flask-volume:v1
```

## Test

```bash
curl http://localhost:5000
```

Refresh multiple times:

```text
Visits: 1
Visits: 2
Visits: 3
```

## Verify Data Persistence

Remove the container:

```bash
docker rm -f flask-volume-test
```

Start it again:

```bash
docker run -d \
--name flask-volume-test \
-p 5000:5000 \
-v visit-data:/data \
flask-volume:v1
```

The counter value continues from the previous number instead of starting from 0.

## Inspect Volume

```bash
docker volume ls
docker volume inspect visit-data
```

## What I Learned

- Docker Volumes
- Data Persistence
- Container Storage
- Volume Mounts
- Container Lifecycle
- Persistent Application Data

## Docker Hub

```bash
docker pull hmanojbabu/flask-volume:v1
```

## Author

Manoj Naik

CloudOps Chronicle
