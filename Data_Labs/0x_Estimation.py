import matplotlib.pyplot as plt
import numpy as np

from classes.model import Model
from classes.analysis import Analysis


def main():
    new_model = Model()
    new_analysis = Analysis()

    N = 180
    dt = 0.006

    # f = open('E:\\pgp_dt0005.dat', 'rb')
    # print(f)
    # signal = f.read()
    # print(signal)

    # with open('E:\\pgp_dt0005.dat', 'rb') as f:
    #     signal = np.fromfile(f, dtype=np.float32)
    # print(signal)

    # signal = new_model.polyHarm(N, 50, 315, 30, 10, 3, 3, 0.001)
    # signal = new_model.harm(N, 10, 330, dt)
    # signal = new_model.noise(N, 10)
    signal = new_model.data_4()
    # signal = new_analysis.acf(signal, N)

    analys1 = new_analysis.Fourier(signal, N)
    analys2 = new_analysis.spectrFourier([i for i in range(N)], N, dt)

    fig, ax = plt.subplots(nrows=2, ncols=1)
    fig.suptitle("Оценка сигнала", fontsize=15)
    ax[0].plot(signal)
    ax[1].plot(analys2, analys1)
    ax[1].set_xlim([0, 1 / (dt * 2)])

    plt.show()

main()