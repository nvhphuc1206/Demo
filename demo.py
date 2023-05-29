
x = [1,2,3,4]
import numpy as np
y = np.array(x)
z = np.array([5,6,7,8])
# Cách thêm phần tử vào mảng trong Numpy (.insert(đối tượng đc chèn, vị trí chèn, phần tử chèn vào))
y = np.insert(y,4,z)
print(y)
z= np.insert()

fam = [1,2,3,4]
for i,so in enumerate(fam):
    print(i, " va ", so)

fam = [1,2,3,4]
z = enumerate(fam)
print(max(fam))


print("2","b",sep = "\n") # Cách in kết quả xuống dòng



# Toán tử index để lấy từng p/tử với khoảng cách nhất định:
x = "Hoang Phuc"
print(x[::3])


# Cách đọc file txt: sử dụng hàm open() để mở và hàm read() để đọc
from Bio.Seq import Seq
file = open("BioPython/2_rosalind_rna.txt","r")
rna = Seq(file.read())
print(rna)


import numpy as np
a = np.array([1,2,3,4,5])
b = np.array(["a","b","c","d","e"])
print(b[a==max(a)][0])
print(b[0])


# Cách rút trích những phần tử trong list không kề nhau: 
fam = [1,2,3,4,5,6,7,8,9,10]
x = [fam[i] for i in [0,3,4,7,9]]
print(x)
y = fam[0:3]
print(y)

import os
print(os.getcwd())