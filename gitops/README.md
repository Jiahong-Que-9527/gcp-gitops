> [房玄龄·2026-11-10] Starter implementation; GCP execution pending.

# GitOps starter boundary

These manifests render offline. They do not install GKE or Argo CD. The image
is an obvious placeholder, so the workload is not deployment-ready.

```bash
kubectl kustomize gitops/workloads/event-api/overlays/dev
```

In labs 19–21: obtain a reviewed cluster, install a fixed Argo CD version,
bootstrap the `lab-dev` namespace and restricted AppProject, publish a real
image, replace the placeholder with `registry/image@sha256:...`, and review
resource scope before creating the Application. Do not apply the whole repo.

AppProject allows only Deployment and Service in `lab-dev`. No Namespace,
cluster-wide permissions, CreateNamespace, deletion finalizer, automated sync
or prune is configured. First sync is manual. Self-healing is enabled only as
an explicit later exercise. GitOps reconciliation is therefore **not yet active**.

Use a private local port-forward path for initial tests; no public LoadBalancer
is created. GKE must have permission to pull the selected Artifact Registry image.
Do not put registry keys or kubeconfig in Git.
