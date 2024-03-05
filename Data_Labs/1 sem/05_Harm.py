import matplotlib.pyplot as plt
import time

from classes.model import Model

def main():
    new_model = Model()

    N = 1000
    A0 = 100
    f0 = 550
    A1 = 15
    f1 = 5
    A2 = 20
    f2 = 170
    dt = 0.001

    harm = new_model.harm(N, A0, f0, dt)
    # harm = new_model.shift(harm, 100, 0, 200)
    # harm = new_model.spikes(harm, N, 10, 100, time.time())
    polyharm = new_model.polyHarm(N, A0, f0, A1, f1, A2, f2, dt)

    fig, ax = plt.subplots(nrows=2, ncols=1)
    fig.suptitle('Harm and polyHarm')
    ax[0].plot(harm)
    ax[1].plot(polyharm)
    plt.show()

main()