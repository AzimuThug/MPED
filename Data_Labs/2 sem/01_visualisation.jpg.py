from classes.in_out import IN_OUT
from classes.proccessing import Proccessing
import matplotlib.pyplot as plt
import numpy as np

# Пусть к исходному изображению
name = 'HollywoodLC.jpg'
path = './Media/' + name

# Чтение исходного изображения
img_source = IN_OUT.readJPG(path)

# Изменение исходного изображения
img_change = img_source.copy() # Присваивание без создания ссылки на объект
img_shift = Proccessing.shift_2D(img_change, 100)
# img_mult = Proccessing.multModel_2D(img_source, 1.3)

# Расчет гистограммы для исходного и измененного изображения
hist, bins = np.histogram(img_source.ravel(), bins=256, range=[0,256], density=True)
hist_2, bins_2 = np.histogram(img_shift.ravel(), bins=256, range=[0,256], density=True)

# Отображение измененного изображения
# IN_OUT.showJPG(path, img_shift)

# Вывод исходного и измененного изображений и их гистограмм
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 7))
fig.suptitle("Гистограммы изображений", fontsize=15)
# Картинки
ax[0, 0].imshow(img_source, cmap='gray')
ax[1, 0].imshow(img_shift, cmap='gray')
ax[0, 0].set_axis_off()
ax[1, 0].set_axis_off()
# Гистограммы
ax[0, 1].plot(bins[:-1], hist)
ax[1, 1].plot(bins_2[:-1], hist_2)
ax[0, 1].fill_between(bins[:-1], hist)
ax[1, 1].fill_between(bins_2[:-1], hist_2)
# Подпись графиков
ax[0, 0].set_title("Исходное")
ax[1, 0].set_title("Измененное")
ax[0, 1].set_title("signal raw spectre")
ax[1, 1].set_title("signal spectre")

plt.show()
