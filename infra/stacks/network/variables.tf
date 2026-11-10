# [房玄龄·2026-11-10]
variable "project_id" {
  description = "Existing dedicated sandbox project ID; no project is created."
  type        = string
  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{4,28}[a-z0-9]$", var.project_id))
    error_message = "Use a valid, explicitly selected GCP project ID."
  }
}
variable "region" {
  description = "Region chosen after checking product availability and pricing."
  type        = string
  default     = "europe-west3"
}
variable "environment" {
  description = "Learning environment label."
  type        = string
  default     = "dev"
  validation {
    condition     = contains(["dev", "stage"], var.environment)
    error_message = "Use dev or stage."
  }
}
