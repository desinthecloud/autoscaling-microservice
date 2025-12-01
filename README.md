# Auto-Scaling Microservice: Homelab + AWS Hybrid

This project showcases a production-style hybrid deployment where a containerized microservice runs across both my homelab and AWS. The goal was to simulate how real companies operate mixed on-prem and cloud environments while building fully automated DevOps workflows.

The result is a lightweight, scalable, observable microservice that can run locally or in AWS, with full CI/CD, autoscaling policies, and a teardown process for cost control.

Overview

This system deploys a Dockerized microservice to:

Homelab Deployment

Local Docker host running the service

Useful for rapid testing, experimenting, and simulating on-prem workloads

AWS Deployment

ECS Fargate cluster

Application Load Balancer

CloudWatch metrics for scaling

Public endpoint for testing

Automated CI/CD from GitHub Actions

By combining both environments, this project replicates a real hybrid infrastructure pattern used in enterprises moving from on-prem systems toward cloud-native workloads.

What This Project Demonstrates

Ability to design and operate hybrid architecture (on-prem + cloud)

Build, push, and deploy container images using GitHub Actions

Auto-scaling a microservice based on CloudWatch metrics

Exposing the service with an Application Load Balancer

Running identical containers in local and cloud environments

Cost awareness with teardown commands to fully clean AWS resources

Observability via CloudWatch logs

Infrastructure deployment with minimal friction

Architecture

Local (Homelab)

Docker Engine

Local network access

Quick feedback loop for testing changes

AWS

ECS Fargate Service + Cluster

Application Load Balancer (ALB)

Target Group

CloudWatch Alarms + Scaling Policies

Route 53 (optional)

CloudWatch Logs

This mirrors how real companies run hybrid workloads while migrating toward cloud-native designs.

Tech Stack

Docker

GitHub Actions

AWS ECS (Fargate)

AWS ALB

CloudWatch (logs + scaling)

Route 53

macOS Terminal

Bash

Repository Structure
/
├── src/                 # Microservice code
├── Dockerfile           # Container image
├── .github/workflows/   # CI/CD pipelines
│   └── build-and-push.yml
├── deploy/              # AWS + homelab deployment scripts
│   ├── deploy-homelab.sh
│   ├── deploy-aws.sh
│   └── teardown.sh
└── README.md

How It Works
1. Build & Push

A GitHub Actions workflow automatically:

Builds the Docker image

Tags it

Pushes to Docker Hub

2. Homelab Deployment

Run:

bash deploy/deploy-homelab.sh

3. AWS Deployment

Run:

bash deploy/deploy-aws.sh

4. Test the Service

Once deployed, hit the ALB endpoint:

curl http://your-alb-dns-name

5. Auto-Scaling

CloudWatch policies increase or decrease Fargate tasks based on CPU/Memory thresholds.
The ALB ensures traffic is routed to healthy tasks only.

6. Teardown

To avoid surprise charges:

bash deploy/teardown.sh

Business Value (Why This Project Matters)

This isn’t just a “fun build.” It matches how actual companies evolve their infrastructure:

Legacy on-prem environments transitioning toward cloud

Need for unified deployment pipelines

Cost-efficient compute using auto-scaling

Standardized container deployments across environments

Disaster recovery failover between homelab/local and cloud

Reduced operational overhead

This project demonstrates the ability to build systems that are portable, scalable, cost-aware, and production-ready.

Future Enhancements

Migrate manual deploy scripts into CloudFormation

Add private ECR registry

Integrate AWS Systems Manager for remote orchestration

Add Grafana dashboards for metrics

Support blue/green deployments

Author

Desiree Weston
Cloud | DevOps | AI Engineer
Portfolio: https://desinthecloud.com

GitHub: github.com/desinthecloud


