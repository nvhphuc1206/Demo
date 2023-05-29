# Dữ liệu Tuple:
a = (1,2,3,4,[5,6])
b = 5,6,7,8
c = ("Chuoi",)
print(a,b,c,sep="\n")
print(type(a))
print(type(b))
print(type(c))
a[4][0] = 6
print(a)

z = [[1,2,3,4],"Hi",True,[5,6,7,8]]
for x in z:
    print(x)


a = (1,2,3,4,[5,6]) # Tuple
b = 5,6,7,8
# Dữ liệu tập hợp (Set):
x = {1,2,3,4,5}
y = {"Hi",b, 11} # Có thể chứa Tuple nhưng tuple đó kh đc chứa những mutable data (Vd như b là Tuple kh chứa list)
z = {"Hello"} 

print(type(x))
print(type(y))
print(type(z))

x.update([10])
x.update("Xin Chao","k")
print(x)
y.add("Xin Chao")
print(y)
x.remove(1)
print(x)