# [房玄龄·2026-11-10]
PYTHON ?= python3
.PHONY: check test run replay doctor terraform-check
check: test
	$(PYTHON) tools/check_repo.py
test:
	$(PYTHON) -m unittest discover -s tests -v
run:
	$(PYTHON) apps/event-api/app.py
replay:
	$(PYTHON) tools/replay.py samples/events.json
doctor:
	bash tools/doctor.sh
terraform-check:
	bash tools/validate_terraform.sh
