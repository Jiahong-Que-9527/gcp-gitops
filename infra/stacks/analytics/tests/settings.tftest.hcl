# [房玄龄·2026-11-10] Mocked provider; no cloud resources.
mock_provider "google" {}
run "protected_partitioned_events" {
  command = plan
  variables { project_id = "gitops-test-project" }
  assert {
    condition     = google_bigquery_table.events.require_partition_filter && google_bigquery_table.events.deletion_protection
    error_message = "Require bounded scans and explicit data deletion review."
  }
  assert {
    condition     = !google_bigquery_dataset.lab.delete_contents_on_destroy && google_bigquery_table.events.time_partitioning[0].field == "event_time"
    error_message = "Protect dataset contents and partition by event time."
  }
}
