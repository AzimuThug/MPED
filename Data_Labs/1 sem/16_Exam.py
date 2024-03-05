import matplotlib.pyplot as plt
import numpy as np

from classes.model import Model
from classes.analysis import Analysis

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True


def main():
    new_model = Model()
    new_analysis = Analysis()

    # N = 1000
    dt = 0.0005

    with open("./v34.dat", 'rb') as file:
        signal = np.fromfile(file, dtype=np.float32)
    N = len(signal)
    print(N)
    signal_furier = new_analysis.Fourier(signal, N)
    new_X_n = new_analysis.spectrFourier([i for i in range(N)], N, dt)

    fig, ax = plt.subplots(nrows=2, ncols=1)
    fig.suptitle("Зачетное задание", fontsize=15)
    ax[0].plot(harm)
    ax[1].plot(new_X_n, signal_furier)
    ax[1].set_xlim([0, 1 / (dt * 2)])
    ax[0].set_title("signal")
    ax[1].set_title("signal spectre")

    plt.show()

main()
