restart_doc:
	docker compose down
	docker rmi -f exam_qayta-bot
	docker compose up