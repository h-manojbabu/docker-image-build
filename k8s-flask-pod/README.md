# Kubernetes Flask Pod

This project demonstrates how to deploy a Docker image as a Kubernetes Pod using K3s.

## Deploy

```bash
kubectl apply -f pod.yaml
```

## Verify

```bash
kubectl get pods
```

## Access

```bash
kubectl port-forward pod/flask-pod 5000:5000
```

## Test

```bash
curl http://localhost:5000
```

## What I Learned

- Kubernetes Pod
- kubectl
- Port Forwarding
- Pod Lifecycle
- Container Deployment
`
