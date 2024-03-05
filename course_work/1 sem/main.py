import matplotlib.pyplot as plt
import numpy as np
import time
from classes.model import Model
from classes.analysis import Analysis
from classes.proccessing import Proccessing

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True


def main():
    new_model = Model()
    new_analysis = Analysis()

    N = 10 ** 3
    A = 30
    f0 = 10
    df = 1
    f1 = 2
    del_t = 0.01
    dt = 0.001

    m = 128
    M = 2 * m + 1

    # harm = new_model.harm(N, A, f1, del_t)
    signal = new_model.frequencyModulation(N, A, f0, df, f1, del_t)
    noise = new_model.my_noise(time.time(), N, 40)
    signal = new_model.addModel(signal, noise, N)
    signal = new_model.spikes(signal, N, 12, 50, time.time())
    # signal = new_model.shift(signal, 100, 300, 400)
    # signal = Proccessing.antiSpike(signal)
    # signal = Proccessing.antiNoise(signal)
    # signal = Proccessing.antiShift(signal)

    low_pass_filter = Proccessing.lpf_reverse(Proccessing.lpf(10, m, dt/2))
    signal = new_model.convolModel(signal, low_pass_filter, N, M)

    signal_fourier = new_analysis.Fourier(signal, N)
    new_X_n = new_analysis.spectrFourier([i for i in range(N)], N, dt)
    k = np.arange(0, N, 1)

    fig, ax = plt.subplots(nrows=2, ncols=1)
    fig.suptitle("Курсовая работа", fontsize=15)
    # ax[0].plot(k, signal, 'r', k, harm, 'g')
    ax[0].plot(k, signal)
    ax[1].plot(new_X_n, signal_fourier)
    ax[1].set_xlim([0, 1 / (dt * 2)])
    ax[0].set_title("ЧМ сигнал")
    ax[1].set_title("Спектр ЧМ сигнала")
    plt.show()

main()