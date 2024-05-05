from classes.in_out import IN_OUT
from classes.proccessing import Proccessing
from classes.analysis import Analysis
from classes.model import Model
import matplotlib.pyplot as plt
import numpy as np
import time


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

    # Наложение случайного шума
    img_randomNoise = img_source.copy()
    for i in range(height):
        img_randomNoise[i] = img_randomNoise[i] + new_model.noise(width, 35)

    # Наложение импульсного шума
    img_impulseNoise = img_source.copy()
    for i in range(height):
        img_impulseNoise[i] = new_model.spikes(img_impulseNoise[i], width-1, 5, 255, time.time())

    # Наложение двух типов шумов
    img_multipleNoise = img_source.copy()
    for i in range(height):
        img_multipleNoise[i] = new_model.spikes(img_multipleNoise[i], width-1, 5, 200, time.time())
        img_multipleNoise[i] = img_multipleNoise[i] + new_model.noise(width, 30)

    # Убираем шум усредняющим фильтром
    img_without_randomNoise = Proccessing.average_filter(img_randomNoise, 5, 5)
    img_without_impulseNoise = Proccessing.average_filter(img_impulseNoise, 5, 5)
    img_without_multipleNoise = Proccessing.average_filter(img_multipleNoise, 5, 5)

    # Убираем шум медианным фильтром
    # img_without_randomNoise = Proccessing.median_filter(img_randomNoise, 5)
    # img_without_impulseNoise = Proccessing.median_filter(img_impulseNoise, 5)
    # img_without_multipleNoise = Proccessing.median_filter(img_multipleNoise, 5)

    # Вывод изображений
    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(10, 7))
    fig.suptitle("Изображение" + name + "с шумами и без (усредняющий фильтр=5)", fontsize=15)
    # Изображения с шумами
    ax[0, 0].imshow(img_randomNoise, cmap='gray')
    ax[1, 0].imshow(img_impulseNoise, cmap='gray')
    ax[2, 0].imshow(img_multipleNoise, cmap='gray')
    ax[0, 0].set_axis_off()
    ax[1, 0].set_axis_off()
    ax[2, 0].set_axis_off()
    # Изображения без шумов
    ax[0, 1].imshow(img_without_randomNoise, cmap='gray')
    ax[1, 1].imshow(img_without_impulseNoise, cmap='gray')
    ax[2, 1].imshow(img_without_multipleNoise, cmap='gray')
    ax[0, 1].set_axis_off()
    ax[1, 1].set_axis_off()
    ax[2, 1].set_axis_off()
    # Подпись графиков
    ax[0, 0].set_title("случайный шум")
    ax[1, 0].set_title("соль и перец")
    ax[2, 0].set_title("сложный шум")
    ax[0, 1].set_title("")
    ax[1, 1].set_title("")
    ax[2, 1].set_title("")

    plt.show()


main()
