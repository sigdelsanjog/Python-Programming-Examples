# Pure Function Example
# Topic: Calculating GC content in a DNA sequence

analysis_count = 0


def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


def calculate_gc_content_impure(sequence):
    global analysis_count

    analysis_count = analysis_count + 1

    gc_count = sequence.count("G") + sequence.count("C")
    gc_content = (gc_count / len(sequence)) * 100

    print("Impure function was called")
    print(f"Analysis Count: {analysis_count}")

    return gc_content


if __name__ == "__main__":
    dna_sequence = "ATGCGCTA"

    gc_content = calculate_gc_content(dna_sequence)
    impure_gc_content = calculate_gc_content_impure(dna_sequence)

    print("Pure Function DNA Analysis")
    print("---------------------------")
    print(f"DNA Sequence: {dna_sequence}")
    print(f"GC Content: {gc_content:.2f}%")

    print("\nImpure Function DNA Analysis")
    print("---------------------------")
    print(f"DNA Sequence: {dna_sequence}")
    print(f"GC Content: {impure_gc_content:.2f}%")

    print("---------------------------")
    impure_gc_content = calculate_gc_content_impure(dna_sequence)
    print(f"GC Content: {impure_gc_content:.2f}%")

    print("---------------------------")
    gc_content = calculate_gc_content(dna_sequence)
    print(f"GC Content: {gc_content:.2f}%")
