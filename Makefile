push: test
	git push
format: 
	autopep8 --in-place --recursive ./src
test: format 
	pytest tests

