import random
import time
from multiprocessing import Pool, cpu_count

LENGTH = 1000000000

def generate_sequence_sequential():
    """Generate DNA sequence sequentially"""
    bases = ['A', 'T', 'G', 'C']
    start = time.time()
    
    dna = ''.join(random.choice(bases) for _ in range(LENGTH))
    
    end = time.time()
    time_taken = end - start
    
    print("Sequential generation completed")
    print(f"Time taken: {time_taken:.6f} seconds")
    print("First 100 bases:")
    print(dna[:100])
    print()
    
    return dna


def generate_chunk(args):
    """Generate a chunk of DNA sequence (for parallel processing)"""
    chunk_size, chunk_id = args
    bases = ['A', 'T', 'G', 'C']
    return ''.join(random.choice(bases) for _ in range(chunk_size))


def generate_sequence_parallel():
    """Generate DNA sequence in parallel using multiple processes"""
    bases = ['A', 'T', 'G', 'C']
    num_processes = cpu_count()
    chunk_size = LENGTH // num_processes
    
    start = time.time()
    
    # Create tasks for each process
    tasks = [(chunk_size, i) for i in range(num_processes)]
    
    # Add remainder to last chunk
    tasks[-1] = (chunk_size + LENGTH % num_processes, num_processes - 1)
    
    # Use multiprocessing pool to generate chunks in parallel
    with Pool(processes=num_processes) as pool:
        chunks = pool.map(generate_chunk, tasks)
    
    dna = ''.join(chunks)
    
    end = time.time()
    time_taken = end - start
    
    print("Parallel generation completed")
    print(f"Time taken: {time_taken:.6f} seconds")
    print(f"Number of processes used: {num_processes}")
    print("First 100 bases:")
    print(dna[:100])
    print()
    
    return dna


if __name__ == '__main__':
    print("=" * 50)
    print("DNA Sequence Generator - Sequential vs Parallel")
    print("=" * 50)
    print(f"Length: {LENGTH}\n")
    
    # Sequential execution
    print("--- SEQUENTIAL EXECUTION ---")
    dna_seq = generate_sequence_sequential()
    
    # Parallel execution
    print("--- PARALLEL EXECUTION ---")
    dna_par = generate_sequence_parallel()
    
    # Verify both sequences have the same length
    print("=" * 50)
    print(f"Sequential DNA length: {len(dna_seq)}")
    print(f"Parallel DNA length: {len(dna_par)}")
    print("=" * 50)


# BICP 406::python3 dna_sequence_generator.py
# ==================================================
# DNA Sequence Generator - Sequential vs Parallel
# ==================================================
# Length: 10000000

# --- SEQUENTIAL EXECUTION ---
# Sequential generation completed
# Time taken: 5.568213 seconds
# First 100 bases:
# ACCTGCGACATAGACCCGTCGAGGTGAGTTCCGGCATGCCGGTCAGACATATCGCTACCCGGGAATCAATCTTCGACGTGATAGACTGCCCCCCCGTCAG

# --- PARALLEL EXECUTION ---
# Parallel generation completed
# Time taken: 1.213883 seconds
# Number of processes used: 12
# First 100 bases:
# AGCATACAACAATCATGAAGAGACGGGTACGCGGCCGGAACTGTACGGAATGGCATGCGACTATGGAGTAGGGAGTAGTGCTGAGCTGATGATCGTAGTT

# ==================================================
# Sequential DNA length: 10000000
# Parallel DNA length: 10000000
# ==================================================