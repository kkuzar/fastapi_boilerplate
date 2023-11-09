
ECR_URL ?= 379815923190.dkr.ecr.eu-central-1.amazonaws.com/rgbd
IMAGE_TAG ?= latest

.PHONY: deps
deps: # Install the production deps
	@pip install -r ./requirements.txt

.PHONY: dev-deps
dev-deps: # Install the dev deps
	@pip install  -r ./requirements.txt -r ./requirements-dev.txt

.PHONY: setup
setup: dev-deps # setup for docker

.PHONY: format
format: ## Formatting the code.
	@isort .
	@black .

.PHONY: lint
lint: # lint da hell out of code.
	@flake8 .
	@black . --check
	@mypy app/

# .PHONY: pre-commit
# pre-commit: # run pre-commit on repo
# 	@pre-commit run -a

.PHONY: tidy
tidy: format lint   # pre-commit # Tidy up the code base

.PHONY: run
run: # running the viewer project backend in dev
	@PYTHONDONTWRITEBYTECODE=1 uvicorn app.main:app --reload

.PHONY: test
test:  # test the code
	@coverage run --source ./app -m pytest tests/ -x
	@coverage report --fail-under=85 -m

.PHONY: base-req
base-req:  #  run pip-compile in repo
	@pip-compile --generate-hashes ./requirements.in

.PHONY: req
req:  base-req
	@pip-compile --generate-hashes ./requirements-dev.in

.PHONY: docker-build-app
docker-build-viewer: # build viewer docker image
	@docker build -t $(ECR_URL):$(IMAGE_TAG) -f=app/docker/Dockerfile .
