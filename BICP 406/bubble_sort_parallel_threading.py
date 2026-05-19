#!/usr/bin/env python3

import time
from threading import Thread


def bubble_sort_parallel(arr):
    n = len(arr)

    for _ in range(n):
        threads = []
        for i in range(0, n - 1, 2):
            t = Thread(target=compare_swap, args=(arr, i, i + 1))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

        threads = []
        for i in range(1, n - 1, 2):
            t = Thread(target=compare_swap, args=(arr, i, i + 1))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

    return arr


def compare_swap(arr, i, j):
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    with open("random.txt", "r", encoding="ascii") as f:
        data = [int(x) for x in f.read().strip().split(",") if x]

    start = time.perf_counter()
    sorted_data = bubble_sort_parallel(data)
    elapsed = time.perf_counter() - start
    print(sorted_data[:20])
    print(f"Time taken: {elapsed:.6f} seconds")
