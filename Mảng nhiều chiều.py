# Cách tạo mảng nhiều chiều từ bàn phím:
import numpy as np
a = []
row = int(input("Nhap so hang :"))
column = int(input("Nhap so cot :"))
for i in range(row):
    z = []
    for k in range(column):
        x = int(input("Nhap so o hang " + str(i+1) +" cot " + str(k+1) +" : "))
        z.append(x)
    a.append(z)
print(a)

# Cách viết chương trình tìm số lớn nhất của mảng 2 chiều:
a = [[1 , 2 , 3] , [4 , 5 , 6]]
ROW = len ( a )
COL = len ( a [0])
max1 = a [0][0]
for i in range (0 , ROW ) :
    for j in range (0 , COL ) :
        if a [ i ][ j ] > max1 :
            max1 = a [ i ][ j ]
print (" Phan tu lon nhat la: ", max1 )
import numpy as np
b = np.array(a)
print("Phan tu lon nhat la : ", np.max(b))

# Cách duyệt mảng nhiều chiều: 
a = [[1 , 2 , 3] , [4 , 5 , 6]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print("Phan tu o hang",i+1,"cot",j+1,"la",a[i][j])

