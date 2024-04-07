import numpy as np
import matplotlib.pyplot as plt
from classes.in_out import IN_OUT
from classes.proccessing import Proccessing

# Негатив для файлов *.jpg и *.xcr
data_xcr = IN_OUT.readXCR("./c12-85v_1Kx1K.xcr")
data_xcr = np.reshape(data_xcr, (1024, 1024))
data_xcr = Proccessing.negative(data_xcr)
plt.imshow(data_xcr, cmap='gray')
plt.show()

data_jpg = IN_OUT.readJPG("grace.jpg")
data_jpg = Proccessing.negative(data_jpg)
IN_OUT.showJPG("grace.jpg", data_jpg)

# Чтение файлов *.jpg для преобразования
img_1 = IN_OUT.readJPG('./Media/photo1.jpg')
img_2 = IN_OUT.readJPG('./Media/photo2.jpg')
img_3 = IN_OUT.readJPG('./Media/photo3.jpg')
img_4 = IN_OUT.readJPG('./Media/photo4.jpg')
img_HollywoodLC = IN_OUT.readJPG('./Media/HollywoodLC.jpg')

# Гамма-преобразование
# img_1 = Proccessing.gamma_transform(img_1, 2, 0.5)
# print('1')
# img_2 = Proccessing.gamma_transform(img_2, 2, 0.5)
# print('2')
# img_3 = Proccessing.gamma_transform(img_3, 1, 0.4)
# print('3')
# img_4 = Proccessing.gamma_transform(img_4, 2, 0.4)
# print('4')
# img_HollywoodLC = Proccessing.gamma_transform(img_HollywoodLC, 2, 0.7)
# print('5')

# Логарифмическое преобразование
img_1 = Proccessing.log_transform(img_1, 1)
print('1')
img_2 = Proccessing.log_transform(img_2, 2)
print('2')
img_3 = Proccessing.log_transform(img_3, 1)
print('3')
img_4 = Proccessing.log_transform(img_4, 2)
print('4')
img_HollywoodLC = Proccessing.log_transform(img_HollywoodLC, 1)
print('5')

fig, axs = plt.subplots(3, 2)
p1 = axs[0, 0].imshow(img_1, cmap='gray')
p2 = axs[0, 1].imshow(img_2, cmap='gray')
p3 = axs[1, 0].imshow(img_3, cmap='gray')
p4 = axs[1, 1].imshow(img_4, cmap='gray')
p5 = axs[2, 0].imshow(img_HollywoodLC, cmap='gray')

plt.show()




