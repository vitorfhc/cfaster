.PHONY: clean dev package upload_test upload install

package:
	python setup.py sdist
	python setup.py bdist_wheel

upload-test: clean package
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload: clean package
	twine upload dist/*

install:
	python setup.py install

install-test:
	pip install --index https://test.pypi.org/simple --extra-index https://test.pypi.org/simple --upgrade cfaster

install-prod:
	pip install --upgrade cfaster

clean:
	rm -rf dist build *.egg-info
	find . -name __pycache__ -type d | xargs rm -rf

dev:
	docker-compose up --build -d
	docker-compose exec cfaster bash
