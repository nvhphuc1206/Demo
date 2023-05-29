import pandas as pd 
# Tạo DataFrame từ dictionary:
# VD1:
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
brics1 = pd.DataFrame(house)
brics1.index = ["HALL","KIT","LIVING","BED","BATH"] # Cách thay đổi stt của từng dòng
print(brics1)

# VD2:
import pandas as pd 
europe = {"Spain":{"Capital":"Madrid","Population":46.77},
          "France":{"Capital":"Paris","Population":66.03},
          "Germany":{"Capital":"Berlin","Population":80.02},
          "Norway":{"Capital":"Olso","Population":5.084}}
brics2 = pd.DataFrame(europe)
print(brics2)

# Tạo DataFrame từ file CSV:
import pandas as pd 
dict1 = pd.read_csv("Pandas_country.csv", index_col=0)
print(dict1)
print(dict1.keys())

# Column and Row Access []: Rút trích p/tử bằng ngoặc vuông (Chỉ lấy được cả dòng hoặc cả cốt, kh thể lấy riêng từng p/tử)
print(dict1[["Capital","Area"]])
print(dict1[0:2])

# Column and Row Access by loc and iloc: (loc và iloc có thể rút trích riêng từng p/tử)
print(dict1.loc[["BR"],["Country"]])
print(dict1.loc[:,:])
print(dict1.loc[:,["Country"]])

print(dict1.iloc[0:2])
print(dict1.iloc[[0,1,2]])
print(dict1.iloc[[0],:])

import pandas as pd 
dict1 = pd.read_csv("Pandas_country.csv", index_col=0)
print(dict1)
print(dict1.loc[["BR"],["Country"]])

dict = {"country":["Brazil","Russia","India"], #Key là giá trị duy nhất và không thể thay đổi 
        "country":3,
        "country":6}
print(dict["country"])
print(3 in dict)


