import numpy as np
import matplotlib.pyplot as plt
from classes.in_out import IN_OUT

data = IN_OUT.readXCR("./Media/c12-85v_1Kx1K.xcr")
data = np.reshape(data, (1024, 1024))

crop_img = np.empty((256, 256))
for i in range(0, 256):
    crop_img[i] = data[i][0:256]

plt.imshow(crop_img, cmap='gray')
plt.show()

# plt.hist(data.ravel(), 256, [0,256])
# plt.show()