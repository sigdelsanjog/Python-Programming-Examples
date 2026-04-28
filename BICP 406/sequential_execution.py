import time

def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

def gc_content_sequential(sequences):
    start = time.time()
    results = []
    for seq in sequences:
        results.append(gc_content(seq))
    end = time.time()
    
    return results, end - start