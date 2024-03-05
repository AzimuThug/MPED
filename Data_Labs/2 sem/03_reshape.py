import numpy as np
import matplotlib.pyplot as plt
from classes.in_out import IN_OUT
from classes.proccessing import Proccessing

path = 'grace.jpg'
img_source = IN_OUT.readJPG(path)

img_resize_1_3 = Proccessing.resize(img_source, 1.3, 1)
img_resize_0_7 = Proccessing.resize(img_source, 0.7, 1)

IN_OUT.showJPG(path, img_resize_1_3)
IN_OUT.showJPG(path, img_resize_0_7)

data = IN_OUT.readXCR("./c12-85v_1Kx1K.xcr")
data = np.reshape(data, (1024, 1024))
data = np.rot90(data)

plt.imshow(data, cmap='gray')
plt.show()

# IN_OUT.writeJPG('shakal.jpg', img_source)