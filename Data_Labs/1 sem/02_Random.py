import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import re
import math
import time

fig, ax = plt.subplots(nrows= 2 , ncols= 1 )
fig.suptitle('Trends with noise')

a = 1
b = 1
pattern = r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'

def submit_a(inp):
    global a
    global pattern
    if re.match(pattern, inp):
        a = float(inp)
    else:
        print('incorrect value of a')

def submit_b(inp):
    global b
    global pattern
    if re.match(pattern, inp):
        b = float(inp)
    else:
        print('incorrect value of b')

def draw(event):
    ax[0].cla()
    ax[1].cla()

    t = np.linspace(-100, 100, 1000)
    x_1 = -t * a + b + noise
    x_2 = -t * a + b + my_noise

    ax[0].plot(t, x_1)
    ax[1].plot(t, x_2)
    plt.show()

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

# a parameter Button
axes_textbox_a = plt.axes([0.13, 0.01, 0.1, 0.05])
textbox_title_a = TextBox(axes_textbox_a, "a")
textbox_title_a.on_text_change(submit_a)
textbox_title_a.on_submit(submit_a)

# b parameter Button
axes_textbox_b = plt.axes([0.33, 0.01, 0.1, 0.05])
textbox_title_b = TextBox(axes_textbox_b, "b")
textbox_title_b.on_text_change(submit_b)
textbox_title_b.on_submit(submit_b)

# draw Button
axbutton = fig.add_axes([0.8, 0.01, 0.1, 0.05])
btn = Button(axbutton, 'Draw')
if btn.on_clicked(draw):
    plt.clf()

# default graphs
N = 1000
R = 10
left_border = -100
right_border = 100
t = np.linspace(left_border, right_border, N)
noise = np.random.randint(10, size=(N))
x_1 = -t * a + b + noise

my_noise = lin_rand_arr_flxd(time.time(),1001)
x_2 = -t * a + b + my_noise

ax[0].plot(t, x_1)
ax[1].plot(t, x_2)

plt.show()
