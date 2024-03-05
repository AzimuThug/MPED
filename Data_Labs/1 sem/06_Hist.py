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
    M = 100
    a = -0.01
    b = 0.4
    R = 10
    A0 = 100
    f0 = 33
    A1 = 30
    f1 = 15
    A2 = 2
    f2 = 20
    dt = 0.001

    trend_linear = new_model.trend_linear(N, a, b)
    trend_nonlinear = new_model.exp(N, a, b)
    noise = new_model.noise(N, R)
    my_noise = new_model.my_noise(time.time(), N, R)
    harm = new_model.harm(N, A0, f0, dt)
    polyharm = new_model.polyHarm(N, A0, f0, A1, f1, A2, f2, dt)

    fig, ax = plt.subplots(nrows=6, ncols=2)
    fig.suptitle("Задание 6", fontsize=15)

    ax[0, 0].plot(trend_linear)
    ax[1, 0].plot(trend_nonlinear)
    ax[2, 0].plot(noise)
    ax[3, 0].plot(my_noise)
    ax[4, 0].plot(harm)
    ax[5, 0].plot(polyharm)
    ax[0, 0].set_title("linear trend")
    ax[1, 0].set_title("nonlinear trend")
    ax[2, 0].set_title("noise")
    ax[3, 0].set_title("myNoise")
    ax[4, 0].set_title("harm")
    ax[5, 0].set_title("polyharm")

    mode = 1
    if mode == 1:
        hist_trend_linear = new_analysis.hist(trend_linear, N, M)
        hist_trend_nonlinear = new_analysis.hist(trend_nonlinear, N, M)
        hist_noise = new_analysis.hist(noise, N, M)
        hist_my_noise = new_analysis.hist(my_noise, N, M)
        hist_harm = new_analysis.hist(harm, N, M)
        hist_polyharm = new_analysis.hist(polyharm, N, M)

        # Гистограммы
        ax[0, 1].plot(hist_trend_linear.keys(), hist_trend_linear.values())
        ax[1, 1].plot(hist_trend_nonlinear.keys(), hist_trend_nonlinear.values())
        ax[2, 1].plot(hist_noise.keys(), hist_noise.values())
        ax[3, 1].plot(hist_my_noise.keys(), hist_my_noise.values())
        ax[4, 1].plot(hist_harm.keys(), hist_harm.values())
        ax[5, 1].plot(hist_harm.keys(), hist_polyharm.values())
        ax[0, 1].set_title("linear trend hist")
        ax[1, 1].set_title("nonlinear trend hist")
        ax[2, 1].set_title("noise hist")
        ax[3, 1].set_title("myNoise hist")
        ax[4, 1].set_title("harm hist")
        ax[5, 1].set_title("polyharm hist")
    elif mode == 2:
        acf_trend_linear = new_analysis.acf(trend_linear, N)
        acf_trend_nonlinear = new_analysis.acf(trend_nonlinear, N)
        acf_noise = new_analysis.acf(noise, N)
        acf_my_noise = new_analysis.acf(my_noise, N)
        acf_harm = new_analysis.acf(harm, N)
        acf_polyharm = new_analysis.acf(polyharm, N)

        # АКФ
        ax[0, 1].plot(acf_trend_linear)
        ax[1, 1].plot(acf_trend_nonlinear)
        ax[2, 1].plot(acf_noise)
        ax[3, 1].plot(acf_my_noise)
        ax[4, 1].plot(acf_harm)
        ax[5, 1].plot(acf_polyharm)
        ax[0, 1].set_title("linear trend acf")
        ax[1, 1].set_title("nonlinear trend acf")
        ax[2, 1].set_title("noise acf")
        ax[3, 1].set_title("myNoise acf")
        ax[4, 1].set_title("harm acf")
        ax[5, 1].set_title("polyharm acf")

    plt.show()

main()