# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15 :
    print("big place!")

# Câu lệnh điều kiện lồng:
a = 20
b = 10 
if a > 1:
     if b > 12:
          a = a + 1
          b = b + 1
else :
     a = a + 2 
     b = b + 2 
     
print(a,b)



# Viết chương trình nhập vào tháng của năm, in ra số ngày của tháng:
t = int(input("Nhap thang t cua nam 2023: "))
if t == 2:
     s = 28
elif t == 4 or t == 6 or t == 9 or t == 11 :
     s = 30
else:
     s = 31
print("So ngay cua thang",t,"la", s)
