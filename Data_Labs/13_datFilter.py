import matplotlib.pyplot as plt
from classes.proccessing import Proccessing
from classes.analysis import Analysis
from classes.model import Model
from classes.in_out import IN_OUT
import numpy as np

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True

def main():
    new_analysis = Analysis()
    new_model = Model()

    fc = 50
    fc1 = 70
    fc2 = 250
    m = 256
    M = 2 * m + 1
    dt = 0.0005
    N = 1000

    with open("./pgp_dt0005.dat", 'rb') as file:
        polyharm = np.fromfile(file, dtype=np.float32)

    low_pass_filter = Proccessing.lpf_reverse(Proccessing.lpf(fc, m, dt))
    high_pass_filter = Proccessing.hpf(fc2, m, dt)
    band_pass_filter = Proccessing.bpf(fc1, fc2, m, dt)
    band_stop_filter = Proccessing.bsf(fc1, fc2, m, dt)

    signal_1 = new_model.convolModel(polyharm, low_pass_filter, N, M)
    signal_2 = new_model.convolModel(polyharm, band_pass_filter, N, M)
    signal_3 = new_model.convolModel(polyharm, high_pass_filter, N, M)
    signal_4 = new_model.convolModel(polyharm, band_stop_filter, N, M)

    polyharm_furier = new_analysis.Fourier(polyharm, N)
    lpf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(low_pass_filter, M), M)
    hpf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(high_pass_filter, M), M)
    bpf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(band_pass_filter, M), M)
    bsf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(band_stop_filter, M), M)
    new_X_n = new_analysis.spectrFourier([i for i in range(M)], M, dt / 2)
    new_X_1 = new_analysis.spectrFourier([i for i in range(N)], N, dt)

    fig, ax = plt.subplots(nrows=5, ncols=2)
    fig.suptitle("Задание 13", fontsize=15)
    ax[0, 0].plot(polyharm)
    ax[1, 0].plot(signal_1)
    ax[2, 0].plot(signal_2)
    ax[3, 0].plot(signal_3)
    ax[4, 0].plot(signal_4)
    ax[0, 1].plot(new_X_1, polyharm_furier)
    ax[1, 1].plot(new_X_n, lpf_fr)
    ax[2, 1].plot(new_X_n, bpf_fr)
    ax[3, 1].plot(new_X_n, hpf_fr)
    ax[4, 1].plot(new_X_n, bsf_fr)
    ax[0, 1].set_xlim([0, 1 / (dt * 2)])
    ax[1, 1].set_xlim([0, 1 / (dt * 2)])
    ax[2, 1].set_xlim([0, 1 / (dt * 2)])
    ax[3, 1].set_xlim([0, 1 / (dt * 2)])
    ax[4, 1].set_xlim([0, 1 / (dt * 2)])
    ax[0, 0].set_title("Исходный сигнал")
    ax[1, 0].set_title("НЧ 10 Гц")
    ax[2, 0].set_title("СЧ 110 Гц")
    ax[3, 0].set_title("ВЧ 500 Гц")
    ax[4, 0].set_title("Полисигнал")
    ax[0, 1].set_title("Спектр исходного сигнала")
    ax[1, 1].set_title("АЧХ ФНЧ")
    ax[2, 1].set_title("АЧХ ПФ")
    ax[3, 1].set_title("АЧХ ФВЧ")
    ax[4, 1].set_title("АЧХ РФ")
    plt.show()

def WAVfile():
    channel_proccessed = []
    array, nchannels, sampwidth, framerate, nframes = IN_OUT.readWAV("file.wav")

    for n in range(nchannels):
        channel = array[n::nchannels]

    for n in range(nframes):
        channel_proccessed.append(channel[n] * 1.5)

    for i in range(nframes * nchannels):
        array[i] *= 1.5

    fig, ax = plt.subplots(nrows=2, ncols=1)
    fig.suptitle("Задание 13", fontsize=15)
    ax[0].plot(channel)
    ax[1].plot(channel_proccessed)
    plt.show()

    IN_OUT.writeWAV("file_out.wav", array, nchannels, sampwidth, framerate, nframes)

# main()
WAVfile()