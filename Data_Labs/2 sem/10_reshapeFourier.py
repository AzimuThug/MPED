from classes.in_out import IN_OUT
from classes.proccessing import Proccessing
from classes.model import Model
import matplotlib.pyplot as plt
import numpy as np


def main(mode):
    # Пусть к исходному изображению
    global img_ifft2D_1, img_ifft2D
    name = 'grace.jpg'
    path = './Media/' + name

    # Чтение исходного изображения
    img_source = IN_OUT.readJPG(path)

    # Определение разрешения изображения
    height = img_source.shape[0]
    width = img_source.shape[1]

    # Коэффициент изменения разрешения
    N = 1.2
    M = 1.2

    # Разрешение итоговое
    height_1 = int(height * N)
    width_1 = int(width * M)

    height_2 = int(height / N)
    width_2 = int(width / M)

    # Прямое 2D преобразование Фурье
    img_fft2D = np.fft.ifftshift(img_source)
    img_fft2D = np.fft.fft2(img_fft2D)
    img_fft2D = np.fft.fftshift(img_fft2D)

    # Увеличение изображения
    if mode == 0:
        # Start/Stop
        height_start = int((height_1 - height) / 2)
        width_start = int((width_1 - width) / 2)

        img_ifft2D = np.zeros((height_1, width_1), dtype=complex)
        # img_ifft2D[:, (height - width) / 2:(height + width) / 2] = img_fft2D
        for i in range(height_start, height + height_start):
            for j in range(width_start, width + width_start):
                img_ifft2D[i][j] = img_fft2D[i - height_start][j - width_start]
    # Уменьшение изображения
    elif mode == 1:
        # Start/Stop
        height_start = int((height - height_2) / 2)
        width_start = int((width - width_2) / 2)

        img_ifft2D_1 = img_fft2D.copy()
        new_model = Model()
        fc = 0.5 / N
        m = 1
        M_1 = 2 * m + 1
        N_1 = width  # 480
        N_2 = height  # 360
        dt = 1

        # ФНЧ
        low_pass_filter = Proccessing.lpf_reverse(Proccessing.lpf(fc, m, dt))

        # Построчная свертка с ФНЧ
        for i in range(0, height):
            img_ifft2D_1[i] = new_model.convolModel(img_ifft2D_1[i], low_pass_filter, N_1, M_1)
            img_ifft2D_1[i] = np.roll(img_ifft2D_1[i], -m)

        img_ifft2D_1 = np.rot90(img_ifft2D_1)
        for i in range(0, width):
            img_ifft2D_1[i] = new_model.convolModel(img_ifft2D_1[i], low_pass_filter, N_2, M_1)
            img_ifft2D_1[i] = np.roll(img_ifft2D_1[i], -m)

        img_ifft2D_1 = np.rot90(img_ifft2D_1, -1)
        img_ifft2D = np.zeros((height_2, width_2), dtype=complex)
        for i in range(0, height_2):
            for j in range(0, width_2):
                img_ifft2D[i][j] = img_ifft2D_1[i + height_start][j + width_start]

    # Обратное 2D преобразование Фурье
    img_ifft2D = np.fft.ifftshift(img_ifft2D)
    img_ifft2D = np.fft.ifft2(img_ifft2D)
    img_ifft2D = np.fft.fftshift(img_ifft2D)

    print(f"Исходный размер: {img_source.shape}")
    print(f"Итоговый размер: {img_ifft2D.shape}")

    # Вывод изображений
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 7))
    fig.suptitle("Изображение " + name + "", fontsize=15)
    # Изображения
    ax[0].imshow(img_source, cmap='gray')
    ax[1].imshow(abs(img_fft2D), cmap='gray')
    ax[2].imshow(abs(img_ifft2D), cmap='gray')
    # Подписи изображений
    ax[0].set_title("Исходное изображение")
    ax[1].set_title("ППФ")
    ax[2].set_title(f"Уменьшенное в {N} раз изображение")

    plt.show()

main(1)
