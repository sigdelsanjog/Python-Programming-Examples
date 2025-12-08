# Base Strategy (Closed for modification)
class AnalysisStrategy:
    def compute(self, seq):
        raise NotImplementedError("Subclasses must implement compute()")


# ------------------------------
# Existing Strategies which is known to us(GC, AT)
# ------------------------------

class GCContent(AnalysisStrategy):
    def compute(self, seq):
        gc = seq.count("G") + seq.count("C")
        return gc / len(seq)


class ATContent(AnalysisStrategy):
    def compute(self, seq):
        at = seq.count("A") + seq.count("T")
        return at / len(seq)


# ------------------------------
# New Strategy: K-mer Counting
# (Extension without modifying old code)
# ------------------------------

class KmerCounter(AnalysisStrategy):
    def __init__(self, k=3):
        self.k = k

    def compute(self, seq):
        counts = {}
        for i in range(len(seq) - self.k + 1):
            kmer = seq[i:i+self.k]
            counts[kmer] = counts.get(kmer, 0) + 1
        return counts


# ------------------------------
# Orchestrate the classes such that you can be able to call any class necessary.
# SequenceAnalyzer (Closed for modification)
# Accepts ANY strategy
# ------------------------------

class SequenceAnalyzer:
    def __init__(self, strategy: AnalysisStrategy):
        self.strategy = strategy

    def run(self, seq):
        return self.strategy.compute(seq)


def main():
    seq = "ACGTACGTGCGT"

    print("Sequence:", seq)

    analyzer = SequenceAnalyzer(GCContent())
    print("GC Content:", analyzer.run(seq))

    analyzer = SequenceAnalyzer(ATContent())
    print("AT Content:", analyzer.run(seq))

    analyzer = SequenceAnalyzer(KmerCounter(k=2))
    print("2-mer Counts:", analyzer.run(seq))


if __name__ == "__main__":
    main()
