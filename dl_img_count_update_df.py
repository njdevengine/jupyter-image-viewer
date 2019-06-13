from IPython.display import Image, display
import urllib.request
from PIL import Image as img
import pandas as pd

df = pd.read_excel('twitter_followers_detailed.xlsx')
print('got df')
n = 0
for imageName in list(df["profile_image_url"]):
    try:
        urllib.request.urlretrieve(imageName, '/ml/out.png')
        colors = len(img.open("ml/out.png",mode="r").getcolors(maxcolors=9999999))
        df.at[n,"color_number"] = colors    
    except:
        df.at[n,"color_number"] = 0.01
    n+=1
    print(n)
df.to_csv('update.csv')
