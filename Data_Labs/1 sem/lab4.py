import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import re

fig, ax = plt.subplots(nrows= 1 , ncols= 1 )
fig.suptitle('Multitrend')

a = 1
b = 1
x_1 = -2
x_2 = 2
pattern = r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'

def submit_a(inp):
    global x_1
    global pattern
    if re.match(pattern, inp):
        x_1 = float(inp)
    else:
        print('incorrect value of x_1')

def submit_b(inp):
    global x_2
    global pattern
    if re.match(pattern, inp):
        x_2 = float(inp)
    else:
        print('incorrect value of x_2')

def draw(event):
    pass

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
x_f = []

for i in range(100):
    if t[i] < x_1:
        x_f.append(-t[i] * a + b)
    elif t[i] > x_1 and t[i] < x_2:
        x_f.append( np.exp(-t[i] * a) * b)
    elif t[i] > x_2:
        x_f.append( t[i] * a + b)
ax.plot(t, x_f)

plt.show()
