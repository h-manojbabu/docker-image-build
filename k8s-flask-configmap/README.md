# Kubernetes End-to-End Flask Application

This project demonstrates deploying a Flask application on Kubernetes using K3s.

## Components

- Deployment
- Service
- NodePort
- Ingress
- ConfigMap
- Secret
- Persistent Volume (PV)
- Persistent Volume Claim (PVC)

## Architecture

```text
Ingress
   |
Service
   |
Deployment
   |
Pod
   |
PVC
   |
PV
```

## Deploy Resources

```bash
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

## Verify

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl get pvc
kubectl get pv
```

## Learning Outcomes

- Kubernetes Pods
- Deployments
- Services
- Ingress
- ConfigMaps
- Secrets
- Persistent Storage
