import matplotlib.pyplot as plt
from classes.in_out import IN_OUT
import numpy as np

plt.rcParams["figure.figsize"] = [20, 7.5]
plt.rcParams["figure.autolayout"] = True

file_name = "record"

def main():
    data_proccessed = []
    data, nchannels, sampwidth, framerate, nframes = IN_OUT.readWAV("./records/" + file_name + ".wav")

    for i in range(0, 18000):
        data_proccessed.append(data[i] / 3)

    for i in range(18000, nframes):
        data_proccessed.append(data[i] * 3)

    data_proccessed = np.array(data_proccessed, dtype=np.int16)

    fig, ax = plt.subplots(nrows=2, ncols=1)
    fig.suptitle("Задание 14", fontsize=15)
    ax[0].plot(data)
    ax[1].plot(data_proccessed)
    plt.show()

    IN_OUT.writeWAV("./records/" + file_name + "_out.wav", data_proccessed, nchannels, sampwidth, framerate, nframes)

main()