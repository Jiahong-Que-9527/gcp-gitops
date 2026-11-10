# [房玄龄·2026-11-10]
variable "image" {
  description = "Built Artifact Registry image pinned by SHA256 digest."
  type        = string
  validation {
    condition     = can(regex("^[a-z0-9-]+-docker\\.pkg\\.dev/.+@sha256:[a-f0-9]{64}$", var.image))
    error_message = "Use an Artifact Registry image@sha256:digest, not a mutable tag."
  }
}
resource "google_service_account" "runtime" {
  account_id   = "gitops-${var.environment}-runtime"
  display_name = "Synthetic event API runtime; no project roles by default"
}
resource "google_cloud_run_v2_service" "api" {
  name                = "gitops-${var.environment}-event-api"
  location            = var.region
  deletion_protection = true
  ingress             = "INGRESS_TRAFFIC_ALL"
  labels              = { project = "gcp-gitops", environment = var.environment }
  template {
    service_account = google_service_account.runtime.email
    scaling {
      min_instance_count = 0
      max_instance_count = 2
    }
    max_instance_request_concurrency = 8
    timeout                          = "30s"
    containers {
      image = var.image
      ports { container_port = 8080 }
      resources {
        limits   = { cpu = "1", memory = "256Mi" }
        cpu_idle = true
      }
      env {
        name  = "APP_VERSION"
        value = var.image
      }
      startup_probe {
        http_get { path = "/healthz" }
      }
    }
  }
}
output "service_uri" { value = google_cloud_run_v2_service.api.uri }
output "runtime_identity" { value = google_service_account.runtime.email }
