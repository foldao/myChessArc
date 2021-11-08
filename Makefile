push: test
	git push
test: format 
	pytest tests
format: 
	autopep8 --in-place --recursive

