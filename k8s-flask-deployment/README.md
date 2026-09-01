# Kubernetes Flask Deployment

This project demonstrates how to deploy a Flask application in Kubernetes using a Deployment.

## What is a Deployment?

A Deployment manages Pods and ensures the desired number of replicas are always running.

Benefits:

- Self-healing
- Scaling
- Rolling updates
- High availability

## Project Structure

```text
k8s-flask-deployment/
├── deployment.yaml
└── README.md
```

## Deploy Application

```bash
kubectl apply -f deployment.yaml
```

## Verify Deployment

```bash
kubectl get deployments
```

Expected:

```text
NAME               READY   UP-TO-DATE   AVAILABLE
flask-deployment   3/3
```

## Verify Pods

```bash
kubectl get pods
```

Expected:

```text
flask-deployment-xxxxx
flask-deployment-yyyyy
flask-deployment-zzzzz
```

## Scale Deployment

Scale to 5 replicas:

```bash
kubectl scale deployment flask-deployment --replicas=5
```

Verify:

```bash
kubectl get pods
```

Scale back to 2 replicas:

```bash
kubectl scale deployment flask-deployment --replicas=2
```

## Test Self-Healing

Delete a Pod:

```bash
kubectl delete pod <pod-name>
```

Watch Kubernetes automatically create a replacement Pod:

```bash
kubectl get pods -w
```

## View Deployment Details

```bash
kubectl describe deployment flask-deployment
```

## View Pod Logs

```bash
kubectl logs <pod-name>
```

## Remove Deployment

```bash
kubectl delete deployment flask-deployment
```

## What I Learned

- Kubernetes Deployments
- ReplicaSets
- Self-Healing
- Scaling Applications
- Pod Management
- Declarative Configuration

## Author

Manoj Naik

CloudOps Chronicle

////////////////////////////////////////////

# Kubernetes Ingress

This project demonstrates how to expose a Kubernetes Service using Ingress.

## Deploy

```bash
kubectl apply -f ingress.yaml
```

## Verify

```bash
kubectl get ingress
```

## Test

```bash
curl http://flask.local
```

## What I Learned

- Kubernetes Ingress
- Host-based routing
- Service exposure
- Reverse proxy concepts
