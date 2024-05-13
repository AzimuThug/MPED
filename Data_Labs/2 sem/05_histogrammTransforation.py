from classes.in_out import IN_OUT
from classes.proccessing import Proccessing
from classes.analysis import Analysis
import matplotlib.pyplot as plt
import numpy as np


def main(mode=0):
    # Пусть к исходному изображению
    name = 'HollywoodLC.jpg'
    path = './Media/' + name

    # Чтение исходного изображения
    img_source = IN_OUT.readJPG(path)

    # Определение разрешения изображения
    height = img_source.shape[0]
    width = img_source.shape[1]

    if mode == 0:
        # Изменение исходного изображения
        img_change = img_source.copy()  # Присваивание без создания ссылки на объект
        print(len(img_change.ravel()))
        img_transform = Proccessing.gradTransform(img_change.ravel())
        img_transform = np.reshape(img_transform, (height, width))

        # Расчет гистограммы для исходного и измененного изображения
        hist, bins = np.histogram(img_source.ravel(), bins=256, range=[0, 256], density=True)
        hist_2, bins_2 = np.histogram(img_transform, bins=256, range=[0, 256], density=True)

        # Вывод исходного и измененного изображений и их гистограмм
        fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 7))
        fig.suptitle("Гистограммы изображений", fontsize=15)
        # Картинки
        ax[0, 0].imshow(img_source, cmap='gray')
        ax[1, 0].imshow(img_transform, cmap='gray')
        ax[0, 0].set_axis_off()
        ax[1, 0].set_axis_off()
        # Гистограммы
        ax[0, 1].plot(bins[:-1], hist)
        ax[1, 1].plot(bins_2[:-1], hist_2)
        ax[0, 1].fill_between(bins[:-1], hist)
        ax[1, 1].fill_between(bins_2[:-1], hist_2)
        # Подпись графиков
        ax[0, 0].set_title("Исходное " + name)
        ax[1, 0].set_title("Измененное")
        ax[0, 1].set_title("Гистограмма исходного " + name)
        ax[1, 1].set_title("Гистограмма измененного")

    elif mode == 1:
        # Увеличение исходного изображения методом билинейной интерполяции
        img_change = img_source.copy()
        img_transform = Proccessing.resize(img_change, 2, 2)
        img_transform = Proccessing.resize(img_transform, 0.5, 2)

        # Разность исходного и полученного изображения
        img_diff = img_source - img_transform
        img_diff_1 = img_diff.copy()
        # Оптимальное градационное преобразование
        img_transform = Proccessing.gradTransform(img_change.ravel(), img_diff_1.ravel())
        img_transform = np.reshape(img_transform, (height, width))

        # Расчет гистограммы для исходного и измененного изображения
        hist, bins = np.histogram(img_source.ravel(), bins=256, range=[0, 256], density=True)
        hist_2, bins_2 = np.histogram(img_diff, bins=256, range=[0, 256], density=True)
        hist_3, bins_3 = np.histogram(img_transform, bins=256, range=[0, 256], density=True)

        # Вывод исходного и измененного изображений и их гистограмм
        fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(8, 10))
        fig.suptitle("Гистограммы изображений", fontsize=15)
        # Картинки
        ax[0, 0].imshow(img_source, cmap='gray')
        ax[1, 0].imshow(img_diff, cmap='gray')
        ax[2, 0].imshow(img_transform, cmap='gray')
        ax[0, 0].set_axis_off()
        ax[1, 0].set_axis_off()
        ax[2, 0].set_axis_off()
        # Гистограммы
        ax[0, 1].plot(bins[:-1], hist)
        ax[1, 1].plot(bins_2[:-1], hist_2)
        ax[2, 1].plot(bins_3[:-1], hist_3)
        ax[0, 1].fill_between(bins[:-1], hist)
        ax[1, 1].fill_between(bins_2[:-1], hist_2)
        ax[2, 1].fill_between(bins_3[:-1], hist_3)
        # Подпись графиков
        ax[0, 0].set_title("Исходное " + name)
        ax[1, 0].set_title("Разница изображений")
        ax[2, 0].set_title("Градационное преобразование")
        ax[0, 1].set_title("Гистограмма исходного " + name)
        ax[1, 1].set_title("Гистограмма разницы")
        ax[2, 1].set_title("Гистограмма преобразования")

    plt.show()


main(0)
