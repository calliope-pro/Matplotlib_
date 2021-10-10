import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)

plt.style.use('ggplot')

x = np.linspace(0, 1, 10)
y = 2 * x + np.random.randn(10)
plt.plot(x, y)
plt.show()






