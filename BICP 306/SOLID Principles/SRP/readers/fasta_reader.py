class FASTAReader:
    def read(self, fasta_string):
        lines = fasta_string.splitlines()
        seq = "".join(
            line.strip() for line in lines 
            if not line.startswith(">")
        )
        return seq
