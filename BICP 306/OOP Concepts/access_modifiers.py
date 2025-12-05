class DNASequence:
    def __init__(self, name, sequence):
        self.name = name              # public attribute
        self._sequence = sequence     # protected attribute
        self.__gc_content = None      # private attribute

    # ---------- Public Method ----------
    def analyze(self):
        print(f"Analyzing sequence: {self.name}")
        gc = self.__calculate_gc_content()  # private method
        self.__gc_content = gc
        print(f"GC Content: {gc:.2f}%")

    # ---------- Protected Method ----------
    def _transcribe(self):
        """Protected: can be used in subclasses"""
        return self._sequence.replace("T", "U")

    # ---------- Private Method ----------
    def __calculate_gc_content(self):
        """Private: should not be called directly outside"""
        g = self._sequence.count("G")
        c = self._sequence.count("C")
        return ((g + c) / len(self._sequence)) * 100


# create object
seq1 = DNASequence("BRCA1", "ATGCGTACGATCGATCGTAGCTAG")

# --- Access public attribute and method ---
print(seq1.name)         # ✅ Public attribute
seq1.analyze()           # ✅ Public method
seq1._transcribe()        # ❌ Should not be called directly
# seq1.__calculate_gc_content()  # ❌ Error

# --- Access protected attribute/method ---
print(seq1._sequence)    # ⚠️ Works, but should be used carefully

print(seq1._transcribe())# ⚠️ Works, but intended for subclass use

# --- Access private attribute/method ---
# print(seq1.__gc_content)       # ❌ Error
# print(seq1.__calculate_gc_content())  # ❌ Error
print(seq1._DNASequence__gc_content)    # ⚠️ Forced access (not recommended)
