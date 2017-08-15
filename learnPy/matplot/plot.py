import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bo', t, t**3, 'g^') # 参数循环：x轴,y轴,绘图形式
help(plt.plot)
plt.show()