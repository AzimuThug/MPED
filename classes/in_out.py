import wave
import numpy as np
import cv2
from classes.proccessing import Proccessing

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

    @staticmethod
    def readJPG(path):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        return img

    @staticmethod
    def writeJPG(path, img):
        cv2.imwrite(path, img)

    @staticmethod
    def showJPG(window_name, img):
        cv2.imshow(window_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def infoJPG(img):
        # img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        print(f'Resolution: {img.shape}\nNumber of pixels: {img.size}\n'
              f'Max value: {img.max()}, Min value: {img.min()}')

    # Чтение xcr файлов, возвращает одномерный массив uint8
    @staticmethod
    def readXCR(path):
        narray = np.zeros(1048576, dtype='ushort')
        with open(path, 'rb') as file:
            narray = np.fromfile(file, dtype=np.ushort, count=1048576, offset=2048)
        for i in range(narray.size):
            narray[i] = np.uint8(narray[i])
        return narray[::-1]

    @staticmethod
    def writeXCR(path, data):
        with open(path, "wb") as file:
            file.write(data)
