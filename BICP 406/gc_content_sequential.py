import time
import random

def make_seq(n):
    return ''.join(random.choice("ATGC") for _ in range(n))

sequences = [make_seq(10000000) for _ in range(20)]

# print("First 5 Sequences Generated:", sequences[:5])
# print()

def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

start = time.time()

results = []
for seq in sequences:
    results.append(gc_content(seq))

end = time.time()

print("Sequence with GC Content:")
# for seq, gc in zip(sequences, results):
#     print(f"  {seq} -> {gc:.2f}%")

for i in range(len(sequences)):
    print(sequences[i], results[i])

print("Time:", end - start)