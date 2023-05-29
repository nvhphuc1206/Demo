import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5,6,7,8,9,10,11]
y = ["a","b","c","d","e","f","g","h","j","k","l"]
plt.scatter(y,x,s=np.array(x)*10,c="gray", alpha=1)
    
# x,bins=None, range=None,density=False,weights=None,cumulative=False,bottom=None,histtype="bar",align="mid",orientation="vertical",rwidth=None, log=False, color=None, label=None,stacked=False, data=None
plt.xlabel("So nguyen")
plt.ylabel("Chu cai")
plt.text("a",1,"Phan tu 1")
plt.grid(True)
plt.show()

