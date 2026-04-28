import time
from multiprocessing import Pool

def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

def gc_content_parallel(sequences):
    start = time.time()
    with Pool() as pool:
        results = pool.map(gc_content, sequences)
    end = time.time()
    
    return results, end - start