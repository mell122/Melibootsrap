#!/bin/bash

# Set your AWS region and EKS cluster name
AWS_REGION="us-west-2"
EKS_CLUSTER_NAME="my-eks-cluster"

# Run Terraform to create the EKS cluster and output kubeconfig filename
terraform init
terraform apply -auto-approve
KUBECONFIG_FILENAME=$(terraform output kubeconfig)

# Download and update kubeconfig
aws eks --region $AWS_REGION update-kubeconfig --name $EKS_CLUSTER_NAME --kubeconfig $KUBECONFIG_FILENAME

# Verify configuration
kubectl get nodes
