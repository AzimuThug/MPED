import matplotlib.pyplot as plt
import time

from classes.model import Model

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True


def main():
    new_model = Model()

    N = 10 ** 3 # число точек
    M = 1000     #
    a = 30      # степень экспаненты
    f = 7       # частота гармонического процесса
    R = 1       # амплитуда импульсов
    Rs = 0.1    # разброс пиков
    dt = 0.005  # шаг

    h = new_model.cardiogram(N, f, dt, a)
    x = new_model.rhythm(N, M, R, Rs)
    s = [0]*N
    s[100] = 1
    s[230] = 0.95
    s[500] = 1.05
    s[700] = 1
    # s = new_model.spikes(s, N, 5, R, time.time())
    convolution = new_model.convolModel(h, s, N, M)

    fig, ax = plt.subplots(nrows=3, ncols=1)
    fig.suptitle("Задание 11", fontsize=15)
    ax[0].plot(h)
    ax[1].plot(s)
    ax[2].plot(convolution)
    plt.show()

main()