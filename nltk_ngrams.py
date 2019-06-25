from nltk import word_tokenize
with open('tweets.txt','r',encoding="latin1") as myfile:
    string=myfile.read().replace('\n', '')

tokens = word_tokenize(string)
text = nltk.Text(tokens)

#array is the tuple of ngrams, array2 is the count of appearances, can be zipped into a dataframe
array =[]
array2 =[]
bgs = nltk.ngrams(tokens,6)
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
    if v >10:
        print(k,v)
