import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# df = pd.DataFrame(data=np.random.randint(0, 100, 500), columns=['c1'])
# 単数
# plt.boxplot(df['c1'], labels=['c1'])
# plt.show()

df_2 = pd.DataFrame(data=np.random.randint(0, 100, (500, 3)), columns=['c1', 'c2', 'c3'])
# 複数
plt.boxplot([df_2['c1'], df_2['c2'], df_2['c3']], labels=['c1', 'c2', 'c3'])
# 下でも良い
# plt.boxplot(df_2[['c1', 'c2', 'c3']], labels=['c1', 'c2', 'c3'])
plt.show()
