#!/usr/bin/env python3
"""
main.py: první projekt do IT gymnázia

author: Jan Zeithaml
email: 1256@student.itgymnazium.cz
"""

import string

TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

passwords = {
        "bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123",
        }

name = input("Username: ")
password = input("Password: ")

if name not in passwords or passwords[name] != password:
    print("Incorrect username or password")
    exit(1)

print(f"Welcome {name}")

try:
    prompt = f"Which text do you want to ananalyze [1-{len(TEXTS)}]? "
    text_choice_string = input(prompt)
    text_choice = int(text_choice_string)
except ValueError:
    print(f"{text_choice_string} is not a number")
    exit(1)

if text_choice < 1 or text_choice > len(TEXTS):
    print(f"Text number must be between 1 and {len(TEXTS)}")
    exit(1)

text = TEXTS[text_choice-1]
words = text.split()

capitalized_count = 0
caps_lock_count = 0
lowercase_count = 0
number_count = 0
acc = 0
len_counts = {}
biggest_len = 0
for word in words:
    word = word.translate(str.maketrans("", "", string.punctuation))
    if word.isupper(): caps_lock_count += 1
    if word.islower(): lowercase_count += 1
    if word[0].isupper() and word[1:].islower():
        capitalized_count += 1
    try:
        integer = int(word)
        number_count += 1
        acc += integer
    except ValueError:
        pass
    biggest_len = max(biggest_len, len(word))
    if len(word) not in len_counts:
        len_counts[len(word)] = 1
    else:
        len_counts[len(word)] += 1

print(f"Number of words: {len(words)}")
print(f"Number of capitalized words: {capitalized_count}")
print(f"Number of caps locked words: {caps_lock_count}")
print(f"Number of lowercase words: {lowercase_count}")
print(f"Number of numbers: {number_count}")
print(f"Sum of all numbers: {acc}")
print("--------------------------")
print("LEN | OCCURENCES | NR.")
print("--------------------------")
max_width = max(len_counts.values())
for i in range(1, biggest_len+1):
    amount = len_counts.get(i, 0)
    len_formatted = str(i).rjust(3)
    bar = (amount * "*").ljust(max_width)
    print(f"{len_formatted} | {bar} | {amount}")
