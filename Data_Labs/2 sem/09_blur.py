from classes.in_out import IN_OUT
from classes.proccessing import Proccessing
from classes.analysis import Analysis
from classes.model import Model
import matplotlib.pyplot as plt
import numpy as np


def main(mode):

    if mode == 0:
        new_model = Model()

        N = 10 ** 3  # число точек
        M = 1000  #
        a = 30  # степень экспаненты
        f = 7  # частота гармонического процесса
        R = 1  # амплитуда импульсов
        Rs = 0.1  # разброс пиков
        dt = 0.005  # шаг

        h = new_model.cardiogram(N, f, dt, a)
        s = [0] * N
        s[100] = 1
        s[230] = 0.95
        s[500] = 1.05
        s[700] = 1
        convolution = new_model.convolModel(h, s, N, M)
        fft = np.fft.fft(convolution) / np.fft.fft(h)
        ifft = np.fft.ifft(fft)

        # Построение графиков
        fig, ax = plt.subplots(nrows=4, ncols=1)
        fig.suptitle("Обратная фильтрация", fontsize=15)
        ax[0].plot(h)
        ax[1].plot(s)
        ax[2].plot(convolution)
        ax[3].plot(ifft)
        ax[0].set_title("функция сердечной мышцы")
        ax[1].set_title("управляющая функция")
        ax[2].set_title("кардиограмма")
        ax[3].set_title("восстановленная функция")
        plt.show()

    elif mode == 1:
        # Определение разрешения изображения
        height = 185
        width = 259

        # Пусть к исходному изображению
        name = 'blur259x185L.dat'
        path = './Media/lab№9/' + name

        # Задающая функция
        kern_name = 'kern64L.dat'
        kern_path = './Media/lab№9/' + kern_name

        # Чтение исходного изображения
        img_source = np.fromfile(path, dtype=np.float32)
        img_transform = np.reshape(img_source, (height, width))

        # Чтение задающей функции
        kern = np.fromfile(kern_path, dtype=np.float32)
        shape = (height, width)
        for i in range(kern.size, shape[1]):
            kern = np.append(kern, 0)

        # Построчная фильтрация
        img_blur = img_transform.copy()
        for row in range(height):
            fft = np.fft.fft(img_transform[row]) / np.fft.fft(kern)
            img_blur[row] = np.fft.ifft(fft)

        # # Прямое 2D преобразование Фурье
        # img_fft2D = np.fft.ifftshift(img_transform)
        # img_fft2D = np.fft.fft2(img_fft2D) / np.fft.fft2(kern)
        # img_fft2D = np.fft.fftshift(img_fft2D)
        #
        # # Обратное 2D преобразование Фурье
        # img_ifft2D = np.fft.ifftshift(img_fft2D)
        # img_ifft2D = np.fft.ifft2(img_ifft2D)
        # img_ifft2D = np.fft.fftshift(img_ifft2D)

        # Вывод изображений
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 7))
        fig.suptitle("Изображение " + name + "", fontsize=15)
        # Изображения
        ax[0].imshow(img_transform, cmap='gray')
        ax[1].imshow(img_blur, cmap='gray')
        ax[0].set_axis_off()
        ax[1].set_axis_off()
        # Подписи изображений
        ax[0].set_title("Исходное изображение")
        ax[1].set_title("Восстановленное")

        plt.show()


main(1)
