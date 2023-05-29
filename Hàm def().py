# Tạo 1 hàm tính tổng : 
def cong(x,y):
    return x + y 
a = cong(5,6)
print(a)

# Tạo 1 hàm tính tổng nhập từ bàn phím :
def cong(x,y):
    return x + y
x = int(input("Nhap so thu nhat : "))
y = int(input("Nhap so thu hai : "))
a = cong(x,y)
print(a)

# Tạo hàm giải phương trình bậc 1: ax + b = 0 (Đây là hàm def có đối số)
def PTB1(a,b):
    if a == 0 and b == 0:
        return "Phuong trinh co vo so nghiem"
    elif a == 0 and b !=0:
        return "Phuong trinh vo nghiem"
    else:
        return "Phuong trinh co nghiem x = {}".format(round(-b/a))
x = PTB1(1,2)
print(x)


# Tạo hàm xuất 1 chuỗi (Đây là hàm def kh có đối số)
def xuatchuoi(a):
    print(a)
x = input("Nhap 1 chuoi : ")
xuatchuoi(x)


# Tạo hàm tính tỉ lệ Roi = (doanh thu - chi phí)/chi phí , nếu Roi >= 0.75 nên đầu tư
def roi(a,b):
    if (a-b)/b >= 0.75:
        return "Roi = {} -> Nen dau tu".format(round((a-b)/b,2))
    else:
        return "Roi = {} -> Khong nen dau tu".format(round((a-b)/b,2))
a = float(input("Nhap doanh thu : "))
b = float(input("Nhap chi phi : "))
print(roi(a,b))