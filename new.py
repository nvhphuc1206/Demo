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

    

def find_all_occurrences(string, substring):
    occurrences = []
    start_index = 0
    while True:
        index = string.find(substring, start_index)
        if index == -1:
            break
        occurrences.append(index)
        start_index = index + 1
    return occurrences

string1 = "Hello, how are you? I'm fine, how about you?"
string2 = "how"

# Tìm tất cả các vị trí trùng lặp
occurrences = find_all_occurrences(string1, string2)
print(occurrences)
if occurrences:
    print("Chuỗi con được tìm thấy tại các vị trí sau:")
    for index in occurrences:
        print(index)
else:
    print("Chuỗi con không được tìm thấy")
