import matplotlib.pyplot as plt
from classes.proccessing import Proccessing
from classes.analysis import Analysis
from classes.model import Model
import numpy as np

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True

def main():
    new_analysis = Analysis()
    new_model = Model()

    fc = 3
    fc1 = 1.5
    fc2 = 3
    m = 128
    M = 2 * m + 1
    dt = 0.1
    N = 256

    polyharm = new_model.data_2_tab1()

    low_pass_filter = Proccessing.lpf_reverse(Proccessing.lpf(fc, m, dt))
    high_pass_filter = Proccessing.hpf(fc, m, dt)
    band_pass_filter = Proccessing.bpf(fc1, fc2, m, dt)
    band_stop_filter = Proccessing.bsf(fc1, fc2, m, dt)

    signal_1 = new_model.convolModel(polyharm, low_pass_filter, N, M)
    signal_2 = new_model.convolModel(polyharm, band_pass_filter, N, M)
    signal_3 = new_model.convolModel(polyharm, high_pass_filter, N, M)
    signal_4 = new_model.convolModel(polyharm, band_stop_filter, N, M)


    lpf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(low_pass_filter, M), M)
    hpf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(high_pass_filter, M), M)
    bpf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(band_pass_filter, M), M)
    bsf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(band_stop_filter, M), M)
    new_X_n = new_analysis.spectrFourier([i for i in range(M)], M, dt / 2)
    new_X_1 = new_analysis.spectrFourier([i for i in range(N)], N, dt)

    polyharm_furier_before = new_analysis.Fourier(polyharm, N)
    polyharm_furier = new_analysis.Fourier(signal_2, N)

    fig, ax = plt.subplots(nrows=5, ncols=2)
    fig.suptitle("Задание 13", fontsize=15)
    ax[0, 0].plot(polyharm)
    ax[1, 0].plot(signal_1)
    ax[2, 0].plot(signal_2)
    ax[3, 0].plot(signal_3)
    ax[4, 0].plot(signal_4)
    ax[0, 1].plot(new_X_1, polyharm_furier_before)
    ax[1, 1].plot(new_X_n, lpf_fr)
    ax[2, 1].plot(new_X_n, bpf_fr)
    ax[3, 1].plot(new_X_n, hpf_fr)
    ax[4, 1].plot(new_X_1, polyharm_furier)
    ax[0, 1].set_xlim([0, 1 / (dt * 2)])
    ax[1, 1].set_xlim([0, 1 / (dt * 2)])
    ax[2, 1].set_xlim([0, 1 / (dt * 2)])
    ax[3, 1].set_xlim([0, 1 / (dt * 2)])
    ax[4, 1].set_xlim([0, 1 / (dt * 2)])
    ax[0, 0].set_title("Исходный сигнал")
    ax[1, 0].set_title(f"НЧ до {fc} Гц")
    ax[2, 0].set_title(f"СЧ между {fc1} и {fc2} Гц")
    ax[3, 0].set_title(f"ВЧ более {fc} Гц")
    ax[4, 0].set_title("Полисигнал")
    ax[0, 1].set_title("Спектр исходного сигнала")
    ax[1, 1].set_title("АЧХ ФНЧ")
    ax[2, 1].set_title("АЧХ ПФ")
    ax[3, 1].set_title("АЧХ ФВЧ")
    ax[4, 1].set_title("Спектр отфильтрованного сигнала")

    plt.show()

main()