CC=g++
CFLAGS=-c -Wall

all: output

output: main.o table.o graph.o
	$(CC) main.o table.o graph.o -o output

main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp

table.o: table.cpp
	$(CC) $(CFLAGS) table.cpp

graph.o: graph.cpp
	$(CC) $(CFLAGS) Graph.cpp

clean:
	rm *o output

