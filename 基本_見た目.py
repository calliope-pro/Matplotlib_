import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)

df = pd.DataFrame(
    data=np.random.rand(30, 2),
    columns=['c1', 'c2'],
)

plt.figure(figsize=(12, 8))

plt.plot(df['c1'])
 # kwargsはLine2Dの基本的にパラメータ
# 幅8.0, 赤点線
plt.plot(df['c2'], color='red', linewidth=8.0, linestyle='dashed')

# グラフのタイトル
plt.title('test title', fontsize=20)

# 軸ラベル
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)

# 凡例
plt.legend(['col1', 'col2'])

plt.show()
