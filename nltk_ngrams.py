from nltk import word_tokenize
#N-GRAMS are n length word phrases that appear in a text
#finding common n-grams in a text can help find keyword phrases that appear more frequently in a text
#this can help characterize texts

#### CONVERTING A CSV TO TXT
# import csv
# csv_file = raw_input('Enter the name of your input file: ')
# txt_file = raw_input('Enter the name of your output file: ')
# with open(txt_file, "w") as my_output_file:
#     with open(csv_file, "r") as my_input_file:
#         [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
#     my_output_file.close()

import nltk
import string
from nltk import word_tokenize
import pandas as pd

nltk.download('punkt')

with open('logos.txt','r',encoding="latin1") as myfile:
    my_string=myfile.read().replace('\n', '')

exclude = set(string.punctuation)
string = ''.join(ch for ch in my_string if ch not in exclude)

tokens = word_tokenize(string)
text = nltk.Text(tokens)

#array is the tuple of ngrams, array2 is the count of appearances, array1 is joined tuples, array 1 & 2 can be zipped into a dataframe
array =[]
array2 =[]

### length of n-grams is second argument to nltk.ngrams(tokens,length_goes_here)
bgs = nltk.ngrams(tokens,2)
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
    if v >10:
        array.append(k)
        array2.append(v)

array1 = []
for i in range(len(array)):
    x = ' '.join(map(str,array[i]))
    array1.append(x)
    
df = pd.DataFrame({'phrase':array1,'count': array2}).sort_values(by="count",ascending=False)
df.to_csv('output.csv')
