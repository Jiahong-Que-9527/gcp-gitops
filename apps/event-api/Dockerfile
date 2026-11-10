# [房玄龄·2026-11-10] Learning image; record a digest before cloud/GitOps promotion.
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 HOST=0.0.0.0 PORT=8080
WORKDIR /app
COPY --chown=10001:10001 app.py contract.py ./
USER 10001:10001
EXPOSE 8080
CMD ["python", "app.py"]
