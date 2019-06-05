from IPython.display import Image, display
import urllib.request

n=0
for imageName in list(df["profile_image_url"]):
    try:
        urllib.request.urlretrieve(imageName, '/ml/outfile'+str(n)+'.png')
        display(Image(filename='/ml/outfile'+str(n)+'.png'))
        n+=1
    except:
        print('error')
