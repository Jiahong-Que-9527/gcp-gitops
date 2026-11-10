# [房玄龄·2026-11-10] Mocked provider; no cloud resources.
mock_provider "google" {}
run "bounded_runtime" {
  command = plan
  variables {
    project_id = "gitops-test-project"
    image      = "europe-west3-docker.pkg.dev/gitops-test-project/lab/event-api@sha256:0000000000000000000000000000000000000000000000000000000000000000"
  }
  assert {
    condition     = google_cloud_run_v2_service.api.deletion_protection && google_cloud_run_v2_service.api.template[0].scaling[0].min_instance_count == 0 && google_cloud_run_v2_service.api.template[0].scaling[0].max_instance_count == 2
    error_message = "Keep protection and explicit scale bounds."
  }
}
run "reject_mutable_tag" {
  command = plan
  variables {
    project_id = "gitops-test-project"
    image      = "europe-west3-docker.pkg.dev/gitops-test-project/lab/event-api:latest"
  }
  expect_failures = [var.image]
}
