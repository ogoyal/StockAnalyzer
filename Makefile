all: build csv output readme

jenkins: build csv readme

build:
	mkdir -p build/readme
	cp python/intro.md python/conclusion.md build/readme

csv:
	python python/stocks.py

output:
	cd build; cmake ../C++/; \
	make

readme:
	python python/csvtomd.py;
	cd build/readme; cat intro.md data.md conclusion.md > README.md; mv README.md ../..

clean:
	rm -rf build

