import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)

df = pd.DataFrame(data=np.random.randint(0, 5, 500), columns=['c1'])

print(df['c1'].value_counts())

# デフォルトは3時から反時計まわりえ描画
# plt.pie(df['c1'].value_counts(), labels=df['c1'].value_counts().index)

plt.pie(
    df['c1'].value_counts(),
    labels=df['c1'].value_counts().index,
    autopct='%.1f%%', #auto percent
    startangle=90, 
    counterclock=False,
    textprops={'color': 'gray'}
)


plt.show()