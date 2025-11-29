variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "project_name" {
  type    = string
  default = "hybrid-autoscaling-microservice"
}

variable "docker_image" {
  type = string
  # e.g. "YOUR_DOCKERHUB_USER/autoscaling-microservice:latest"
}

