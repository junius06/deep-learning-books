import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
y = np.sin(x)

# 그래프 그리기
plt.plot(x, y)
# plt.show() # wsl 환경에서는 그래프가 GUI로 띄워지지 않음.
 
# 그래프 사진 생성
plt.savefig("p-42.plot.png")