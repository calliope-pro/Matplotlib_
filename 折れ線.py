import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)

df = pd.DataFrame(
    data=np.random.rand(30, 2),
    columns=['c1', 'c2'],
)

plt.figure(figsize=(12, 8))

# 普通のplotが折れ線
plt.plot(df['c1'])
plt.plot(df['c2'])

plt.show()




