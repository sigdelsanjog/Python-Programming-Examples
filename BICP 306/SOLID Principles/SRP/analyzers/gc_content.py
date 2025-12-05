class GCContentCalculator:
    def compute(self, seq):
        gc = seq.count("G") + seq.count("C")
        return gc / len(seq)
