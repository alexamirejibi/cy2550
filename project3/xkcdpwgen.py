#!/usr/bin/env python3

import sys
import argparse
import random


parser = argparse.ArgumentParser(description="Generate a secure, memorable password using the XKCD method")

parser.add_argument("-w", "--words", type=int, default=4, help="include WORDS words in the password (default=4)")
parser.add_argument("-c", "--caps", type=int, default=0, help="capitalize the first letter of CAPS random words (default=0)")
parser.add_argument("-n", "--numbers", type=int, default=0, help="insert NUMBERS random numbers in the password (default=0)")
parser.add_argument("-s", "--symbols", type=int, default=0, help="insert SYMBOLS random symbols in the password (default=0)")

args = parser.parse_args()

with open("words.txt", "r") as f:
    wordlist = [line.strip() for line in f.readlines()]

import random

def generate_password(words, caps, numbers, symbols):
    if words < 1:
        words = 1  # Ensure at least one word is present in the password

    selected_words = random.sample(wordlist, words)
    
    # Capitalize words
    for _ in range(caps):
        index = random.randint(0, words - 1)
        selected_words[index] = selected_words[index].capitalize()

    # Insert numbers
    for _ in range(numbers):
        index = random.randint(0, len(selected_words) - 1)
        at_end = random.randint(0, 1)
        if at_end:
            selected_words[index] += str(random.randint(0, 9))
        else:
            # append at start
            selected_words[index] = str(random.randint(0, 9)) + selected_words[index]

    # Insert symbols
    symbols_list = "~!@#$%^&*.:;"
    for _ in range(symbols):
        index = random.randint(0, len(selected_words) - 1)
        at_end = random.randint(0, 1)
        if at_end:
            selected_words[index] += random.choice(symbols_list)
        else:
            selected_words[index] = random.choice(symbols_list) + selected_words[index]

    password = "".join(selected_words)
    return password


password = generate_password(args.words, args.caps, args.numbers, args.symbols)


print(password)
