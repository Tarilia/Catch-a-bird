lint:
	poetry run flake8 catch_a_bird.py

install:
	poetry install

build: # сборка пакета
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install: # установка пакета в систему
	python3 -m pip install --user dist/*.whl

package-reinstall: # переустановка пакета в систему после обновления
	pip install --user --force-reinstall dist/*.whl

catch-bird: # запуск программы
	poetry run python -m catch_a_bird
