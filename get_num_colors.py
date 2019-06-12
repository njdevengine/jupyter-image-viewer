from PIL import Image
x = PIL.Image.open('test.jpg',mode="r")
colors = x.getcolors(maxcolors=99999)
num_of_colors = len(colors)
