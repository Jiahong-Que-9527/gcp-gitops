# [房玄龄·2026-11-10]
terraform {
  required_version = ">= 1.14.0, < 2.0.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 8.10.0"
    }
  }
}
provider "google" {
  project = var.project_id
  region  = var.region
}
