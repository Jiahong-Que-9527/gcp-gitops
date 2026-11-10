# [房玄龄·2026-11-10] Mocked provider; no cloud resources.
mock_provider "google" {}
run "explicit_private_subnet" {
  command = plan
  variables { project_id = "gitops-test-project" }
  assert {
    condition     = !google_compute_network.lab.auto_create_subnetworks && google_compute_subnetwork.lab.private_ip_google_access
    error_message = "Use an explicit subnet with Private Google Access."
  }
  assert {
    condition     = google_compute_subnetwork.lab.ip_cidr_range == "10.42.0.0/24"
    error_message = "Keep the small learning CIDR explicit."
  }
}
