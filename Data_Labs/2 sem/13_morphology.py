from classes.in_out import IN_OUT
from classes.proccessing import Proccessing
from classes.model import Model
import matplotlib.pyplot as plt
import numpy as np
import time
import cv2


def main():
    # Пусть к исходному изображению
    # name = 'MODELimage.jpg'
    name = 'grace.jpg'
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

    kernel = np.ones((5, 5), np.uint8)

    # Эрозия изображений
    img_ed_source = cv2.erode(img_source.copy(), kernel, iterations=1)
    img_ed_multipleNoise = cv2.erode(img_multipleNoise, kernel, iterations=1)
    img_ed_filtered_avg = cv2.erode(img_filtered_average, kernel, iterations=1)
    img_ed_filtered_med = cv2.erode(img_filtered_median, kernel, iterations=1)

    # Дилатация изображений
    # img_ed_source = cv2.dilate(img_source.copy(), kernel, iterations=1)
    # img_ed_multipleNoise = cv2.dilate(img_multipleNoise, kernel, iterations=1)
    # img_ed_filtered_avg = cv2.dilate(img_filtered_average, kernel, iterations=1)
    # img_ed_filtered_med = cv2.dilate(img_filtered_median, kernel, iterations=1)

    # Пороговое преобразование
    ret, img_tr_source = cv2.threshold(img_source.copy(), 120, 255, cv2.THRESH_BINARY)
    ret, img_tr_multipleNoise = cv2.threshold(img_multipleNoise.copy(), 120, 255, cv2.THRESH_BINARY)
    ret, img_tr_filtered_avg = cv2.threshold(img_filtered_average.copy(), 120, 255, cv2.THRESH_BINARY)
    ret, img_tr_filtered_med = cv2.threshold(img_filtered_median.copy(), 120, 255, cv2.THRESH_BINARY)

    # Выделение контуров изображений
    img_outline_source = img_ed_source - img_source
    img_outline_multipleNoise = img_ed_multipleNoise - img_multipleNoise
    img_outline_filtered_avg = img_ed_filtered_avg - img_filtered_average
    img_outline_filtered_med = img_ed_filtered_med - img_filtered_median

    # Вывод изображений
    fig, ax = plt.subplots(nrows=4, ncols=3, figsize=(10, 7))
    fig.suptitle("Изображение " + name, fontsize=15)
    # Исходные изображения
    ax[0, 0].imshow(img_tr_source, cmap='gray')
    ax[1, 0].imshow(img_tr_multipleNoise, cmap='gray')
    ax[2, 0].imshow(img_tr_filtered_avg, cmap='gray')
    ax[3, 0].imshow(img_tr_filtered_med, cmap='gray')
    ax[0, 0].set_axis_off()
    ax[1, 0].set_axis_off()
    ax[2, 0].set_axis_off()
    ax[3, 0].set_axis_off()
    # Эрозия/Дилатация изображений
    ax[0, 1].imshow(img_ed_source, cmap='gray')
    ax[1, 1].imshow(img_ed_multipleNoise, cmap='gray')
    ax[2, 1].imshow(img_ed_filtered_avg, cmap='gray')
    ax[3, 1].imshow(img_ed_filtered_med, cmap='gray')
    ax[0, 1].set_axis_off()
    ax[1, 1].set_axis_off()
    ax[2, 1].set_axis_off()
    ax[3, 1].set_axis_off()
    # Контуры изображений
    ax[0, 2].imshow(img_outline_source, cmap='gray')
    ax[1, 2].imshow(img_outline_multipleNoise, cmap='gray')
    ax[2, 2].imshow(img_outline_filtered_avg, cmap='gray')
    ax[3, 2].imshow(img_outline_filtered_med, cmap='gray')
    ax[0, 2].set_axis_off()
    ax[1, 2].set_axis_off()
    ax[2, 2].set_axis_off()
    ax[3, 2].set_axis_off()
    # Подпись графиков
    ax[0, 0].set_title("без шумов")
    ax[1, 0].set_title("смесь шумов")
    ax[2, 0].set_title("усредняющий фильтр")
    ax[3, 0].set_title("медианный фильтр")
    ax[0, 1].set_title("Эрозия")
    ax[1, 1].set_title("Эрозия")
    ax[2, 1].set_title("Эрозия")
    ax[3, 1].set_title("Эрозия")
    ax[0, 2].set_title("Контур")
    ax[1, 2].set_title("Контур")
    ax[2, 2].set_title("Контур")
    ax[3, 2].set_title("Контур")

    plt.show()


main()
