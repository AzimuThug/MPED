import numpy as np
import matplotlib.pyplot as plt
from classes.in_out import IN_OUT

data = IN_OUT.readXCR("./c12-85v_1Kx1K.xcr")
data = np.reshape(data, (1024, 1024))

plt.imshow(data, cmap='gray')
plt.show()

print(data.ndim)
print(data.size)
print(data[100])

# IN_OUT.writeXCR('out.bin', data)


