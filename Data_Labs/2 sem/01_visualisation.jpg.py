from classes.in_out import IN_OUT
from classes.proccessing import Proccessing

path = 'grace.jpg'
img_source = IN_OUT.readJPG(path)
img_shift = Proccessing.shift_2D(img_source, 30)
img_mult = Proccessing.multModel_2D(img_source, 1.3)
print(IN_OUT.infoJPG(img_source))
print(IN_OUT.infoJPG(img_mult))
# IN_OUT.showJPG(path, img_mult)
IN_OUT.writeJPG('shakal.jpg', img_mult)