import time

import matplotlib.pyplot as plt

from classes.model import Model
from classes.proccessing import Proccessing

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True

def main():
    new_model = Model()

    N = 10 ** 3
    A0 = 5
    f0 = 50
    dt = 0.001

    harm = new_model.harm(N, A0, f0, dt)
    noise = new_model.noise(N, 10)
    harm = new_model.shift(harm, 100, 0, N)
    noise = new_model.shift(noise, 100, 0, N)
    harm = new_model.spikes(harm, N, 5, 50, time.time())
    noise = new_model.spikes(noise, N, 5, 50, time.time())
    harm_source = Proccessing.antiShift(harm)
    noise_source = Proccessing.antiShift(noise)
    harm_source = Proccessing.antiSpike(harm_source)
    noise_source = Proccessing.antiSpike(noise_source)

    fig, ax = plt.subplots(nrows=2, ncols=2)
    fig.suptitle("Задание 9", fontsize=15)
    ax[0, 0].plot(harm)
    ax[1, 0].plot(noise)
    ax[0, 1].plot(harm_source)
    ax[1, 1].plot(noise_source)
    ax[0, 0].set_title("harm")
    ax[1, 0].set_title("noise")
    ax[0, 1].set_title("harm_after")
    ax[1, 1].set_title("noise_after")
    plt.show()

main()