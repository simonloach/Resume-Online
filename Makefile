.PHONY: up
up:
	@docker-compose build && docker-compose up -d
.PHONY: build
build:
	@docker-compose build --no-cache && docker-compose up -d
.PHONY: down
down:
	@docker-compose down

.PHONY: debug
debug:
	@docker-compose build && docker-compose up

.PHONY: deploy
deploy:
	@git fetch origin master
	@git reset --hard FETCH_HEAD
	@python3 -m venv venv
	@source ./venv/bin/activate
	@pip install -r requirements.txt
	@python3 jinja.py
	@cp -r html /resume-online/html