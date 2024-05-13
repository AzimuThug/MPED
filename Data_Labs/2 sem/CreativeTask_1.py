import numpy as np
import cv2
import matplotlib.pyplot as plt
from classes.proccessing import Proccessing

name = 'brain-V_x256.bin'
# name = 'brain-H_x512.bin'
# name = 'spine-H_x256.bin'
# name = 'spine-V_x512.bin'
path = './Media/MRI/' + name
h = w = 512

# Считываем снимок
with open(path, 'rb') as file:
    narray = np.fromfile(file, dtype=np.ushort, count=h * w, offset=0)
    source_image = np.reshape(narray, (h, w))
    tmp = source_image.copy()

# Негатив
neg = Proccessing.negative(source_image.copy())

# Оптимальное градационное преобразование
step_1 = Proccessing.gradTransform(tmp.ravel())
step_1 = np.reshape(step_1, (h, w))

# Удаление шума
step_2 = Proccessing.clear(step_1.copy(), 115)
# step_2 = Proccessing.average_filter(step_2, 3, 3)
# step_2 = Proccessing.median_filter(step_2, 3)

# Маски Первита
# kernel = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
# kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
# kernel = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
# kernel = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])

# # Маски Собела
# kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
# kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
# kernel = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])

# Маски Лапласиан
# kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
# kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
# kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
# kernel_1 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# Повышение четкости фильтрацией
step_3, filtered = Proccessing.improve(step_2.copy(), kernel, 2, -1)

# Повышение четкости фильтрацией дилатацией
# kernel = np.ones((5, 5), np.uint8)
# img_ed_source = cv2.dilate(step_2.copy(), kernel, iterations=1)
# filtered = img_ed_source - step_2
# step_3 = cv2.addWeighted(
#     step_2.copy(), 1, filtered, -1, 0
# )

# Вывод изображений
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(10, 7))
fig.suptitle("Изображение " + name, fontsize=15)
# Пошаговый вывод изображений
ax[0, 0].imshow(source_image, cmap='gray')
ax[0, 1].imshow(neg, cmap='gray')
ax[0, 2].imshow(step_1, cmap='gray')
ax[1, 0].imshow(step_2, cmap='gray')
ax[1, 1].imshow(step_3, cmap='gray')
ax[1, 2].imshow(filtered, cmap='gray')
ax[0, 0].set_axis_off()
ax[0, 1].set_axis_off()
ax[0, 2].set_axis_off()
ax[1, 0].set_axis_off()
ax[1, 1].set_axis_off()
ax[1, 2].set_axis_off()

# Подпись графиков
ax[0, 0].set_title("Исходное")
ax[0, 1].set_title("Негатив")
ax[0, 2].set_title("Шаг 1")
ax[1, 0].set_title("Шаг 2")
ax[1, 1].set_title("Шаг 3")
ax[1, 2].set_title("Контур")

plt.show()