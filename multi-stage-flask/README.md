# Docker Multi-Stage Build

This project demonstrates how to use Docker Multi-Stage Builds to create smaller and more efficient Docker images.

## What is a Multi-Stage Build?

A multi-stage build separates the build process from the runtime environment.

Benefits:

- Smaller image size
- Better security
- Faster deployments
- Production-ready images

## Project Structure

```text
multi-stage-flask/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Build Image

```bash
docker build -t multi-stage-flask:v1 .
```

Verify:

```bash
docker images
```

## Run Container

```bash
docker run -d \
--name multi-stage-demo \
-p 5000:5000 \
multi-stage-flask:v1
```

## Test Application

```bash
curl http://localhost:5000
```

Expected Output:

```html
CloudOps Chronicle
Docker Multi-Stage Build Demo
```

## Check Image Layers

```bash
docker history multi-stage-flask:v1
```

## Docker Hub

```bash
docker pull hmanojbabu/multi-stage-flask:v1
```

## What I Learned

- Multi-Stage Builds
- Builder and Runtime Images
- COPY --from
- Docker Image Layers
- Image Optimisation
- Production Docker Practices

## Author

Manoj Naik

CloudOps Chronicle
