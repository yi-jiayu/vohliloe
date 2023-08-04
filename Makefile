requirements.txt: poetry.lock
	poetry export --without-hashes > requirements.txt
