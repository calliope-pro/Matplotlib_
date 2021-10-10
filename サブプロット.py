import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import ndarray
from matplotlib.pyplot import Axes

from 基本_複数 import x_1, x_2, x_3, y_1, y_2, y_3

np.random.seed(0)


# figに対応するaxesを一気に同時作成
axes: ndarray # shape=(2, 3), 各グラフに対応
fig, axes = plt.subplots(2, 3, figsize=(10, 7)) # **fig_kwはFigureのパラメータ

# 多次元indexでのax指定
# axes[0, 0].plot(x_1, y_1)
# axes[0, 2].plot(x_2, y_2)
# axes[1, 1].plot(x_3, y_3)

# 1次元化indexでのax指定
axes = axes.ravel()
axes[0].plot(x_1, y_1)
axes[2].plot(x_2, y_2)
axes[4].plot(x_3, y_3)


plt.show()





