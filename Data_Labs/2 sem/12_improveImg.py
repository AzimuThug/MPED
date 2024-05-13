from classes.in_out import IN_OUT
from classes.proccessing import Proccessing
import matplotlib.pyplot as plt
import numpy as np
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

    # # Маски Лапласиан
    # kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    # kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    # kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    # Выделение контуров изображений Градиентом
    img_improve = cv2.filter2D(img_source.copy(), -1, kernel)

    # Добавление результата к исходному изображению
    img_improve = cv2.addWeighted(
        img_source.copy(), 1, img_improve, -1, 0
    )
    # img_improve += img_source.copy()
    # Нормализация изображения
    min_val = np.min(img_improve)
    max_val = np.max(img_improve)
    img_improve = (img_improve - min_val) / (max_val - min_val)

    # Вывод изображений
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 7))
    fig.suptitle("Изображение " + name, fontsize=15)
    # Исходные изображения
    ax[0].imshow(img_source, cmap='gray')
    ax[1].imshow(img_improve, cmap='gray')
    ax[0].set_axis_off()
    ax[1].set_axis_off()
    # Подпись графиков
    ax[0].set_title("Исходное изображение")
    ax[1].set_title("Повышенная четкость")

    plt.show()


main()
