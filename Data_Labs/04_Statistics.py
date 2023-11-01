import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import re
import math
import time

fig, ax = plt.subplots(nrows= 2 , ncols= 1 )
fig.suptitle('Noise')

def lin_rand_arr_flxd(seed,size):
    m = 32768
    a = 23
    b = 12345
    if size==1:
        return math.ceil(math.fmod(a*math.ceil(seed)+b,m))
    r=[0 for i in range(size)]
    r[0]=math.ceil(seed)
    for i in range(1,size):
        r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
    return r[1:size]

# default graphs
N = 1000
R = 10
left_border = -100
right_border = 100
t = np.linspace(left_border, right_border, N)
noise = np.random.randint(10, size=(N))
x_1 = noise

my_noise = lin_rand_arr_flxd(time.time(),1001)
x_2 = my_noise

ax[0].plot(t, x_1)
ax[1].plot(t, x_2)

god_mode = 0 # 0 - noise/ 1 - my_noise

# min/max
minimum = min(x_1)
maximum = max(x_1)
print(minimum, maximum)

# СЗ
average = sum(x_1) / len(x_1)
print(average)

# D (variance) - S
D = sum(pow((x_1 - average), 2)) / len(x_1)
print(D)

# sigma
sigma = math.sqrt(D)
print(sigma)

# Ассиметрия и коэффициент ассиметрии
u3 = sum(pow((x_1 - average), 3)) / len(x_1)
y1 = u3 / pow(sigma, 3)
print(u3, y1)

# Эксцесс и куртозис
u4 = sum(pow((x_1 - average), 4)) / len(x_1)
y2 = u4 / pow(sigma, 4)
print(u4, y2)

# Средний квадрат
average_2 = sum(pow(x_1, 2)) / len(x_1)
print(average_2)

# Среднеквадратичная ошибка
e = math.sqrt(average_2)
print(e)

plt.show()
