class FASTAReader:
    """Handles reading DNA sequences from FASTA files."""
    def read(self, filename):
        with open(filename) as f:
            lines = f.readlines()
        # Remove header if present
        seq = "".join(line.strip() for line in lines if not line.startswith(">"))
        return seq


class DNAValidator:
    """Responsible only for validating DNA sequences."""
    VALID_BASES = set("ACGT")

    def validate(self, seq):
        if not set(seq).issubset(self.VALID_BASES):
            raise ValueError("Sequence contains invalid nucleotides.")
        return True


class GCContentCalculator:
    """Computes GC content only."""
    def compute(self, seq):
        gc_count = seq.count("G") + seq.count("C")
        return gc_count / len(seq)


def main():
    reader = FASTAReader()
    validator = DNAValidator()
    gc_calc = GCContentCalculator()

    seq = reader.read("sampleDNA.fasta")
    print("Sequence read:", seq)
    
    validator.validate(seq)
    
    gc_content = gc_calc.compute(seq)
    print("GC Content:", gc_content)


if __name__ == "__main__":
    main()
