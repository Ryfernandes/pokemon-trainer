CC = gcc
CFLAGS = -Wall -std=c17 -g -pedantic

PokemonTrainer: main.o
	$(CC) $(CFLAGS) -o $@ $^

main.o: main.c
	$(CC) $(CFLAGS) -c $^