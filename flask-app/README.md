# Flask Application in Docker

A simple Python Flask web application containerised using Docker.

## Project Overview

This project demonstrates how to:

- Create a Python Flask application
- Define application dependencies
- Build a Docker image
- Run a containerised Flask application
- Publish Docker images to Docker Hub
- Manage source code using GitHub

## Project Structure

```text
flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Application Code

### app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Welcome to CloudOps Chronicle</h1>
    <h2>My First Flask Docker Application</h2>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Prerequisites

- Docker
- Git
- Docker Hub Account
- GitHub Account

## Build the Docker Image

```bash
docker build -t flask-app:v1 .
```

Verify the image:

```bash
docker images
```

## Run the Container

```bash
docker run -d \
--name flask-app \
-p 5000:5000 \
flask-app:v1
```

Verify:

```bash
docker ps
```

## Access the Application

Local machine:

```text
http://localhost:5000
```

EC2 instance:

```text
http://<EC2-Public-IP>:5000
```

> Ensure Security Group allows inbound TCP port 5000.

## Container Management

View logs:

```bash
docker logs flask-app
```

Access the container:

```bash
docker exec -it flask-app bash
```

Stop container:

```bash
docker stop flask-app
```

Remove container:

```bash
docker rm flask-app
```

## Docker Hub

Tag the image:

```bash
docker tag flask-app:v1 hmanojbabu/flask-app:v1
```

Push the image:

```bash
docker push hmanojbabu/flask-app:v1
```

Pull from Docker Hub:

```bash
docker pull hmanojbabu/flask-app:v1
```

Run directly from Docker Hub:

```bash
docker run -d -p 5000:5000 hmanojbabu/flask-app:v1
```

## Learning Outcomes

This project helped me understand:

- Python Flask Basics
- Dockerfile Instructions
- Python Dependency Management
- Container Networking
- Docker Image Publishing
- Docker Hub Integration
- Git and GitHub Workflow

## Future Enhancements

- Add HTML Templates
- Add CSS Styling
- Use Docker Compose
- Connect to a Database
- Deploy to Kubernetes
- Deploy to AWS EKS / Azure AKS

## Author

**Manoj Naik**

Infra Technology Specialist | Cloud & DevOps Engineer

Publication: **CloudOps Chronicle**

Technologies:
- AWS
- Azure
- Docker
- Kubernetes
- Terraform
- Ansible
- Linux
- DevOps
