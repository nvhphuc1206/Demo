string1 = "Hello, World!, Hello, Hi, Hello "
string2 = "Hello"

index = string1.find(string2)
print(index)
if index != -1:
    print(f"Chuỗi '{string2}' tồn tại trong chuỗi '{string1}' tại vị trí {index}")
else:
    print(f"Chuỗi '{string2}' không tồn tại trong chuỗi '{string1}'")

import os 
print(os.getcwd())
