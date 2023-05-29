import numpy as np
import matplotlib.pyplot as plt

all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(10) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
print(random_walk)
print(all_walks)
# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)
print(np_aw)

# Plot np_aw and show
plt.plot(np_aw) # Có 100 đường mỗi đường 10 giá trị
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw) # Hàm hoán vị
print(np_aw_t)

# Plot np_aw_t and show
plt.plot(np_aw_t) # Có 10 đường mỗi đường 100 giá trị
plt.show()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]
print(ends)

# Plot histogram of ends, display plot
plt.hist(ends,10)
plt.show()
plt.clf()
print(np.mean(ends >= 60)) # Chuyển array ends thành array gồm boolean với đk là >=60 sao đó mỗi p/tử true sẽ được tính là 1 và đem đi tính trung bình.
