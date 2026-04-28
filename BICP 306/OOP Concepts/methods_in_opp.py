class Gene:
      
      total_genes=0

      def __init__(self, name, sequence):
         self.name = name
         self.sequence = sequence
         Gene.total_genes += 1
         
      def length(self):
         return len(self.sequence)
   
      def gc_content(self):
         gc_count = self.sequence.count('G') + self.sequence.count('C')
         return gc_count / len(self.sequence) * 100
      
      @classmethod
      def get_total_genes(cls):
         return cls.total_genes
      
      @staticmethod
      def is_valid_sequence(seq):
          return all(base in "ATGC" for base in seq)
      


g1 = Gene("BRCA1", "ATGCGTACGTAGCTAG")
print(g1.length())
print(Gene.get_total_genes())
print(Gene.is_valid_sequence("ATGCGTACGTAGCTAG"))