from IPython.display import Image, display
import urllib.request
from PIL import Image as img
import pandas as pd

df = pd.read_csv('update.csv')
print('got df')

# for i in list(df["profile_image_url"]):
#     print(i)
import os
try:
    os.mkdir("ml")
except:
    print("folder already exists...")
    
import face_recognition

n = 0
for i in list(df["profile_image_url"]):
    try:
        urllib.request.urlretrieve(i, r'ml/out.png')
        detection = face_recognition.load_image_file("ml/out.png")
        if face_recognition.face_locations(detection):
            df.at[n,"face_detection"] = 1
        else:
            df.at[n,"face_detection"] = 0
    except:
        df.at[n,"face_detection"] = 999
    n+=1
    print(n,face_recognition.face_locations(detection))
df.to_csv('update.csv')

clean = df[df.face_detection !=999.0]
clean = clean[clean.color_number != 184]
clean.to_csv("clean_data.csv")

logos = clean[(clean.color_number <=10000) & (clean.face_detection != 1)]

###view your images in jupyter###
from IPython.display import Image, display
import urllib.request
import urllib

n=0
for imageName in list(logos["profile_image_url"]):
    print(imageName)
    try:
        urllib.request.urlretrieve(imageName,'ml/test.png')
        display(Image(filename='ml/test.png'))
        n+=1
    except:
        print('error')
