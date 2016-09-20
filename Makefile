all: build csv output

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

