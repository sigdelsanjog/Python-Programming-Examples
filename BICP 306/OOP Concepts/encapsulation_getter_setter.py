class DNASequence:

    def __init__(self, sequence):
        self.__sequence = sequence

    def set_sequence(self, sequence):

        valid = {"A", "T", "G", "C"}

        for base in sequence:
            if base not in valid:
                print("Invalid DNA sequence")
                return

        self.__sequence = sequence
        print("Valid DNA sequence stored successfully")

    def get_sequence(self):
        return self.__sequence
    
    

dna = DNASequence("ATGC")

dna.set_sequence("ATGCGGCCGGCG")