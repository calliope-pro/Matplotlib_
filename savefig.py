import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

np.random.seed()

x = np.linspace(0, 1, 10)
y = 2 * x + np.random.randn(10)
plt.plot(x, y)

plt.savefig(Path('./test_img.png'))




