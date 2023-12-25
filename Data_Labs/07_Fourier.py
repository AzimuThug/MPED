import matplotlib.pyplot as plt
import numpy as np

from classes.model import Model
from classes.analysis import Analysis

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True


def main():
    new_model = Model()
    new_analysis = Analysis()

    N = 128
    A0 = 100
    f0 = 33
    A1 = 15
    f1 = 5
    A2 = 20
    f2 = 170
    del_t = 0.001
    dt = 0.1

    harm = new_model.harm(N, A0, f0, del_t)
    # harm = new_model.shift(harm, 100, 0, 200)
    harm = new_model.windowing(harm, N, 100)
    # polyharm = new_model.polyHarm(N, A0, f0, A1, f1, A2, f2, del_t)
    # polyharm = new_model.windowing(polyharm, N, 200)
    # with open("./pgp_dt0005.dat", 'rb') as file:
    #     polyharm = np.fromfile(file, dtype=np.float32)
    polyharm = new_model.data_10_tab2()
    harm_furier = new_analysis.Fourier(harm, N)
    polyharm_furier = new_analysis.Fourier(polyharm, N)
    new_X_n = new_analysis.spectrFourier([i for i in range(N)], N, dt)

    fig, ax = plt.subplots(nrows=2, ncols=2)
    fig.suptitle("Задание 7", fontsize=15)
    ax[0, 0].plot(harm)
    ax[1, 0].plot(new_X_n, harm_furier)
    ax[1, 0].set_xlim([0, 1 / (dt * 2)])
    ax[0, 1].plot(polyharm)
    ax[1, 1].plot(new_X_n, polyharm_furier)
    ax[1, 1].set_xlim([0, 1 / (dt * 2)])
    ax[0, 0].set_title("harm")
    ax[1, 0].set_title("harm spectre")
    # ax[0, 1].set_title("polyharm")
    # ax[1, 1].set_title("polyharm spectre")
    plt.show()

main()