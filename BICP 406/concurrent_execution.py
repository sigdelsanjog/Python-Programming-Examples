import time
import threading
import random
from typing import List

def generate_dna_sequence(length: int, sequence_id: int) -> str:
    """Generate a random ATGC sequence of specified length"""
    nucleotides = ['A', 'T', 'G', 'C']
    sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    return sequence

def process_sequence_thread(sequence_id: int, sequence: str, results: List):
    """Process a DNA sequence in a thread and calculate GC percentage"""
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percentage = (gc_count / len(sequence)) * 100
    results.append({
        "id": sequence_id,
        "sequence": sequence[:50] + ("..." if len(sequence) > 50 else ""),  # Show first 50 chars
        "length": len(sequence),
        "gc_count": gc_count,
        "gc_percentage": gc_percentage
    })

def concurrent_execution_threading(num_threads: int, sequence_length: int):
    """Process multiple sequences concurrently using threading"""
    start = time.time()
    results = []
    threads = []
    
    # Generate sequences and create threads
    sequences = [generate_dna_sequence(sequence_length, i) for i in range(num_threads)]
    
    for i, sequence in enumerate(sequences):
        thread = threading.Thread(target=process_sequence_thread, args=(i, sequence, results))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    end = time.time()
    return results, end - start


# ============================================
# Main Execution
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("CONCURRENT DNA SEQUENCE PROCESSING - Threading Approach")
    print("=" * 70)
    
    # Get user input
    while True:
        try:
            num_threads = int(input("\nEnter number of sequences (threads): "))
            if num_threads < 1:
                print("Please enter a number >= 1")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    while True:
        try:
            sequence_length = int(input("Enter sequence length (nucleotides): "))
            if sequence_length < 1:
                print("Please enter a number >= 1")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    print(f"\nGenerating {num_threads} sequences of length {sequence_length}...")
    results_threading, elapsed_time = concurrent_execution_threading(num_threads, sequence_length)
    
    print(f"\n✓ Processed {num_threads} sequences in {elapsed_time:.4f} seconds")
    print("-" * 70)
    
    # Sort results by ID for consistent display
    results_threading.sort(key=lambda x: x['id'])
    for result in results_threading:
        print(f"Sequence {result['id']:3d} | {result['sequence']:50s} | "
              f"Length: {result['length']:5d} | GC: {result['gc_count']:4d} ({result['gc_percentage']:5.2f}%)")
    
    # Calculate average GC percentage
    avg_gc = sum(r['gc_percentage'] for r in results_threading) / len(results_threading)
    print("-" * 70)
    print(f"Average GC percentage: {avg_gc:.2f}%")
