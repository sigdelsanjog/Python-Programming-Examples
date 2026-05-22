# numbers = [10, 20, 31, 40, 50]

# total = 0

# for number in numbers:
#     total = total + number

# mean = total / len(numbers)

# print("Mean:", mean)



dna_sequence = "ATGCGCTA"

gc_count = 0

for base in dna_sequence:
    if base == "G" or base == "C":
        gc_count = gc_count + 1

gc_content = (gc_count / len(dna_sequence)) * 100

print("GC Content:", gc_content)