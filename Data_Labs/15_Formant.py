import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft
from classes.proccessing import Proccessing
from classes.model import Model
from classes.in_out import IN_OUT

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True

file_name = "record"

def filterWAV(data, N, dt):
    new_model = Model()

    # Для первого слога
    # f0 = 260 + 40
    # f1 = 506
    # f2 = 1262
    # f3 = 2354
    # f4 = 3600 - 100

    # Для второго слога
    f0 = 230 + 40
    f1 = 564
    f2 = 1224
    f3 = 2450
    f4 = 3600 - 100

    m = 128
    M = 2 * m + 1
    low_pass_filter = Proccessing.lpf_reverse(Proccessing.lpf(f0, m, dt)) # Основной тон
    band_pass_filter_F1 = Proccessing.bpf(f1 - 50, f1 + 50, m, dt) # первая форманта
    band_pass_filter_F2 = Proccessing.bpf(f2 - 50, f2 + 50, m, dt) # вторая форманта
    band_pass_filter_F3 = Proccessing.bpf(f3 - 50, f3 + 50, m, dt) # третья форманта
    high_pass_filter_F4 = Proccessing.hpf(f4, m, dt) # четвертая форманта

    patch = new_model.convolModel(data, low_pass_filter, N, M)
    print('point 7')
    formant_1 = new_model.convolModel(data, band_pass_filter_F1, N, M)
    print('point 8')
    formant_2 = new_model.convolModel(data, band_pass_filter_F2, N, M)
    print('point 9')
    formant_3 = new_model.convolModel(data, band_pass_filter_F3, N, M)
    print('point 10')
    formant_4 = new_model.convolModel(data, high_pass_filter_F4, N, M)

    fig, ax = plt.subplots(nrows=6, ncols=1)
    fig.suptitle("Задание 15", fontsize=15)
    ax[0].plot(data)
    ax[1].plot(patch)
    ax[2].plot(formant_1)
    ax[3].plot(formant_2)
    ax[4].plot(formant_3)
    ax[5].plot(formant_4)
    ax[0].set_title("Исходный сигнал")
    ax[1].set_title("Основной тон")
    ax[2].set_title("1 форманта")
    ax[3].set_title("2 форманта")
    ax[4].set_title("3 форманта")
    ax[5].set_title("4 форманта")
    plt.show()

    formant_1 = np.array(formant_1, dtype=np.int16)
    formant_2 = np.array(formant_2, dtype=np.int16)
    formant_3 = np.array(formant_3, dtype=np.int16)
    formant_4 = np.array(formant_4, dtype=np.int16)
    patch = np.array(patch, dtype=np.int16)

    IN_OUT.writeWAV("./records/patch.wav", patch, 1, 2, 22050, len(patch))
    IN_OUT.writeWAV("./records/formant1.wav", formant_1, 1, 2, 22050, len(formant_1))
    IN_OUT.writeWAV("./records/formant2.wav", formant_2, 1, 2, 22050, len(formant_2))
    IN_OUT.writeWAV("./records/formant3.wav", formant_3, 1, 2, 22050, len(formant_3))
    IN_OUT.writeWAV("./records/formant4.wav", formant_4, 1, 2, 22050, len(formant_4))

def main():
    data, nchannels, sampwidth, framerate, nframes = IN_OUT.readWAV("./records/" + file_name + ".wav")

    div = 18000
    data = data[0:div]      # первый слог
    # data = data[div:nframes]  # второй слог

    sr = 22050
    ts = 1.0 / sr
    t = np.arange(0, div/framerate, ts)                 # первый слог
    # t = np.arange(0, (nframes-div)/framerate, ts)     # второй слог
    X = fft(data)
    N = len(X)
    n = np.arange(N)
    T = N / sr
    freq = n / T

    plt.figure(figsize=(12, 6))
    plt.subplot(121)

    plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude |X(freq)|')
    plt.xlim(0, 4000)

    plt.subplot(122)
    plt.plot(t, ifft(X), 'r')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

    filterWAV(data, N, ts)

    # IN_OUT.writeWAV("./records/" + file_name + "_out.wav", data_proccessed, nchannels, sampwidth, framerate, nframes)

main()