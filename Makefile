SHELL := /bin/bash

push: test
	git push
format: 
	venv/bin/python3.10 -m autopep8 --in-place --recursive ./src

test: format 
	pytest tests

