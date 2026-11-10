> [房玄龄·2026-11-10] Starter implementation; GCP execution pending.

# Synthetic event API

This dependency-free lab service validates a bounded batch and returns an
aggregate. It neither persists events nor provides end-to-end ingestion.
It is a small reference workload, not a hardened general-purpose web server.
Cloud Run IAM / a platform gateway must enforce cloud authentication.

```bash
python3 apps/event-api/app.py
# Optional local container exercise; no image pushed or cloud resource created:
docker build -t gcp-gitops-event-api:local apps/event-api
docker run --read-only --cap-drop=ALL --security-opt=no-new-privileges \
  -p 127.0.0.1:8080:8080 gcp-gitops-event-api:local
```

Stop with Ctrl-C. Do not add `--rm` when retention/deletion approval is required.
Retained stopped containers and images can be reviewed separately.

GET `/healthz` is liveness; GET `/version` reports APP_VERSION; POST `/validate`
accepts JSON with 1–1000 events and at most 1 MiB. Duplicate IDs are rejected
within a batch only; durable cross-request deduplication is a later lab.
HTTP 400 is malformed data, 413 body bounds, 415 wrong content type.

The Python base tag is deliberately readable for the first lab. Record and
review a base-image digest and vulnerability scan in lab 06; use immutable
application digests for deployment. No production throughput or DoS claim is made.
