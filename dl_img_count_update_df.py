from IPython.display import Image, display
import urllib.request
from PIL import Image as img
import pandas as pd

#download image from url, count colors, update dataframe

df = pd.read_excel('twitter_followers_detailed.xlsx')
print('got df')
n = 0
for imageName in list(df["profile_image_url"]):
    try:
        urllib.request.urlretrieve(imageName, '/ml/out.png')
        colors = len(img.open("ml/out.png",mode="r").getcolors(maxcolors=9999999))
        df["color_number"] = colors
    except:
        df["color_number"] = "image_not_found"
    n+=1
    print(n)
df.to_csv('update.csv')
