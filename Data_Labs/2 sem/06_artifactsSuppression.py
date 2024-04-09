import numpy as np
import matplotlib.pyplot as plt
from classes.in_out import IN_OUT
from classes.analysis import Analysis
from classes.proccessing import Proccessing
from classes.model import Model


def main(mode):

    new_analysis = Analysis()

    # Пусть к исходному изображению
    name = 'c12-85v_1Kx1K.xcr'
    path = './Media/' + name

    # Размеры изображения
    height = 1024
    width = 1024

    # Открыть и повернуть изображение
    data = IN_OUT.readXCR(path, height, width)
    data = np.reshape(data, (height, width))
    data = np.rot90(data, 3)

    # Детектор
    if mode == 0:
        N = height
        dt = 1
        new_analysis = Analysis()

        # Номер строки от 0 до 1024
        i = 500

        # Строка i спектр исходный
        line_furier = np.fft.fft(data[i], N)

        # Строка i спектр производной
        line = data[i].copy()
        line = np.diff(line)
        line = np.append(line, line[-1])
        line_diff_furier = new_analysis.Fourier(line, N)

        # Строка i+10 производная
        line_2 = data[i+10].copy()
        line_2 = np.diff(line_2)
        line_2 = np.append(line_2, line_2[-1])

        # Строка i спектр АКФ производной
        line_acf = new_analysis.acf(line, N)
        line_acf_furier = np.fft.fft(line_acf)

        # Строка i спектр ВКФ производной
        line_ccf = new_analysis.ccf(line, line_2, N)
        line_ccf_furier = np.fft.fft(line_ccf)

        new_X_n = new_analysis.spectrFourier([i for i in range(N)], N, dt)

        # Вывод исходного и измененного изображений и их гистограмм
        fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(8, 10))
        fig.suptitle("Спектры " + name, fontsize=15)

        # Спектры
        ax[0].plot(new_X_n, line_furier)
        ax[1].plot(new_X_n, line_diff_furier)
        ax[2].plot(new_X_n, line_acf_furier)
        ax[3].plot(new_X_n, line_ccf_furier)
        ax[0].set_xlim([0, 1 / (dt * 2)])
        ax[1].set_xlim([0, 1 / (dt * 2)])
        ax[2].set_xlim([0, 1 / (dt * 2)])
        ax[3].set_xlim([0, 1 / (dt * 2)])
        # Подпись графиков
        ax[0].set_title(f"Спектр исходной {i} строки")
        ax[1].set_title("Спектр производной")
        ax[2].set_title("Спектр АКФ производных")
        ax[3].set_title("Спектр ВКФ производных")

        plt.show()

    # Подавитель
    if mode == 1:
        new_model = Model()

        # Берем часть изображения 256х256
        crop_img = np.empty((256, 256))
        for i in range(0, 256):
            crop_img[i] = data[i][0:256]

        # Параметры фильтра
        fc1 = 0.5
        fc2 = 1
        m = 16
        M = 2 * m + 1
        N = 256
        dt = 1

        # Режекторный фильтр
        band_stop_filter = Proccessing.bsf(fc1, fc2, m, dt)

        # Построчная свертка с режекторным фильтром
        for i in range(0, 256):
            crop_img[i] = new_model.convolModel(crop_img[i], band_stop_filter, N, M)
            for j in range(m):
                crop_img[i] = np.concatenate((crop_img[i][1:], crop_img[i][:1]))

        # Спектр строки после свертки
        line_furier = np.fft.fft(crop_img[0])
        new_X_n = new_analysis.spectrFourier([i for i in range(N)], N, dt)

        # Вывод спектра строки
        plt.plot(new_X_n, line_furier)
        plt.show()

        # Вывод изображения после свертки
        plt.imshow(crop_img, cmap='gray')
        plt.show()


main(0)