class DNASequence:

    def __init__(self, sequence):
        self.__sequence = sequence

    def get_sequence(self):
        return self.__sequence

    def get_length(self):
        return len(self.__sequence)


dna = DNASequence("ATGCGTAA")

print(dna.get_sequence())

print(dna.get_length())