# Mục 7: Sequence Input/Output

# 1. Parsing or reading sequence :
from Bio import SeqIO
file =  SeqIO.parse("BioPython/sequence.fasta","fasta")
dna1 = next(file)
print(dna1)
print(dna1.id)

from Bio import SeqIO
file =  SeqIO.parse("BioPython/sequence.fasta","fasta")
list = list(file)
print(list)
print("_"*50)
print(list[0].id)
for i in list:
    print("_"*50)
    print(i)
from Bio import SeqIO
file = SeqIO.parse("BioPython/ls_orchid.fasta","fasta")
sum_seq = list(file)
print(sum_seq[-1])

from Bio import SeqIO
id_sum =  [x.id for x in SeqIO.parse("BioPython/sequence.fasta","fasta")]
print(id_sum)


# 2. Extracting data 
# Đối với file genbank có các ghi chú như id, sequence, annotations, ...
from Bio import SeqIO
all_species = [x.annotations['organism'] for x in SeqIO.parse("BioPython/ls_orchid.gbk","genbank")]
print(all_species)

# Đối với file FASTA chỉ có descrition và sequence 
from Bio import SeqIO
all_species = [x.description.split()[1] for x in SeqIO.parse("BioPython/ls_orchid.fasta","fasta")]
print(all_species)



# 3. Modifying data: 
from Bio import SeqIO
record_iterator = SeqIO.parse("BioPython/sequence.fasta", "fasta")
first_record = next(record_iterator)
first_record.id = "new_id"
first_record.description = first_record.id + " " + "desired new description"
print(first_record.format("fasta")[:200])
print("_"*80)
print(first_record)


# 4. Writing seq and converting seq format:
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
sequence = SeqIO.read("BioPython/16S.fasta","fasta").seq
dna = SeqRecord(sequence, id= "NC_000913.3:4166659-4168200", name= "NC_000913.3:4166659-4168200", 
                description= "NC_000913.3:4166659-4168200 Escherichia coli str. K-12 substr. MG1655, complete genome")
print(dna)
print("_"*100)

SeqIO.write(dna,"fasta_ex","fasta")
x = SeqIO.read("fasta_ex.fasta","fasta")
print(x)

# Hoặc 
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

sequence = SeqIO.read("BioPython/16S.fasta","fasta").seq
dna = SeqRecord(sequence, id="NC_000913.3:4166659-4168200", name="NC_000913.3:4166659-4168200",
                description="NC_000913.3:4166659-4168200 Escherichia coli str. K-12 substr. MG1655, complete genome")
record_list = [dna]  # Tạo một danh sách chứa một SeqRecord

# Ghi danh sách SeqRecord ra file fasta
with open("fasta_ex.fasta", "w") as handle:
    SeqIO.write(record_list, handle, "fasta")

# Đọc SeqRecord từ file fasta và in ra màn hình
x = SeqIO.read("fasta_ex.fasta", "fasta")
print(x)



# Để đổi format file qua lại ta sử dụng hàm .convert: 
from Bio import SeqIO
SeqIO.convert("input.gbk","genbank","output.fasta","fasta")
y = SeqIO.read("output.fasta","fasta")
print(y)



