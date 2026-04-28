import random
import time
from sequential_execution import gc_content_sequential
from parallel_execution import gc_content_parallel

def make_seq(n):
    return ''.join(random.choice("ATGC") for _ in range(n))

def main():
    sequences = [make_seq(10000000) for _ in range(20)]
    
    print("SEQUENTIAL EXECUTION")
    seq_results, seq_time = gc_content_sequential(sequences)

    for i, gc in enumerate(seq_results[-5:], len(seq_results) - 4):
        print(f"  Sequence {i}: {gc:.2f}%")
    print(f"Sequential Time: {seq_time:.6f}s")
    
    print("PARALLEL EXECUTION")
    par_results, par_time = gc_content_parallel(sequences)
    
    
    for i, gc in enumerate(par_results[-5:], len(par_results) - 4):
        print(f"  Sequence {i}: {gc:.2f}%")
    print(f"Parallel Time: {par_time:.6f}s")
    
    total_time = seq_time + par_time
    print(f"Sequential Time: {seq_time:.6f}s")
    print(f"Parallel Time: {par_time:.6f}s")
    print(f"Total Time: {total_time:.6f}s")
    speedup = seq_time / par_time if par_time > 0 else 0
    print(f"Speedup: {speedup:.2f}x")

if __name__ == "__main__":
    main()
