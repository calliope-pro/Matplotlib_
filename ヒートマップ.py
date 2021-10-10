import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

df = pd.DataFrame(np.random.rand(5, 3), columns=['c1', 'c2', 'c3'])

# 描画
plt.pcolor(df, cmap='Blues')
plt.colorbar()
plt.show()