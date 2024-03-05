import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import re
import random

fig, ax = plt.subplots(nrows= 1 , ncols= 1 )
fig.suptitle('Trends with noise and shift ability')

a = 1
b = 1
x1 = -1
x2 = 1
shift = 0
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

def shift(dx):
    global shift
    global pattern
    if re.match(pattern, dx):
        shift = float(dx)
    else:
        print('incorrect value of shift')

def draw(event):
    ax.cla()

    t = np.linspace(-5, 5, 1000)
    x = np.sin(t * a)*b + noise
    for i in range(1000):
        if (t[i] > -1) and (t[i] < 1):
            x[i] += shift
    for i in range(M):
        x[t_1[i]] += sampl[i]

    ax.plot(t, x)
    plt.show()

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

# Shift Button
axes_textbox_shift = plt.axes([0.55, 0.01, 0.1, 0.05])
textbox_title_shift = TextBox(axes_textbox_shift, "shift")
textbox_title_shift.on_text_change(shift)
textbox_title_shift.on_submit(shift)

# draw Button
axbutton = fig.add_axes([0.8, 0.01, 0.1, 0.05])
btn = Button(axbutton, 'Draw')
if btn.on_clicked(draw):
    plt.clf()

# default graphs
N = 1000
R = 0.1
left_border = -5
right_border = 5
t = np.linspace(left_border, right_border, N)

# noise def
rnd = np.random.randint(10, size=(N))
noise = [i for i in range(N)]
for i in noise:
    noise[i] = ((((rnd[i] - min(rnd))/(max(rnd)-min(rnd)))-0.5)*2*R) % 0.5

x = np.sin(t * a)*b + noise

# spikes def
M = 6
R_spikes = 0.8
Rs = 0.1 * R_spikes
sampl = np.random.uniform(low=-Rs, high=Rs, size=(M,))
signs = np.random.randint(2, size=M)
for i in range(M):
    if signs[i] == 0:
        signs[i] = -1
    sampl[i] += R_spikes*signs[i]
t_1 = random.sample(list(range(1, N+1)), M)
for i in range(M):
    x[t_1[i]] += sampl[i]

ax.plot(t, x)

plt.show()