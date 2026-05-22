# def calculate_mean(numbers):
#     return sum(numbers) / len(numbers)


# numbers = [10, 20, 30, 40, 50]

# mean = calculate_mean(numbers)

# print("Mean:", mean)


def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count("G") + dna_sequence.count("C")
    return (gc_count / len(dna_sequence)) * 100


dna_sequence = "ATGCGCTA"

gc_content = calculate_gc_content(dna_sequence)

print("GC Content:", gc_content)