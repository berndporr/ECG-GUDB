all:
	rm -rf dist
	python3 ./setup.py sdist
	python3 ./setup.py bdist_wheel
	twine check dist/*

upload:
	twine upload dist/*
