import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

class IN_OUT:

    @staticmethod
    def readWAV(path):
        wav = wave.open(path, mode="r")
        (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
        print(wav.getparams())
        content = wav.readframes(nframes)
        samples = np.fromstring(content, dtype=types[sampwidth])
        return samples, nchannels, sampwidth, framerate, nframes

    @staticmethod
    def writeWAV(path, data, nchannels, sampwidth, framerate, nframes):
        wav = wave.open(path, mode="w")
        wav.setparams((nchannels, sampwidth, framerate, 0, 'NONE', 'not compressed'))
        for i in range(nframes * nchannels):
            wav.writeframes(data[i])
        wav.close()
