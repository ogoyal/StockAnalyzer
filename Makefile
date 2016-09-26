all: build csv output

jenkins: build csv

build:
	mkdir -p build
	mkdir -p build/readme

csv:
	python python/stocks.py
	mv example.csv build/

output:
	cd build; cmake ../; \
	make

readme:
	cp python/csvtomd.py build/readme
	cp python/intro.md build/readme
	cp python/conclusion.md build/readme
	cp build/example.csv build/readme
	cd build/readme; python csvtomd.py; cat intro.md data.md conclusion.md > README.md; mv README.md ../../

clean:
	rm -rf build

