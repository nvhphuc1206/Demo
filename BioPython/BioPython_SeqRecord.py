# SeqRecord không thể tạo trực tiếp từ trình tự mà phải thông qua Seq
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
dna = Seq("ATGC")
dna1 = SeqRecord(dna)
print(dna1.seq)
dna = Seq("ATGC")

# Cách tạo 1 SeqRecord 
from Bio.Seq import Seq
simple_seq = Seq("GATC")
from Bio.SeqRecord import SeqRecord
simple_seq_r = SeqRecord(simple_seq)
simple_seq_r.id = "AC12345"
simple_seq_r.description = "Made up sequence I wish I could write a paper about"
simple_seq_r.annotations["evidence"] = "None. I just made it up."
simple_seq_r.letter_annotations["phred_quality"] = [40, 40, 38, 30]
print(simple_seq_r.id)
print(simple_seq_r.description)
print(simple_seq_r.annotations)
print(simple_seq_r.letter_annotations["phred_quality"])
print(simple_seq_r)
# Hoặc có thể thêm tất cả vào trong hàm SeqRecord
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
sequence = Seq("ATGC")
dna = SeqRecord(sequence,id="AC12345", description="Made up sequence I wish I could write a paper about", annotations={"evidence": "None. I just made it up."}, letter_annotations= {"phred_quality": [40, 40, 38, 30]})
print(dna)

# Tạo 1 SeqRecord từ file FASTA:
from Bio import SeqIO
record = SeqIO.read("BioPython/16S.fasta", "fasta")
print(record)
print("_"*80)
print(record.format("fasta"))
print("_"*80)
print(record.id)
print("_"*80)
print(record.description)
print("_"*80)
print(record.dbxrefs)
print("_"*80)
print(len(record.seq))


# Tạo 1 SeqRecord từ 1 file GenBank: 
from Bio import SeqIO
record = SeqIO.read("BioPython\Salmonella 16S ribosomal RNA.gb","genbank")
print(record)
print("_"*80)
print(record.format("genbank"))
print("_"*80)
print(record.seq)
print("_"*80)
print(record.annotations)
print("_"*80)
print(record.annotations["molecule_type"])
print("_"*80)
print(record.features[0])
print("_"*80)
print(record.features[1])


