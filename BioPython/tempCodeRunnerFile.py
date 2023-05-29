from Bio import Align
from Bio.Seq import Seq
aligner = Align.PairwiseAligner()
aligner.match_score = 1
x = Seq("ATGCAAA")
y = Seq("AAAATGC")
print(aligner.score(x,y))
aligner.mode = "local"
alignment = aligner.align(x,y)
for i in alignment:
    print(i)