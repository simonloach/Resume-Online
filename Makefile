.PHONY: help install build html pdf deploy clean test open dev

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies with UV
	uv sync

build: html pdf ## Build both HTML and PDF

html: ## Generate HTML resume
	uv run python generate_resume.py

pdf: ## Generate PDF resume
	uv run python generate_pdf_cv.py

open: ## Open generated HTML in browser
	open html/index.html

deploy: build ## Deploy to S3 (requires AWS credentials)
	@if [ -z "$(S3_BUCKET)" ]; then \
		echo "Error: S3_BUCKET not set. Usage: make deploy S3_BUCKET=your-bucket-name"; \
		exit 1; \
	fi
	aws s3 sync html/ s3://$(S3_BUCKET)/ --delete --cache-control "public, max-age=3600"

clean: ## Clean generated files
	rm -f html/index.html html/cv.pdf

test: ## Run tests
	uv run pytest -v

dev: install build open ## Full development setup

.DEFAULT_GOAL := help
