import time
import random
from multiprocessing import Pool

def make_seq(n):
    return ''.join(random.choice("ATGC") for _ in range(n))

sequences = [make_seq(10000000) for _ in range(20)]

def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

start = time.time()

with Pool() as pool:
    results = pool.map(gc_content, sequences)

end = time.time()

print("Parallel Results:", results[:5])
print("Time:", end - start)