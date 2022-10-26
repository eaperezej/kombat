.PHONY: test lint example


test:
	docker-compose up test

lint:
	docker-compose up lint

example:
	docker-compose up example

clean:
	docker-compose down
