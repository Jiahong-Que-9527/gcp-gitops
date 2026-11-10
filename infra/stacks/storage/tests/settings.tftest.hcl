# [房玄龄·2026-11-10] Mocked provider; no cloud resources.
mock_provider "google" {}
run "private_versioned_bucket" {
  command = plan
  variables { project_id = "gitops-test-project" }
  assert {
    condition     = google_storage_bucket.raw.public_access_prevention == "enforced" && google_storage_bucket.raw.uniform_bucket_level_access
    error_message = "The bucket must enforce private, uniform access."
  }
  assert {
    condition     = !google_storage_bucket.raw.force_destroy && google_storage_bucket.raw.versioning[0].enabled
    error_message = "Preserve object versions and block forced object deletion."
  }
}
