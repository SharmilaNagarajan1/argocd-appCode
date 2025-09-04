# ArgoCD Application Code  

This repository contains the **source code and Dockerfile** for the sample application deployed using **GitHub Actions + ArgoCD**.  

## 🔹 Workflow  

1. Developer pushes code changes → GitHub Actions pipeline triggers.  
2. CI pipeline:  
   - Builds a new Docker image  
   - Pushes it to Docker Hub (or another registry)  
   - Updates the Kubernetes manifest in the [`argocd-deploy`](https://github.com/SharmilaNagarajan1/argocd-deploy) repo with the new image tag.  

## 🛠️ Tools & Technologies  
- GitHub Actions  
- Docker  
- Kubernetes  
- ArgoCD  

---
