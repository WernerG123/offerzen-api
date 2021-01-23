#!/bin/sh

PYTHON=python3
PYTHON_PIP=pip

for req_file in $(find . -name requirements.txt) ; do
	${PYTHON_PIP} install -r ${req_file}
done