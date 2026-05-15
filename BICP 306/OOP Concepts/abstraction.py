from abc import ABC, abstractmethod


# =========================
# ABSTRACT BASE CLASS
# =========================
class SequenceAnalyzer(ABC):

    def __init__(self, sequence):
        self.sequence = sequence

    @abstractmethod
    def analyze(self):
        pass


# =========================
# CONCRETE CLASS 1
# GC CONTENT ANALYSIS
# =========================
class GCContentAnalyzer(SequenceAnalyzer):

    def analyze(self):
        gc_count = self.sequence.count("G") + self.sequence.count("C")
        length = len(self.sequence)

        gc_content = (gc_count / length) * 100

        print("GC Content Analysis")
        print(f"Sequence: {self.sequence}")
        print(f"GC Content: {gc_content:.2f}%")


# =========================
# CONCRETE CLASS 2
# DNA VALIDATION ANALYSIS
# =========================
class DNAValidator(SequenceAnalyzer):

    def analyze(self):
        valid_bases = {"A", "T", "G", "C"}

        for base in self.sequence:
            if base not in valid_bases:
                print("Invalid DNA Sequence detected")
                return

        print("DNA Sequence is VALID")


# =========================
# MAIN EXECUTION
# =========================
if __name__ == "__main__":

    # Example 1: GC Content
    seq1 = GCContentAnalyzer("ATGCGCGTAA")
    seq1.analyze()

    print("\n----------------------\n")

    # Example 2: Validation
    seq2 = DNAValidator("ATGCGCTA")
    seq2.analyze()

    print("\n----------------------\n")

    # Example 3: Invalid Sequence
    seq3 = DNAValidator("ATGBXZ")
    seq3.analyze()