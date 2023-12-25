import matplotlib.pyplot as plt
from classes.proccessing import Proccessing
from classes.analysis import Analysis

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True


def main():
    new_analysis = Analysis()

    fc = 50
    fc1 = 35
    fc2 = 75
    m = 256
    M = 2 * m + 1
    dt = 0.002

    low_pass_filter = Proccessing.lpf_reverse(Proccessing.lpf(fc, m, dt))
    high_pass_filter = Proccessing.hpf(fc, m, dt)
    band_pass_filter = Proccessing.bpf(fc1, fc2, m, dt)
    band_stop_filter = Proccessing.bsf(fc1, fc2, m, dt)

    lpf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(low_pass_filter, M), M)
    hpf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(high_pass_filter, M), M)
    bpf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(band_pass_filter, M), M)
    bsf_fr = Proccessing.frequencyResponse(new_analysis.Fourier(band_stop_filter, M), M)
    new_X_n = new_analysis.spectrFourier([i for i in range(M)], M, dt / 2)

    fig, ax = plt.subplots(nrows=4, ncols=2)
    fig.suptitle("Задание 12", fontsize=15)
    ax[0, 0].plot(low_pass_filter)
    ax[1, 0].plot(high_pass_filter)
    ax[2, 0].plot(band_pass_filter)
    ax[3, 0].plot(band_stop_filter)
    ax[0, 1].plot(new_X_n, lpf_fr)
    ax[1, 1].plot(new_X_n, hpf_fr)
    ax[2, 1].plot(new_X_n, bpf_fr)
    ax[3, 1].plot(new_X_n, bsf_fr)
    ax[0, 1].set_xlim([0, 1 / (dt * 2)])
    ax[1, 1].set_xlim([0, 1 / (dt * 2)])
    ax[2, 1].set_xlim([0, 1 / (dt * 2)])
    ax[3, 1].set_xlim([0, 1 / (dt * 2)])
    ax[0, 0].set_title("импульсная характеристика ФНЧ")
    ax[1, 0].set_title("импульсная характеристика ФВЧ")
    ax[2, 0].set_title("импульсная характеристика ПФ")
    ax[3, 0].set_title("импульсная характеристика РФ")
    ax[0, 1].set_title("АЧХ ФНЧ")
    ax[1, 1].set_title("АЧХ ФВЧ")
    ax[2, 1].set_title("АЧХ ПФ")
    ax[3, 1].set_title("АЧХ РФ")


    plt.show()

main()