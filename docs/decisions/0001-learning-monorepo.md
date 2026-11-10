> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# ADR 0001: start with one learning repository

Status: accepted for the learning scaffold, 2026-11-10.

Context: one learner needs a coherent progression, low maintenance overhead,
and reviewable evidence across cloud infrastructure and workloads.

Decision: keep a small reference app, Terraform roots, GitOps config and guides
in one repo with separate directories. CI validates without cloud credentials.
Start locally and serverless; add GKE when Kubernetes is the learning objective.

Consequences: this differs from independently owned production app/config
repositories. Release cadence and ownership may eventually justify splitting
the app. The Argo CD application watches only its deployment path.

Alternatives: separate repos immediately (more coordination); GKE first (more
baseline cost and concepts); all GCP services at once (weak validation).

References: [Argo CD practices](https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/),
[OpenGitOps](https://opengitops.dev/).
