#!/usr/bin/env python3

import time
from multiprocessing import Pool, cpu_count


def compare_pair(args):
    a, b = args
    if a > b:
        return b, a
    return a, b


def bubble_sort_parallel_pool(arr, workers=None):
    n = len(arr)
    if workers is None:
        workers = cpu_count()

    with Pool(processes=workers) as pool:
        for _ in range(n):
            even_pairs = [(arr[i], arr[i + 1]) for i in range(0, n - 1, 2)]
            even_results = pool.map(compare_pair, even_pairs)
            for k, i in enumerate(range(0, n - 1, 2)):
                arr[i], arr[i + 1] = even_results[k]

            odd_pairs = [(arr[i], arr[i + 1]) for i in range(1, n - 1, 2)]
            odd_results = pool.map(compare_pair, odd_pairs)
            for k, i in enumerate(range(1, n - 1, 2)):
                arr[i], arr[i + 1] = odd_results[k]

    return arr


if __name__ == "__main__":
    with open("random.txt", "r", encoding="ascii") as f:
        data = [int(x) for x in f.read().strip().split(",") if x]

    start = time.perf_counter()
    sorted_data = bubble_sort_parallel_pool(data)
    elapsed = time.perf_counter() - start

    print(sorted_data[:20])
    print(f"Time taken: {elapsed:.6f} seconds")
