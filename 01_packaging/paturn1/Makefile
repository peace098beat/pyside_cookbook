.PHONY: all clean clean-pyc test install

all: clean clean-pyc

clean: clean-pyc

clean-pyc:
	rm -rf *.pyc
	rm -rf *.pyo
	rm -rf ./galib2/*.pyc
	rm -rf ./galib2/*.pyo
	rm -rf ./galib2/*/*.pyc
	rm -rf ./galib2/*/*.pyo

test:
	python -m unittest discover ./tests/

install:
	pip uninstall -y galib2
	python setup.py install
	python -m unittest discover ./tests/