import matplotlib.pyplot as plt

from classes.model import Model

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True


def main():
    new_model = Model()

    N = 10 ** 3
    A0 = 5
    f0 = 50
    dt = 0.001

    trend = new_model.trend_linear(N, 0.3, 20)
    exp_trend = new_model.exp(N, 0.005, 10)
    harm = new_model.harm(N, A0, f0, dt)
    noise = new_model.noise(N, 10)
    addSignal_1 = new_model.addModel(trend, harm, N)
    addSignal_2 = new_model.addModel(exp_trend, noise, N)
    multSignal_1 = new_model.multModel(trend, harm, N)
    multSignal_2 = new_model.multModel(exp_trend, noise, N)

    fig, ax = plt.subplots(nrows=2, ncols=2)
    fig.suptitle("Задание 8", fontsize=15)
    ax[0, 0].plot(addSignal_1)
    ax[1, 0].plot(multSignal_1)
    ax[0, 1].plot(addSignal_2)
    ax[1, 1].plot(multSignal_2)
    ax[0, 0].set_title("add_harm")
    ax[1, 0].set_title("mult_harm")
    ax[0, 1].set_title("add_exp")
    ax[1, 1].set_title("mult_exp")
    plt.show()

main()