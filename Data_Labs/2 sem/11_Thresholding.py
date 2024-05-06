from classes.in_out import IN_OUT
from classes.proccessing import Proccessing
from classes.model import Model
import matplotlib.pyplot as plt
import numpy as np
import time
import cv2


def main():
    # Пусть к исходному изображению
    name = 'MODELimage.jpg'
    path = './Media/' + name

    # Чтение исходного изображения
    img_source = IN_OUT.readJPG(path)

    # Определение разрешения изображения
    height = img_source.shape[0]
    width = img_source.shape[1]

    new_model = Model()

    # Наложение двух типов шумов
    img_multipleNoise = img_source.copy()
    for i in range(height):
        img_multipleNoise[i] = new_model.spikes(img_multipleNoise[i], width-1, 6, 200, time.time())
        img_multipleNoise[i] = img_multipleNoise[i] + new_model.noise(width, 40)

    # Убираем шум усредняющим фильтром
    img_filtered_average = Proccessing.average_filter(img_multipleNoise, 5, 5)

    # Убираем шум медианным фильтром
    img_filtered_median = Proccessing.median_filter(img_multipleNoise, 5)

    # Выделение контуров изображений
    # img_outline_source = outline(img_source.copy())
    img_outline_multipleNoise = outline(img_multipleNoise.copy())
    img_outline_filtered_avg = outline(img_filtered_average.copy())
    img_outline_filtered_med = outline(img_filtered_median.copy())

    # Пороговое преобразование
    ret, img_outline_source = cv2.threshold(img_source.copy(), 120, 255, cv2.THRESH_BINARY)
    ret, img_outline_multipleNoise = cv2.threshold(img_outline_multipleNoise.copy(), 120, 255, cv2.THRESH_BINARY)
    ret, img_outline_filtered_avg = cv2.threshold(img_outline_filtered_avg.copy(), 120, 255, cv2.THRESH_BINARY)
    ret, img_outline_filtered_med = cv2.threshold(img_outline_filtered_med.copy(), 120, 255, cv2.THRESH_BINARY)

    # Вывод изображений
    fig, ax = plt.subplots(nrows=4, ncols=2, figsize=(10, 7))
    fig.suptitle("Изображение" + name, fontsize=15)
    # Исходные изображения
    ax[0, 0].imshow(img_source, cmap='gray')
    ax[1, 0].imshow(img_multipleNoise, cmap='gray')
    ax[2, 0].imshow(img_filtered_average, cmap='gray')
    ax[3, 0].imshow(img_filtered_median, cmap='gray')
    ax[0, 0].set_axis_off()
    ax[1, 0].set_axis_off()
    ax[2, 0].set_axis_off()
    ax[3, 0].set_axis_off()
    # Контуры изображений
    ax[0, 1].imshow(img_outline_source, cmap='gray')
    ax[1, 1].imshow(img_outline_multipleNoise, cmap='gray')
    ax[2, 1].imshow(img_outline_filtered_avg, cmap='gray')
    ax[3, 1].imshow(img_outline_filtered_med, cmap='gray')
    ax[0, 1].set_axis_off()
    ax[1, 1].set_axis_off()
    ax[2, 1].set_axis_off()
    ax[3, 1].set_axis_off()
    # Подпись графиков
    ax[0, 0].set_title("без шумов")
    ax[1, 0].set_title("смесь шумов")
    ax[2, 0].set_title("усредняющий фильтр")
    ax[3, 0].set_title("медианный фильтр")
    ax[0, 1].set_title("")
    ax[1, 1].set_title("")
    ax[2, 1].set_title("")
    ax[3, 1].set_title("")

    plt.show()

def outline(img):
    # Параметры фильтра
    fc = 0.01
    m = 16
    M = 2 * m + 1
    N = img.shape[1]
    dt = 1

    # ФНЧ / ФВЧ
    # filter = Proccessing.lpf_reverse(Proccessing.lpf(fc, m, dt))
    filter = Proccessing.hpf(fc, m, dt)

    new_model = Model()
    for i in range(0, img.shape[0]):
        img[i] = new_model.convolModel(img[i], filter, N, M)
        img[i] = np.roll(img[i], -m)

    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    return edged


main()
