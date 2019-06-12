import os
from os import listdir
files = os.listdir('/ml/')

dictionary = {}
from PIL import Image
n=0
for i in files:
    number = int(i[7:].split(".")[0])
    colors = len(Image.open("ml/"+i,mode="r").getcolors(maxcolors=9999999))
    dictionary[number] = colors
    print(n)
    n+=1
    
import pandas as pd
keys = list(dictionary.keys())
vals = list(dictionary.values())
data = list(zip(keys,vals))
df_color = pd.DataFrame(data,columns=["num","color_count"])
df_color.to_csv("color.csv")

#identifies default avatars for twitter profile images(they use 184 colors)

from IPython.display import Image, display
n=0
for i in dictionary:
    if dictionary[i] == 184:
        print(dictionary[i])
        display(Image(filename='/ml/outfile'+str(i)+'.png'))
        n+=1
print(n)


