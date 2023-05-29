# Bài 1: Counting DNA Nucleotides
from Bio.Seq import Seq
dna = Seq("GCTTACAATCCAGCCCTAGCCCCTGGCCGATTCGGCGCTACGGTATCATGCGAATGCACTTTCGTTTCTTGTCGCCGTCAAGGCCTTCCGTGCCGCTGCCCCAGTCCTCCTGCGCCGTAGATCTGACGAGTTATATTTCCTTACCCTGTCGGCATATTGAGCGCGGAACAGTATTTACATTAGTGATCGGTCTCATCTGCGGTTGAAGATCGCATAGATGGGTCAAACCCACCTGACGACGGGGCGGAGCACTTACTTCCATTTGCAAGATTACACTTTAGCGGAGCCTCTGAAGGGAGCAAGGGCAGCGGGTAACTGCCCCCCTCGGCAAGAAATAGTCAAATTGCAGGCTACAGGAGGAACTATCACTCCAGAGTCACCACCGGAGGTGCATGCGAGGATCACGGGTGCTATACCTAGGCGGTCACCGCTAGATGTACAACTCTACGCAAAATCAATTCGGATGTGGCAGCTGCAAGCCCAATTGTTTGCGGACGCACAAAAATGACTGGAAGTGGCGACTATGCTGCGTTAGTCGAGTATGATACGCATCTCCTGTCTGGCTTAGGGATCACGACCTATTCTCCGAGAACCCAGAAGCTGGAGTAACTACTTAAGCAAATCACGAAAGTGAACGCATAGACTGTTCGTGAAGTAGTAAAAACTAAATCCGGACGAACTAACAGCGGTGGGAACTAACACTATGTGCCACACAGTCTGGCGAACGCACTTACGCATGGGTGGAATTATCGTCCGCTATGCGGAGTGGTATCGTATTAAGACAGGGACGGAATAGTCCCTTTAGCTCCCGAGTAGAACTCGGGCAGAATTGTTCTCGTG")
print(dna.count("A"), dna.count("C"), dna.count("G"), dna.count("T"))


# Bài 2: Transcribing DNA into RNA
from Bio.Seq import Seq
file = open("BioPython/2_rosalind_rna.txt","r")
rna = Seq(file.read())
print(rna.transcribe())


# Bài 3: Complementing a Strand of DNA
from Bio.Seq import Seq
file = open("BioPython/3_rosalind_revc.txt","r")
dna = Seq(file.read())
print(dna.reverse_complement())


# Bài 5: Computing GC Content
# Cách đổi từ file text (txt) sang file fasta: 
# Đường dẫn tới file văn bản đầu vào và file fasta đầu ra
input_file = "BioPython/5_rosalind_gc.txt"
output_file = "sequences.fasta"

# Mở file văn bản đầu vào và file fasta đầu ra
with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    # Đọc từng dòng trong file văn bản
    for line in f_in:
        # Nếu dòng bắt đầu bằng ký tự ">", thì đó là tên của một sequence
        if line.startswith(">"):
            # Ghi tên sequence ra file fasta với định dạng fasta
            f_out.write(line)
        # Nếu không, thì đó là chuỗi nucleotide của sequence
        else:
            # Ghi chuỗi nucleotide ra file fasta với định dạng fasta, mỗi dòng tối đa 80 ký tự
            f_out.write(line.strip() + "\n")
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import numpy as np
a = []
b = []
for seq in SeqIO.parse("sequences.fasta","fasta"):
    gc_content = gc_fraction(seq)
    a.append(seq.id)
    b.append(gc_content)
c = np.array(a)
d = np.array(b)
print(c,d)
print(c[d == max(d)][0], max(d)*100, sep = "\n")

from Bio import SeqIO
dna = SeqIO.read("BioPython/16S.fasta","fasta")
print(dna.name)


# Bài 6: Xác định điểm đột biến giữa 2 trình tự cùng độ dài
from Bio.Seq import Seq
file = open("BioPython/6_rosalind_hamm.txt","r")
array = file.read().split()
print(array)
dna1 = Seq(array[0])
dna2 = Seq(array[1])
dif = 0
for x,y in zip(dna1,dna2):
    if x!=y:
        dif += 1
print(dif)



# Bài 8: Translating RNA into Protein
from Bio.Seq import Seq
file = open("BioPython/8_rosalind_prot.txt","r")
rna = Seq(file.read())
print(rna.translate())



# Bài 9: Finding a Motif in DNA
from Bio.Seq import Seq
file = open("BioPython/9_rosalind_subs.txt")
array = file.read().split()
print(array)
string = array[0]
motif = array[1]

def findstr(string,substring):
    ket_qua = []
    vi_tri = 0
    while True:
        index = string.find(substring,vi_tri)
        if index == -1:
            break        
        ket_qua.append(index + 1)
        vi_tri = index + 1
    return ket_qua
x = findstr(string,motif)
print(*x,sep = " ")