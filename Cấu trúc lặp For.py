# Cấu trúc lặp FOR
# VD1
x = [1,5,3,10]
y = len(x)
print("Kich thuoc cua list la: ", y)
for i in range (0,y):
     print("Phan tu thu", i+1,"la: ", x[i])
# VD2
z = ["a","b","c","d"]
q = len(z)
print("Kich thuoc cua list la: ", q)
for i in range (0,q):
     print("Phan tu thu", i+1,"la: ", z[i])


# Cấu trúc for với hàm bộ đếm enumerate để print kq theo thứ tự: enumerater("biến", số bắt đầu)
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas,1) :
    print("room " + str(index) + ": " + str(area))


# Tạo cấu trúc lặp nhập từ bàn phím: 
a =[]
N = int(input("Nhap kich thuoc mang:  "))
for i in range (0,N):
     temp = int(input("Nhap so nguyen thu " + str(i+1) + "  "))
     a.append(temp)
print("List bao gồm " ,N,  " phan tu: ", a)


# Tạo chương trình xác định số p/tử lẹ trong mảng: 
l = len(a)
le = 0 
for e in range (0,l):
     if a[e] % 2 != 0:
          le = le + 1
print("So phan tu le trong a la :   ", le)

# Tinh tong , tim so chan , le
tong = chan = le = 0
for i in range (0 , N ) :
     tong = tong + a [ i ]
if a [ i ] % 2 == 0:
     chan = chan + 1
else :
     le = le + 1

# Tim min , max
max1 = min1 = a [0]
for i in range (1 , N ) :
     if a [ i ] < min1 :
          min1 = a [ i ]
if a [ i ] > max1 :
     max1 = a [ i ]

print ( tong , chan , le , max1 , min1 )

