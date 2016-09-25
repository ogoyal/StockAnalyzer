all: build csv output

jenkins: build csv

build:
	mkdir -p build

csv:
	python python/stocks.py
	mv example.csv build/

output:
	cd build; cmake ../; \
	make

clean:
	rm -rf build

