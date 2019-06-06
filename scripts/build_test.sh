#!/bin/bash

pip install -r requirements.dev.txt
./scripts/clear.sh

python setup.py sdist bdist_wheel && \
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
