import numpy as np
import time

import matplotlib.pyplot as plt

from classes.model import Model
from classes.analysis import Analysis

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True


def main():
    new_model = Model()
    new_analysis = Analysis()

    N = 1000
    R = 10
    A0 = 100
    f0 = 10
    A1 = 500
    f1 = 33
    dt = 0.001

    noise_1 = new_model.noise(N, R)
    noise_2 = new_model.noise(N, R)
    my_noise_1 = new_model.my_noise(time.time(), N, R)
    my_noise_2 = new_model.my_noise(time.time(), N, R)
    harm_1 = new_model.harm(N, A0, f0, dt)
    harm_2 = new_model.harm(N, A1, f1, dt)

    fig, ax = plt.subplots(nrows=3, ncols=2)
    fig.suptitle("Задание 6.3", fontsize=15)

    ax[0, 0].plot(noise_1)
    ax[1, 0].plot(my_noise_1)
    ax[2, 0].plot(harm_1)

    ax[0, 0].set_title("noise")
    ax[1, 0].set_title("custom noise")
    ax[2, 0].set_title("harm")

    acf_noise = new_analysis.ccf(noise_1, noise_2, N)
    acf_my_noise = new_analysis.ccf(my_noise_1, my_noise_2, N)
    acf_harm = new_analysis.ccf(harm_1, harm_2, N)

    ax[0, 1].plot(acf_noise)
    ax[1, 1].plot(acf_my_noise)
    ax[2, 1].plot(acf_harm)

    ax[0, 1].set_title("ccf of noise")
    ax[1, 1].set_title("ccf of custom noise")
    ax[2, 1].set_title("ccf of harm")

    plt.show()

main()