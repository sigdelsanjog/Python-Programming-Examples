class DNAValidator:
    VALID_BASES = set("ACGT")

    def validate(self, seq):
        if not set(seq).issubset(self.VALID_BASES):
            raise ValueError("Invalid DNA sequence.")
        return True
