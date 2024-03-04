import matplotlib.pyplot as plt

from classes.model import Model
from classes.proccessing import Proccessing

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True


def main():
    new_model = Model()

    N = 10 ** 3 # число точек
    A0 = 5    # амплитуда первой частоты
    f0 = 1     # первая частота
    A1 = 25     # амплитуда второй частоты
    f1 = 130    # вторая частоота
    A2 = 30     # амплитуда второй частоты
    f2 = 15     # вторая частота
    dt = 0.001  # постоянная времени

    linear = new_model.trend_linear(N, 3, 0)
    harm = new_model.harm(N, A0, f0, dt)
    non_linear = new_model.exp(N, 0.006, 1)
    polyharm = new_model.polyHarm(N, A0, f0, A1, f1, A2, f2, dt)
    noise = new_model.noise(N, 1)

    addSignal_1 = new_model.addModel(non_linear, harm, N)
    addSignal_3 = Proccessing.antiTrendNonLinear(addSignal_1, N, 200)
    # addSignal_3 = Proccessing.antiNoise(addSignal_1, N, 100)

    # harm_source = Proccessing.antiShift(harm)
    # noise_source = Proccessing.antiShift(noise)
    # harm_source = Proccessing.antiSpike(harm_source)
    # noise_source = Proccessing.antiSpike(noise_source)

    fig, ax = plt.subplots(nrows=1, ncols=2)
    fig.suptitle("Задание 10", fontsize=15)

    ax[0].plot(addSignal_1)
    ax[1].plot(addSignal_3)

    ax[0].set_title("harm")
    ax[1].set_title("harm_after")

    plt.show()

main()