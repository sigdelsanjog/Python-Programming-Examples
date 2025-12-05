from readers import FASTAReader
from validators import DNAValidator
from analyzers import GCContentCalculator


def main():
    fasta_data = """>Example
    ACGTGCGTACGT"""

    reader = FASTAReader()
    validator = DNAValidator()
    gc_calc = GCContentCalculator()

    seq = reader.read(fasta_data)
    validator.validate(seq)
    gc = gc_calc.compute(seq)

    print("Sequence:", seq)
    print("GC Content:", gc * 100)


if __name__ == "__main__":
    main()
