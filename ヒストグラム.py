from typing import Union
import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
import pandas as pd
from pandas import Series
from scipy.stats import norm

np.random.seed(0)

df = pd.DataFrame(data=np.random.randn(500), columns=['c1'])

# plt.hist(df['c1']) # デフォルトのヒストグラム

# plt.hist(df['c1'], bins=20, rwidth=0.8, color='gray') # 20本, 棒の幅
# plt.show()

def histgram(x: Union[ndarray, Series]):
    plt.hist(x, bins=20, rwidth=0.8, color='gray', density=True)
    
    print(x)
    mean = x.mean()
    std = x.std()
    
    X = np.linspace(x.min(), x.max(), 20) # 折れ線用のx
    y = norm.pdf(X, mean, std) # 確率密度

    plt.plot(X, y, linewidth=3)
    plt.show()

histgram(df['c1'])

