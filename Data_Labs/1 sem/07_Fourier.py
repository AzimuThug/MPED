# import matplotlib.pyplot as plt
# import numpy as np
#
# from classes.model import Model
# from classes.analysis import Analysis
#
# plt.rcParams["figure.figsize"] = [20, 7.5]
# plt.rcParams["figure.autolayout"] = True
#
#
# def main():
#     new_model = Model()
#     new_analysis = Analysis()
#
#     N = 1000
#     A0 = 100
#     f0 = 33
#     A1 = 15
#     f1 = 5
#     A2 = 20
#     f2 = 170
#     del_t = 0.005
#     dt = 0.1
#
#     harm = new_model.harm(N, A0, f0, del_t)
#     data = new_model.addModel(harm, new_model.trend_linear(N, 2, 0), N)
#
#     data_furier = new_analysis.Fourier(data, N)
#     new_X_n = new_analysis.spectrFourier([i for i in range(N)], N, dt)
#
#     fig, ax = plt.subplots(nrows=2, ncols=1)
#     fig.suptitle("Задание 7", fontsize=15)
#     ax[0].plot(data)
#     ax[1].plot(new_X_n, data_furier)
#     ax[1].set_xlim([0, 1 / (dt * 2)])
#
#     plt.show()
#
# main()

import matplotlib.pyplot as plt
import numpy as np

from classes.model import Model
from classes.analysis import Analysis
from classes.proccessing import Proccessing

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True


def main():
    new_model = Model()
    new_analysis = Analysis()

    fc = 10
    fc1 = 430
    fc2 = 450
    m = 256
    M = 2 * m + 1
    dt = 0.0005
    N = 1000

    # Открываем и убираем смещение
    with open("./v34.dat", 'rb') as file:
        signal = np.fromfile(file, dtype=np.float32)
    signal_source = Proccessing.antiShift(signal)
    # signal_source = new_model.addModel(signal_source, new_model.trend_linear(N,0.1, 0), N)

    # Убираем тренд
    # signal_source = Proccessing.antiTrendLinear(signal_source, N)
    # signal_source = Proccessing.antiTrendNonLinear(signal_source, N, 100)

    # Фильтр
    low_pass_filter = Proccessing.lpf_reverse(Proccessing.lpf(fc, m, dt))
    band_pass_filter = Proccessing.bpf(fc1, fc2, m, dt)
    signal_lpf = new_model.convolModel(signal_source, low_pass_filter, N, M)
    signal_bpf = new_model.convolModel(signal_source, band_pass_filter, N, M)

    # Суммарный сигнал
    addSignal_1 = new_model.addModel(signal_lpf, signal_bpf, N)

    # График Фурье
    signal_furier_raw = new_analysis.Fourier(signal, N)
    signal_furier = new_analysis.Fourier(signal_source, N)
    signal_furier_lpf = new_analysis.Fourier(signal_lpf, N)
    signal_furier_bpf = new_analysis.Fourier(signal_bpf, N)
    signal_furier_result = new_analysis.Fourier(addSignal_1, N)
    new_X_n = new_analysis.spectrFourier([i for i in range(N)], N, dt / 2)

    # Построение графиков
    fig, ax = plt.subplots(nrows=5, ncols=2)
    fig.suptitle("Зачетное задание", fontsize=15)
    ax[0, 0].plot(signal)
    ax[1, 0].plot(signal_source)
    ax[2, 0].plot(signal_lpf)
    ax[3, 0].plot(signal_bpf)
    ax[4, 0].plot(addSignal_1)
    ax[0, 1].plot(new_X_n, signal_furier_raw)
    ax[1, 1].plot(new_X_n, signal_furier)
    ax[2, 1].plot(new_X_n, signal_furier_lpf)
    ax[3, 1].plot(new_X_n, signal_furier_bpf)
    ax[4, 1].plot(new_X_n, signal_furier_result)
    ax[0, 1].set_xlim([0, 1 / (dt * 2)])
    ax[1, 1].set_xlim([0, 1 / (dt * 2)])
    ax[2, 1].set_xlim([0, 1 / (dt * 2)])
    ax[3, 1].set_xlim([0, 1 / (dt * 2)])
    ax[4, 1].set_xlim([0, 1 / (dt * 2)])
    ax[4, 0].set_xlim([370, 1000]) #
    ax[0, 0].set_title("signal raw")
    ax[1, 0].set_title("signal")
    ax[2, 0].set_title("signal lpf")
    ax[3, 0].set_title("signal bpf")
    ax[4, 0].set_title("signal result")
    ax[0, 1].set_title("signal raw spectre")
    ax[1, 1].set_title("signal spectre")
    ax[2, 1].set_title("signal lpf spectre")
    ax[3, 1].set_title("signal bpf spectre")
    ax[4, 1].set_title("signal result spectre")

    # fig, ax = plt.subplots(nrows=2, ncols=1)
    # fig.suptitle("Зачетное задание", fontsize=15)
    # ax[0].plot(signal)
    # ax[1].plot(addSignal_1)
    # ax[1].set_xlim([400, 1000])

    plt.show()

main()