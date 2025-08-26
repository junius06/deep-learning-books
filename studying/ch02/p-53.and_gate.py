# p.51
## 2.3. 퍼셉트론 구현하기
## 2.3.3. 가중치와 편향 구현하기

import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])      # 입력
    w = np.array([0.5, 0.5])    # 가중치
    b = -0.7                    # 편향
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1