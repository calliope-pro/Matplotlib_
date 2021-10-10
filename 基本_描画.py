import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# シード固定
np.random.seed(0)


# 変数x・y
x = np.linspace(0, 1, 10)
y = 2 * x + 0.1 * np.random.randn(10)
print(y)


# 折れ線(テンプレ)
# plt.figure(figsize=(10, 7)) # figsize=(width, height)
# plt.plot(x, y)
# plt.show()


# 折れ線(汎用)
fig = plt.figure() # グラフ領域の準備(ベースのキャンバス)
ax: plt.Axes = fig.add_subplot(111) # 実際にはAxesを使ってグラフを書く(gridの指定)
ax.plot(x, y) # 描画
plt.show() # 表示






