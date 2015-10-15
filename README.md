# Hadoop
## Installation
### Install PyExZ3:
	sudo apt-get update
	sudo apt-get install git
	sudo apt-get install g++
	sudo apt-get install make
	git clone https://github.com/QubitPi/z3.git
	python scripts/mk_make.py
	cd build
	make
	sudo make install

export PYTHONPATH=/home/anna/z3/build
