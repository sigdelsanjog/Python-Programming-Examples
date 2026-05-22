def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


def calculate_at_content(sequence):
    at_count = sequence.count("A") + sequence.count("T")
    return (at_count / len(sequence)) * 100


def create_analysis_result(sequence):
    return {
        "sequence": sequence,
        "gc_content": calculate_gc_content(sequence),
        "at_content": calculate_at_content(sequence),
    }


def display_result(result):
    print("Functional DNA Sequence Analysis")
    print("---------------------------")
    print(f"DNA Sequence: {result['sequence']}")
    print(f"GC Content: {result['gc_content']:.2f}%")
    print(f"AT Content: {result['at_content']:.2f}%")


if __name__ == "__main__":
    dna_sequence = "ATGCGCTA"
    display_result(create_analysis_result(dna_sequence))
