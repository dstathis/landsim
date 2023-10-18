#!/usr/bin/env python3

import random

ITERATIONS = 1000000


def generate_deck(lands: int, dorks: int, others: int):
    return lands * ["L"] + dorks * ["D"] + others * ["O"]


def get_stats(lands: int, dorks: int, others: int):
    lands_results = [0, 0, 0, 0, 0, 0, 0, 0]
    deck = generate_deck(lands=lands, dorks=dorks, others=others)
    for _ in range(ITERATIONS):
        hand = random.choices(population=deck, k=7)
        lands_results[hand.count("L")] += 1
    print(lands_results)
    print([i * 100 / ITERATIONS for i in lands_results])

def main():
    random.seed()

    print("18 Lands")
    get_stats(lands=18, dorks=8, others=34)
    print()
    print("17 Lands")
    get_stats(lands=17, dorks=8, others=35)

        


if __name__ == "__main__":
    main()
