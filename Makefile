push: test
	git push
format: 
	autopep8 --in-place --recursive
test: format 
	pytest tests

