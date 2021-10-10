import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.markers import MarkerStyle

np.random.seed(0)

df = pd.DataFrame(
    data=np.random.rand(30, 2),
    columns=['c1', 'c2'],
)
df['data_size'] = np.random.randint(1, 100, 30)


plt.figure(figsize=(8, 4))

# scatterで散布図
plt.scatter(
    df['c1'].index,
    df['c1'].values,
    s=df['data_size']*10, # s:大きさ
    c=df['data_size'], # c:色
    cmap='viridis', # cmap:カラーマップ
    alpha=0.7, # alpha:透明度
    marker=MarkerStyle('o'), # marker:マーカー
)

plt.colorbar()

plt.title('Test Scatter')

plt.xlabel('index $x_0$')
plt.ylabel('value $y_0$')

plt.show()
