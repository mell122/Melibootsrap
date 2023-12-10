provider "aws" {
  region = "us-west-2"  # Set your desired AWS region
}

locals {
  cluster_name = "api-cluster"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = local.cluster_name
  subnets         = ["subnet-xxxxxx", "subnet-yyyyyy", "subnet-zzzzzz"]  # Replace with your subnet IDs
  vpc_id          = "vpc-xxxxxxxx"  # Replace with your VPC ID
  cluster_version = "1.21"          # Specify the desired Kubernetes version

  node_groups = {
    eks_nodes = {
      desired_capacity = 2
      max_capacity     = 3
      min_capacity     = 1

      key_name = "your-key-pair-name"  # Replace with your EC2 key pair name

      instance_type = "t2.small"  # Replace with your desired EC2 instance type

      additional_security_group_ids = ["sg-xxxxxx"]  # Replace with additional security groups if needed

      tags = {
        Terraform   = "true"
        Environment = "dev"
      }
    }
  }
}

output "kubeconfig" {
  value = module.eks.kubeconfig_filename
}
