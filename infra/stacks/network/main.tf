# [房玄龄·2026-11-10]
resource "google_compute_network" "lab" {
  name                    = "gitops-${var.environment}"
  auto_create_subnetworks = false
  routing_mode            = "REGIONAL"
}
resource "google_compute_subnetwork" "lab" {
  name                     = "gitops-${var.environment}-primary"
  ip_cidr_range            = "10.42.0.0/24"
  region                   = var.region
  network                  = google_compute_network.lab.id
  private_ip_google_access = true
}
output "network_id" { value = google_compute_network.lab.id }
output "subnet_id" { value = google_compute_subnetwork.lab.id }
