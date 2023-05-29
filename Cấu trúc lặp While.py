# Tạo 1 vòng lặp while đơn giản:
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset -1 
    print(offset)

# Có thể thêm điều kiện vào trong cấu trúc lặp While nhằm tránh trường hợp lặp vô hạn vì đặc điểm của từng biến:
# Initialize offset (Khi này offset < 0 nên nếu giữ nguyên câu lệnh như trên thì vòng lặp sẽ vô hạn)
offset = -6
# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1 
    else : 
      offset = offset + 1
    print(offset)


# Sử dụng cấu trúc lặp While để tính tổng các phần tử trong mảng: 
a = [1 ,2 ,3 ,4 ,5]
N = len ( a )
Tong = 0
i = 0
while ( i < N) :
  Tong = Tong + a [ i ]
  i = i + 1
print ("Tong cac phan tu trong mang la : ", Tong)