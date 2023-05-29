# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
# Build a for loop from scratch
for x in house :
    print("the " + x[0] + " is " + str(x[1]) + " sqm")



# Cấu trúc for cho dictionaries:
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
# Iterate over europe
for x,y in europe.items():
    print("the capital of " + x + " is " + y)


import pandas as pd 
dict1 = pd.read_csv("Pandas_country.csv", index_col=0)
for x,y,z in dict1.iterrows():
    print(x)
    print(y)
    print(z)
