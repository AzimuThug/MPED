import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import re

fig, ax = plt.subplots(nrows= 2 , ncols= 2 )
fig.suptitle('Some trends')

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
    ax[0,0].cla()
    ax[0,1].cla()
    ax[1,0].cla()
    ax[1,1].cla()

    t = np.linspace(-5, 5, 100)
    x_exp1 = np.exp(-t * a)*b
    x_exp2 = np.exp(t * a)*b
    x_lin1 = -t * a + b
    x_lin2 = t * a + b

    ax[0, 0].plot(t, x_exp1)
    ax[0, 1].plot(t, x_exp2)
    ax[1, 0].plot(t, x_lin1)
    ax[1, 1].plot(t, x_lin2)
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

# draw Button
axbutton = fig.add_axes([0.8, 0.01, 0.1, 0.05])
btn = Button(axbutton, 'Draw')
if btn.on_clicked(draw):
    plt.clf()

# default graphs
t = np.linspace(-5, 5, 100)

x_exp1 = np.exp(-t * a)*b
x_exp2 = np.exp(t * a)*b
x_lin1 = -t * a + b
x_lin2 = t * a + b

ax[0, 0].plot(t, x_exp1)
ax[0, 1].plot(t, x_exp2)
ax[1, 0].plot(t, x_lin1)
ax[1, 1].plot(t, x_lin2)

plt.show()
