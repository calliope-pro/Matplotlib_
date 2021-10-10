import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)

""" df = pd.DataFrame(data={
    'c1': ['A', 'A', 'A', 'B', 'B', 'C'],
    'c2': [20, 50, 60, 80, 100, 30],
    'c3': [40, 200, 100, 500, 40, 200]
})

plt.figure()

# xに対してのy
plt.bar(df['c1'].unique(), df.groupby('c1').sum()['c2'])
# print(df.groupby('c1').sum())

plt.show() """


df_2 = pd.DataFrame(
    data=100*np.random.rand(5, 5),
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['c1', 'c2', 'c3', 'c4', 'c5'],
)

x = np.arange(len(df_2))

bar_width = 0.4

plt.bar(x, df_2['c1'], color='red', width=bar_width, label='c1') # -0.2~0.2に棒グラフ
plt.bar(x+bar_width, df_2['c2'], color='blue', width=bar_width, label='c2') # 0.2~0.6に

plt.xticks(x + bar_width / 2, df_2.index, fontsize=10) # メモリの位置

plt.legend()
plt.show()
