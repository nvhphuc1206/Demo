import pandas as pd 
dict1 = pd.read_csv("Pandas_country.csv", index_col=0)
print(dict1)
for lab,row in dict1.iterrows(): #iterows() là hàm duyệt qua tất cả các hàng với mỗi lần trả về 1 Tuple bao gồm index và series của hàng đó
    print(lab)
    print(row)

# Sử dụng cấu trúc lặp để thêm 1 cột mới vào brics:
for lab,row in dict1.iterrows():
    dict1.loc[lab,"name_lenght"] = len(row["Country"])
print(dict1)
# Thêm cột mà kh cần dùng vòng lặp:
dict1["name_length"] = dict1["Country"].apply(len)
print(dict1)
# Thêm cột khi cần sử dụng hàm method: .upper ở đây là hàm method nên có chút khác biệt 
dict1["COUNTRY"] = dict1["Country"].apply(str.upper)
print(dict1)