import nltk
import string
from nltk import word_tokenize
import pandas as pd

whitelist = []
exclude = set(string.punctuation)

def keywords(file,grams,count):
    with open(str(file),'r',encoding="latin1") as myfile:
        my_string=myfile.read().replace('\n', '')

    string = ''.join(ch for ch in my_string if ch not in exclude)

    tokens = word_tokenize(string)
    text = nltk.Text(tokens)

    #array is the tuple of ngrams, array2 is the count of appearances, array1 is joined tuples, array 1 & 2 can be zipped into a dataframe
    array =[]
    array2 =[]
    bgs = nltk.ngrams(tokens,int(grams))
    fdist = nltk.FreqDist(bgs)
    for k,v in fdist.items():
        if v > int(count):
            array.append(k)
            array2.append(v)

    array1 = []
    for i in range(len(array)):
        x = ' '.join(map(str,array[i]))
        array1.append(x)

    df = pd.DataFrame({'phrase':array1,'count': array2}).sort_values(by="count",ascending=False)
    for i in list(df['phrase']):
        whitelist.append(i.lower())
    df.to_csv('output_'+str(grams)+'.csv')
    
# keywords('logos.txt',1,100)
keywords('logos.txt',2,20)
keywords('logos.txt',3,10)

from nltk.corpus import stopwords

new_whitelist = []

stop = list(set(stopwords.words('english')))
additional_stop = []
stop += additional_stop
    
for i in whitelist:
    if (i.split(" ")[0] not in stop) & (i.split(" ")[1] not in stop):
        new_whitelist.append(i)
