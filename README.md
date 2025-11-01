# 🚀 ELEVATE_LABS_TASK_8

> **Task 8: Deploy a Dockerized Web Application on the Cloud using AWS ECS (Fargate)**  
> A hands-on showcase of containerization, cloud orchestration, and recruiter-ready documentation.

---

## 🏆 **Highlights & Badges**

![AWS](https://img.shields.io/badge/AWS-Fargate-orange?logo=amazonaws)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?logo=terraform)
![Status](https://img.shields.io/badge/Deployment-Success-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🎯 **Objective**

To deploy a **containerized web application** on the cloud using **AWS ECS (Fargate)** for serverless container orchestration, enabling **scalable, cost-efficient, and managed deployments**.

---

## 🧩 **Project Overview**

This project demonstrates how to:
- 🐳 **Containerize** a web application using Docker.  
- ☁️ **Deploy** it on AWS using **Elastic Container Service (ECS)** with **Fargate**.  
- ⚙️ Use **Terraform** for **Infrastructure as Code (IaC)** to automate setup.  
- 📦 Run the application **without managing servers**, achieving scalability and high availability.

---

🧩 Architecture Explanation(for the figure 1 given below at the bottom)

This architecture explains how a Dockerized application is deployed seamlessly using AWS ECS (Fargate) — eliminating the need for manual server management.

---
🧑‍💻 1️⃣ Local Machine

The developer starts by writing the application code (Flask, Node.js, etc.).

A Dockerfile is created to containerize the app.

The Docker image is built and tested locally:

docker build -t myapp .
docker run -p 8080:8080 myapp

---



After verification, the image is ready to be pushed to AWS.

📦 Purpose: To create a portable container that can run consistently anywhere.

---
🐳 2️⃣ Amazon ECR (Elastic Container Registry)

ECR is a secure Docker image repository hosted by AWS.

The tested image is pushed here using:

docker push <AWS_ACCOUNT_ID>.dkr.ecr.<region>.amazonaws.com/myapp:latest

---

ECS (Elastic Container Service) pulls this image when deploying.

📦 Purpose: Acts as a centralized, private storage for container images.

⚙️ 3️⃣ ECS Task Definition

This is a blueprint that defines how your container should run.

It specifies:

Which Docker image to use

CPU and memory requirements

Environment variables and network settings

---

📦 Purpose: Tells ECS what to run and how to run it.

---

🚀 4️⃣ ECS Cluster

A Cluster groups together multiple running tasks or services.

ECS manages where and how containers are launched.

In this project, it uses AWS Fargate, a serverless compute engine.

---

📦 Purpose: Provides an orchestration layer to manage containerized workloads efficiently.

---

🧭 5️⃣ Fargate Service

AWS Fargate runs containers without the need to manage EC2 instances.

It automatically provisions compute resources and scales as needed.

Each container (task) runs in its own isolated environment.

📦 Purpose: Fully managed, serverless container runtime — no servers to manage.

---

🌐 6️⃣ Application Load Balancer (ALB)

The ALB evenly distributes traffic among running containers in Fargate.

Provides a single public endpoint (DNS name) for users, such as:

http://ecs-fargate-loadbalancer-xxxxxxx.amazonaws.com


Ensures scalability, fault tolerance, and high availability.

---

📦 Purpose: Handles routing and load balancing for seamless user experience.

---

👥 7️⃣ Users

End users access the deployed application through the ALB’s public URL.

The ALB routes incoming requests to healthy containers running in Fargate.

This guarantees zero downtime, auto-scaling, and high performance.

---

📦 Purpose: Provide end users with access to the live, cloud-hosted app.

---

🔁 End-to-End Flow Summary

Developer builds and tests a Docker image locally.

The image is pushed to Amazon ECR.

An ECS Task Definition describes how to run it.

The ECS Cluster launches it using Fargate.

The Application Load Balancer distributes user requests.

Users access the app via the ALB endpoint.

---

💡 In Simple Terms

🧭 “You build once, push to AWS, and AWS Fargate runs your container automatically — no servers, no stress.”

---

✅ Key Takeaway:
This architecture provides a serverless, scalable, and cost-effective way to deploy applications using containers.
It represents the modern DevOps workflow — from local development → containerization → automated deployment → cloud accessibility.

---

## ⚖️ **Difference Between ECR, ECS, and Docker**

| Feature / Aspect | 🐳 **Docker** | 🏗️ **Amazon ECR (Elastic Container Registry)** | 🚀 **Amazon ECS (Elastic Container Service)** |
|------------------|---------------|-----------------------------------------------|-----------------------------------------------|
| **Definition** | An open-source platform to build, ship, and run containers. | A fully managed container image registry by AWS. | A container orchestration service to run and manage Docker containers. |
| **Purpose** | Used to create and package applications into containers. | Used to store, manage, and share Docker container images securely. | Used to deploy, scale, and manage containers in the cloud. |
| **Where It Runs** | On local machines, servers, or cloud environments. | Managed service within AWS cloud. | Managed service within AWS (supports EC2 or Fargate). |
| **Managed By** | User (you manage installation, updates, etc.). | AWS (fully managed registry). | AWS (fully managed orchestration). |
| **Storage Role** | Does not store images permanently; needs a registry like Docker Hub or ECR. | Acts as the **private Docker image storage** for AWS workloads. | Pulls images from ECR or Docker Hub to run them in containers. |
| **Use Case Example** | Build and test a container locally before deployment. | Store versioned Docker images securely before ECS deployment. | Run and manage multiple containers using ECS Tasks and Fargate. |
| **Integration** | Integrates with Docker Hub, Kubernetes, Jenkins, etc. | Integrates with ECS, EKS, and AWS CI/CD pipelines. | Integrates with ECR, CloudWatch, IAM, and Application Load Balancer. |
| **Security Management** | Depends on Docker configuration. | IAM-based access control and encryption. | IAM roles, task permissions, and secure networking. |
| **Pricing** | Free and open-source. | Pay for data storage and image transfers. | Pay for compute usage (EC2 or Fargate) and load balancing. |
| **Example Command** | `docker build -t myapp .` | `docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/myapp` | `ecs run-task --cluster my-cluster --task my-task` |

---

### 🧠 **Summary**
- **Docker** → Builds and runs containers locally.  
- **ECR** → Securely stores container images in AWS.  
- **ECS** → Runs and manages containers at scale using **Fargate** (serverless) or **EC2** (manual).  

✅ **In short:**  
> 🐳 *Docker builds it → 🏗️ ECR stores it → 🚀 ECS runs it.*
---

## Kaniko Build Process Demo(my future plans)

Kaniko is a tool to build container images from a Dockerfile, inside a container or Kubernetes cluster.

![Kaniko Build Demo](https://devopscube.com/content/images/2025/03/kaniko-1-1.gif)

This demo shows how Kaniko executes builds without requiring privileged access or a Docker daemon. It's ideal for CI/CD pipelines running in Kubernetes.

# 🚀 What is Kaniko?

Kaniko is an open-source tool developed by Google that builds container images from a Dockerfile **inside a container or Kubernetes cluster**. Unlike traditional Docker builds, Kaniko does **not require a Docker daemon or root privileges**, making it a secure and scalable solution for cloud-native environments.

## 🔧 Why Use Kaniko?

Kaniko solves a key problem in containerized CI/CD workflows: building images in environments where Docker can't run securely or at all. Here's why it's widely adopted:

- **Daemonless builds**: Kaniko runs entirely in userspace, avoiding the need for a Docker daemon.
- **Security**: No root access required, making it safe for multi-tenant Kubernetes clusters.
- **CI/CD friendly**: Perfect for automated pipelines in GitHub Actions, GitLab CI, Jenkins, and more.
- **Registry integration**: Kaniko can build and push images directly to Docker Hub, Amazon ECR, Google Container Registry, etc.
- **Kubernetes-native**: Runs as a pod using the `gcr.io/kaniko-project/executor` image.

## 📦 How It Works

Kaniko executes each Dockerfile instruction in order, taking a snapshot of the filesystem after each step. These snapshots become image layers, which Kaniko then assembles and pushes to your container registry.

---

# 🛠️ Daily DevOps Commands: Docker, ECR, ECS, Fargate

This section documents frequently used CLI commands for containerized deployments in AWS. These commands are essential for building, pushing, and deploying apps using Docker, Amazon ECR, ECS, and Fargate.

---

## 🐳 Docker Commands

| Task | Command |
|------|--------|
| Build image | `docker build -t my-app .` |
| Run container locally | `docker run -p 5000:5000 my-app` |
| Tag image for ECR | `docker tag my-app:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my-app:latest` |
| List images | `docker images` |
| Remove image | `docker rmi my-app` |
| Stop container | `docker stop <container_id>` |
| Remove container | `docker rm <container_id>` |

---

## 📦 Amazon ECR Commands

| Task | Command |
|------|--------|
| Authenticate Docker to ECR | `aws ecr get-login-password --region <region> \`<br>`| docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com` |
| Create ECR repository | `aws ecr create-repository --repository-name my-app` |
| Push image to ECR | `docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my-app:latest` |
| List repositories | `aws ecr describe-repositories` |
| Delete repository | `aws ecr delete-repository --repository-name my-app --force` |

---

## 🚀 Amazon ECS + Fargate Commands

| Task | Command |
|------|--------|
| Register task definition | `aws ecs register-task-definition --cli-input-json file://task-def.json` |
| Create ECS cluster | `aws ecs create-cluster --cluster-name my-cluster` |
| Run task on Fargate | `aws ecs run-task --cluster my-cluster --launch-type FARGATE --network-configuration file://network.json --task-definition my-task` |
| List running tasks | `aws ecs list-tasks --cluster my-cluster` |
| Stop running task | `aws ecs stop-task --cluster my-cluster --task <task_id>` |

---

## ✅ Pro Tips

- Use `jq` to parse JSON outputs for clarity.
- Automate these commands in GitHub Actions or Terraform for production-grade workflows.
---
# ⚠️ Challenges Faced During Deployment

This section outlines real-world issues encountered while deploying containerized applications using Docker, Amazon ECR, ECS, and Fargate. Each challenge includes a brief description and resolution strategy to help others avoid similar pitfalls.

---

## 🐳 Docker

| Challenge | Description | Resolution |
|----------|-------------|------------|
| Image not found | Docker fails to locate the image during `run` or `push`. | Ensure correct image tag and verify with `docker images`. |
| Port conflicts | Local port already in use. | Use `docker ps` to identify running containers and free up the port. |
| Large image size | Slow builds and pushes. | Optimize Dockerfile with `.dockerignore`, multi-stage builds, and smaller base images. |

---

## 📦 AWS ECR

| Challenge | Description | Resolution |
|----------|-------------|------------|
| Login failure | `docker login` to ECR fails due to expired credentials. | Use `aws ecr get-login-password` to refresh credentials. |
| Push denied | Permission error when pushing image. | Check IAM role and ECR repository policy. |
| Repository not found | CLI errors when pushing to non-existent repo. | Create repo using `aws ecr create-repository`. |

---

## 🚀 ECS + Fargate

| Challenge | Description | Resolution |
|----------|-------------|------------|
| Task stuck in `PROVISIONING` | Misconfigured network or IAM role. | Validate VPC, subnets, and task execution role. |
| Container exits immediately | App crashes due to missing env vars or port mismatch. | Check logs in CloudWatch and verify task definition. |
| Load balancer not routing | Health checks fail or target group misconfigured. | Adjust health check path and ensure container responds correctly. |

---

## ✅ Lessons Learned

- Always validate IAM roles and policies before deployment.
- Use CloudWatch logs for deep troubleshooting.
- Document every fix to build a recruiter-facing transparency section.

---

## 🏗️ **Architecture Diagram(figure 1)**

```mermaid
flowchart LR
    A[Local Machine 🧑‍💻] -->|Push Docker Image| B[(Amazon ECR 🐳)]
    B --> C[ECS Task Definition ⚙️]
    C --> D[ECS Cluster 🚀]
    D --> E[Fargate Service 🧭]
    E --> F[Application Load Balancer 🌐]
    F --> G[(Users 👥)]

