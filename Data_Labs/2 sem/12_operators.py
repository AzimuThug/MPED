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
    name = 'birches.jpg'
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

    # Маски Первита
    # kernel_1 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    # kernel_2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    # kernel_3 = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
    # kernel_4 = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])

    # # Маски Собела
    # kernel_1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    # kernel_2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # kernel_3 = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
    # kernel_4 = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])

    # # Маски Лапласиан
    # kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    # kernel = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
    # kernel = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])

    # Выделение контуров изображений Градиентом
    img_outline_source = cv2.filter2D(img_source.copy(), -1, kernel)
    img_outline_multipleNoise = cv2.filter2D(img_multipleNoise.copy(), -1, kernel)
    img_outline_filtered_avg = cv2.filter2D(img_filtered_average.copy(), -1, kernel)
    img_outline_filtered_med = cv2.filter2D(img_filtered_median.copy(), -1, kernel)

    # Выделение контуров изображений Градиентом на исходном
    # img_outline_source = cv2.filter2D(img_source.copy(), -1, kernel_1)
    # img_outline_multipleNoise = cv2.filter2D(img_source.copy(), -1, kernel_2)
    # img_outline_filtered_avg = cv2.filter2D(img_source.copy(), -1, kernel_3)
    # img_outline_filtered_med = cv2.filter2D(img_source.copy(), -1, kernel_4)

    # Вывод изображений
    fig, ax = plt.subplots(nrows=4, ncols=2, figsize=(10, 7))
    fig.suptitle("Изображение " + name, fontsize=15)
    # Исходные изображения
    ax[0, 0].imshow(img_source, cmap='gray')
    ax[1, 0].imshow(img_filtered_average, cmap='gray')
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
    ax[0, 0].set_title("маска 1")
    ax[1, 0].set_title("маска 2")
    ax[2, 0].set_title("маска 3")
    ax[3, 0].set_title("маска 4")
    ax[0, 1].set_title("")
    ax[1, 1].set_title("")
    ax[2, 1].set_title("")
    ax[3, 1].set_title("")

    plt.show()


main()
