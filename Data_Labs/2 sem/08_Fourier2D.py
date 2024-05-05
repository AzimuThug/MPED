from classes.in_out import IN_OUT
from classes.proccessing import Proccessing
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Пусть к исходному изображению
    name = 'grace.jpg'
    path = './Media/' + name

    # Чтение исходного изображения
    img_source = IN_OUT.readJPG(path)

    # Определение разрешения изображения
    height = img_source.shape[0]
    width = img_source.shape[1]

    # Прямое 2D преобразование Фурье
    img_fft2D = np.fft.ifftshift(img_source)
    img_fft2D = np.fft.fft2(img_fft2D)
    img_fft2D = np.fft.fftshift(img_fft2D)

    # Обратное 2D преобразование Фурье
    img_ifft2D = np.fft.ifftshift(img_fft2D)
    img_ifft2D = np.fft.ifft2(img_ifft2D)
    img_ifft2D = np.fft.fftshift(img_ifft2D)

    # Повышение яркости для улучшения качества картинки
    img_fft2D = Proccessing.gamma_transform(img_fft2D, 1, 0.1)

    # Вывод изображений
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 7))
    fig.suptitle("Изображение " + name + "", fontsize=15)
    # Изображения
    ax[0].imshow(img_source, cmap='gray')
    ax[1].imshow(abs(img_fft2D), cmap='gray')
    ax[2].imshow(abs(img_ifft2D), cmap='gray')
    ax[0].set_axis_off()
    ax[1].set_axis_off()
    ax[2].set_axis_off()
    # Подписи изображений
    ax[0].set_title("Исходное изображение")
    ax[1].set_title("ППФ")
    ax[2].set_title("ОПФ")

    plt.show()


main()
