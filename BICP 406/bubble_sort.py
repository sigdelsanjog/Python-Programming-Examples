#!/usr/bin/env python3
"""Regular bubble sort example."""

from __future__ import annotations

import time
from typing import List


def bubble_sort(data: List[int]) -> List[int]:
    arr = data[:]  # Keep the input unchanged.
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    with open("random.txt", "r", encoding="ascii") as f:
        numbers = [int(x) for x in f.read().strip().split(",") if x]

    start = time.perf_counter()
    sorted_numbers = bubble_sort(numbers)
    elapsed = time.perf_counter() - start
    print(sorted_numbers[:20])
    print(f"Time taken: {elapsed:.6f} seconds")
