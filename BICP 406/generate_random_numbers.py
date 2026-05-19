#!/usr/bin/env python3

import random

COUNT = 50000
MIN_VALUE = 1
MAX_VALUE = 1000000
OUTPUT_FILE = "random.txt"


numbers = [str(random.randint(MIN_VALUE, MAX_VALUE)) for _ in range(COUNT)]

with open(OUTPUT_FILE, "w", encoding="ascii") as f:
    f.write(",".join(numbers))
