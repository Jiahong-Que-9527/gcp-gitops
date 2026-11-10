# [房玄龄·2026-11-10]
resource "google_bigquery_dataset" "lab" {
  dataset_id                 = "gcp_gitops_${var.environment}"
  location                   = var.region
  delete_contents_on_destroy = false
  labels                     = { project = "gcp-gitops", environment = var.environment }
}
resource "google_bigquery_table" "events" {
  dataset_id               = google_bigquery_dataset.lab.dataset_id
  table_id                 = "events"
  deletion_protection      = true
  clustering               = ["airport"]
  require_partition_filter = true
  time_partitioning {
    type  = "DAY"
    field = "event_time"
  }
  schema = jsonencode([
    { name = "event_id", type = "STRING", mode = "REQUIRED" },
    { name = "flight_id", type = "STRING", mode = "REQUIRED" },
    { name = "event_time", type = "TIMESTAMP", mode = "REQUIRED" },
    { name = "airport", type = "STRING", mode = "REQUIRED" },
    { name = "delay_minutes", type = "FLOAT", mode = "REQUIRED" },
    { name = "synthetic", type = "BOOLEAN", mode = "REQUIRED" }
  ])
}
output "events_table" { value = google_bigquery_table.events.id }
