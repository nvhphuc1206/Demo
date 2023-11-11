# Hàm để tìm chuỗi trong chuỗi:
string1 = "Hello, World!, Hello, Hi, Hello "
string2 = "Hello"

index = string1.find(string2)
print(index)
if index != -1:
    print(f"Chuỗi '{string2}' tồn tại trong chuỗi '{string1}' tại vị trí {index}")
else:
    print(f"Chuỗi '{string2}' không tồn tại trong chuỗi '{string1}'")


string1 = "Tu Ly, Uy Vu, Hoang Nam, Phuong Thy"
string2 = "Tu Ly"

index = string1.find(string2,1)
print(index)


def findstr(string,substring):
    ket_qua = []
    vi_tri = 0
    while True:
        index = string.find(substring,vi_tri)
        if index == -1:
            break        
        ket_qua.append(index)
        vi_tri = index + 1
    return ket_qua

lab_hiuq7 = "TL,UV,TB,BT,TL"
nguoi_can_tim = "TL"
x = findstr(lab_hiuq7,nguoi_can_tim)
print(x)

x = [["a","b","a","c"],["a","d","e"]]
y = set(x)
print(y)
print(max(x))


import pandas as pd
import numpy as np
x = {"A":[0,1,3,4,5,6],
     "T":[3,4,5,6,7,8]}
y = pd.DataFrame()
print(y)



a = "abcdef"
b = "b"
x = a.find(b,0)
print(x)

x = {"Tuly":[]}
x["Tuly"].append("Khung")
print(x)
print("__"*50)
x["Tuly"].append("qua")
print(x)
print("__"*50)
y = iter(x)
print(y)
print("__"*50)
start_node = next(iter(x))
print(start_node)
print("__"*50)
start_node = next(iter(x))
print(start_node)
print("__"*50)
next_node = x[start_node].pop(0)
print(next_node)
print("__"*50)




x = {"a":[{"e":1,"f":2,"k":3}],
     "b":[{"h":4,"g":5,"e":6}]}
print(x)
for i in range(len(x["a"])):
    print(x["a"])
    for k in [x["a"][i]]:
        print(k)

from Bio.Seq import Seq
dna = Seq("ATGGAAAAATTTAAAAAGAAACCAAAAAGTATAAAACGATCGCATCAAAAAACAATCTTAAAGCGTCCTTTATGGCTTGCACCTTTACTGATCGGTGGGTTTGCTAGTGGGGTGTATGCTGATGGAACAGATATTTTTGGGCTTAGTTGA")
print(dna.reverse_complement())

print(len("TCAACTAAGCCCAAAAATATCTGTTCCATCAGCATACACCCCACTAGCAAACCCACCGATCAGTAAAGGTGCAAGCCATAAAGGACGCTTTAAGATTGTTTTTTGATGCGATCGTTTTATACTTTTTGGTTTCTTTTTAAATTTTTCCAT"))
print(len("ATGGAAAAATTTAAAAAGAAACCAAAAAGTATAAAACGATCGCATCAAAAAACAATCTTAAAGCGTCCTTTATGGCTTGCACCTTTACTGATCGGTGGGTTTGCTAGTGGGGTGTATGCTGATGGAACAGATATTTTTGGGCTTAGTTGA"))

print(len(""))