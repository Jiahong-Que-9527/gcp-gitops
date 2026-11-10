# [房玄龄·2026-11-10]
resource "google_storage_bucket" "raw" {
  name                        = "${var.project_id}-gitops-${var.environment}-raw"
  location                    = var.region
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
  force_destroy               = false
  labels                      = { project = "gcp-gitops", environment = var.environment }
  versioning { enabled = true }
}
output "bucket_name" {
  description = "Private synthetic-data bucket; no public IAM binding is created."
  value       = google_storage_bucket.raw.name
}
