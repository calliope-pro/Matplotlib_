from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)

x_1 = np.linspace(0, 1, 10)
y_1 = x_1 + 0.1 * np.random.randn(10)

x_2 = np.linspace(0, 1, 100)
y_2 = x_2 + 0.1 * np.random.randn(100)

x_3 = np.linspace(0, 1, 1000)
y_3 = x_3 + 0.1 * np.random.randn(1000)

if __name__ == '__main__':
    fig: Figure = plt.figure(figsize=(10, 7)) # figsize=(width, height)


    ax_1 = fig.add_subplot(231) # 2行3列の内の1番目
    ax_2 = fig.add_subplot(233) # 2行3列の内の3番目
    ax_3 = fig.add_subplot(212) # 2行1列の内の2番目

    ax_1.plot(x_1, y_1)
    ax_2.plot(x_2, y_2)
    ax_3.plot(x_3, y_3)

    plt.show()


