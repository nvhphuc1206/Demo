# Hàm cơ bản để tạo và tìm trình tự bổ sung, lặp đảo:
from Bio.Seq import Seq
my_seq = Seq("ATGCATGCCTGA")
print(my_seq)
print(my_seq[::-1])                   # Sử dụng toán tử index để tạo trình tự ngược chiểu 
print(my_seq.complement())            # Mạch bổ sung ngược chiều 
print(my_seq.reverse_complement())    # Mạch bổ sung cùng chiều
print(my_seq[1:3])

# Cách lấy trình tự từ file FASTA, GenBank:
from Bio import SeqIO
for sequence in SeqIO.parse("BioPython/16S.fasta","fasta"):
    print(sequence)
    print(sequence.id)
    print(repr(sequence.seq))
    print(len(sequence))

# Trình tự của dna cũng như giống data type strings:
from Bio.Seq import Seq
my_seq = Seq("GATCG")
for index, letter in enumerate(my_seq):
    print(index, letter)
print(my_seq[0])
print(my_seq[1])
print(len(my_seq))


# Cách tính %GC trong trình tự bằng hàm gc_fraction:
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(gc_fraction(my_seq))

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
for x in SeqIO.parse("BioPython/16S.fasta","fasta"):
    dna = x.seq 
print(gc_fraction(dna))


# Cắt đoạn trong 1 trình tự
from Bio.Seq import Seq
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq[4:12])
print(my_seq[0::3]) # Hàm 0bject[start:end:step] -> để lấy p/tử cách nhau theo khoảng xác định 
print(type(my_seq))



# Nối hoặc thêm trình tự: 
from Bio.Seq import Seq
seq1 = Seq("ACGT")
seq2 = Seq("AACCGG")
x = seq1 + seq2
y = seq1 + "CGCGCG"
print(x)
print(type(x))
print(y)
print(type(y))


# Sử dụng vòng lặp để nối nhiều trình tự:
from Bio.Seq import Seq
list = [Seq("ATGC"), Seq("GGCCAATT"), Seq("TGCAT")]
target_gene = Seq("")
for i in list:
    target_gene += i 
print(target_gene)


# Sử dụng hàm method .join để nối những trình tự mục tiêu bởi 1 trình tự lặp lại:
from Bio.Seq import Seq
list = [Seq("ATGC"), Seq("GGCCAATT"), Seq("TGCAT")]
linker = Seq("ATGC"*10)
print(linker.join(list))


# Transciption method: Thực chất là quá trình reverse_complement và thay đổi T -> U
from Bio.Seq import Seq
template = Seq("ATGC")
print(template.reverse_complement())
print(template.transcribe())
print(template.reverse_complement().transcribe())
# Phiên mã ngược: .back_transcribe()
from Bio.Seq import Seq
m_rna = Seq("AUGC")
dna = m_rna.back_transcribe()
print(dna)


# Translation method:
from Bio.Seq import Seq
m_rna = Seq("AUGCAUGCAUGCUAG")  
dna = Seq("ATGCATGCATGCTAG")
print(m_rna.translate())
print(dna.translate())
# Đối với những gene đặc biệt không sử dụng AUG làm start codon thì ta cần sử dụng bảng codon của loài đó để thực hiện dịch mã
from Bio.Seq import Seq
gene = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCAGCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGATAATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACATTATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCATAAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA")
protein = gene.translate(table="Bacterial", cds=True)
print(protein)

from Bio.Seq import Seq
m_rna = Seq("AUGCAUGCAUGCUAGAAGAAUCCGUGA") 
print(m_rna.translate())
print(m_rna.translate(to_stop=True))


from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation
seq = Seq("ACCGAGACGGCAAAGGCTAGCATAGGTATGAGACTTCCTTCCTGCCAGTGCTGAGGAACTGGGAGCCTAC")
feature = SeqFeature(SimpleLocation(0, 5, strand=1), type="gene")
print(feature.location)
print(feature.extract(seq))