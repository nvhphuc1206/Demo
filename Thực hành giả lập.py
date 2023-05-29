import numpy as np
import matplotlib.pyplot as plt 

# Ví dụ muốn mô phỏng khả năng trúng độc đắc vé số của 1 người thì:
kq = []
for i in range(1):
    so1 = np.random.randint(0,10)
    so2 = np.random.randint(0,10)
    so3 = np.random.randint(0,10)
    so4 = np.random.randint(0,10)
    so5 = np.random.randint(0,10)
    so6 = np.random.randint(0,10)
    kqso1 = np.random.randint(0,10)
    kqso2 = np.random.randint(0,10)
    kqso3 = np.random.randint(0,10)
    kqso4 = np.random.randint(0,10)
    kqso5 = np.random.randint(0,10)
    kqso6 = np.random.randint(0,10)
    if so1 == kqso1:
        if so2 == kqso2:
            if so3 == kqso3:
                if so4 == kqso4:
                    if so5 == kqso5:
                        if so6 == kqso6:
                            kq.append("Độc đắc")
                        else:
                            kq.append("Giải nhì")
                    else:
                            kq.append("Giải ba")
                else:
                            kq.append("Giải tư")
            else:
                            kq.append("Giải năm")
        else:
                            kq.append("Giải khuyến khích")
    else:
                            kq.append("Không trúng")
plt.hist(kq,7)
plt.show()
print((kq=="Không trúng"))


# Tính xác xuất 2 người rút 1 lá bài thì sẽ chiến thắng:
import numpy as np
import matplotlib.pyplot as plt

a = []
for i in range(1000):
        x = np.random.randint(1,13)
        y = np.random.randint(1,13)
        if x > y :
            a.append("Thắng")
        elif x == y :
            a.append("Hòa")
        else:
            a.append("Thua")
plt.hist(a,3)
plt.xlabel("Kết quả")
plt.ylabel("Số lần")
plt.show()
b = np.array(a)
print(np.mean(b == "Thắng"))



# Giả lập bài toán chơi kéo búa bao để về đích (Thắng = +1, thua = -1, hòa = 0)
import numpy as np 
ket_qua = 0
steps = []
for i in range(100):
    x = np.random.randint(1,4)
    y = np.random.randint(1,4)
    if x > y:
        steps.append("+1")
        ket_qua = ket_qua + 1
    elif x < y:
        steps.append("-1")
        ket_qua = max(0,ket_qua - 1)
    else:
        steps.append("0")
        ket_qua = ket_qua
print(steps)
print(ket_qua)
