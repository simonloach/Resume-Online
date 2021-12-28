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
	@curl localhost:5000/deploy