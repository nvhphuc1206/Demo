import numpy as np
np.random.seed(123)
print(np.random.rand())
print(np.random.rand())

# Tạo 1 giả lập xuất phát từ 50, đổ xúc xắc nếu kq là 1,2 thì lùi 1 bước, là3,4,5 thì tiến 1 bước còn là 6 thì số bước tiến bằng số trên xúc xắc:
np.random.seed(123)
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)


# Giả lập 1 trò chơi dùng xúc xắc để tính xem sau 100 lần thử thì có thể tiến bao nhiêu bước:
import numpy as np
np.random.seed()
# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1) # Hàm max để giới hạn lại biến step không bào giờ dưới 0
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)
print(random_walk)


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)
plt.xlabel("So lan thu")
plt.ylabel("So buoc")
# Show the plot
plt.show()
plt.clf()
