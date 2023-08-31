from random import random

import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
# import these modules
from nltk.stem import PorterStemmer,WordNetLemmatizer

import string
# Import Module
import os
# Folder Path
path = "C:/Users/Irene/PycharmProjects/ML1/task1"
# Change the directory
os.chdir(path)
# Read text File
allwords = []
#
# a1 = open("task1/text_2.txt", "r")
# b1=a1.read()
# n1 = (b1.lower())
# n1 = n1.translate (str.maketrans ('', '', string.punctuation))
# n1 =''.join((x for x in n1 if not x.isdigit()))
# tokenizedText=word_tokenize(n1)
# tokensWithoutSW=[word for word in tokenizedText if not word in stopwords.words()]
# print(tokensWithoutSW)

from nltk.tokenize import word_tokenize

def read_text_file(file_path):
    initial = []
    with open(file_path, 'r') as f:
        b1=f.read()
        n1 = (b1.lower())
        n1 = n1.translate (str.maketrans ('', '', string.punctuation))
        n1 =''.join((x for x in n1 if not x.isdigit()))
        tokenizedText=word_tokenize(n1)
        tokensWithoutSW=[word for word in tokenizedText if not word in stopwords.words()]
        for w in tokensWithoutSW:
          ps = PorterStemmer()
          initial.append(ps.stem(w))

        #print(initial)
        allwords.append(initial)
        #print(tokensWithoutSW)

        # wordnet_lemmatizer = WordNetLemmatizer()
        # for w in tokensWithoutSW:
        #     initial.append(wordnet_lemmatizer.lemmatize(w))
        #     #print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))
        # print(initial)
        # print(tokensWithoutSW)

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"

        # call read text file function
        read_text_file(file_path)

ind =0
uniquewords = set()
while ind<len(allwords):
    uniquewords = uniquewords.union(set(allwords[ind]))
    ind+=1

#print(uniquewords)
# print(allwords)

dictslist = []
ind = 0
for a in allwords:
    number= dictslist.append(dict.fromkeys(uniquewords, 0))

    for wrd in a:
        dictslist[ind][wrd]+=1
    #print(dictslist[ind])
    ind+=1


def computeTF(dictslist, allwords):
    listdata=[]

    ind=0
    for numbers in dictslist:
     tfDict = {}
     bagOfWordsCount = len(allwords[ind])

     for word, count in numbers.items():
        tfDict[word] = count / float(bagOfWordsCount)
     listdata.append(tfDict)
     ind+=1

    return listdata

tf = computeTF(dictslist, allwords)
#print(tf)
#print(dictslist)

def computeIDF(dictslist):
    import math
    N = len(dictslist)
    idfDict = dict.fromkeys(dictslist[0].keys(), 0)

    for ind in dictslist:
        for word, val in ind.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

idf=computeIDF(dictslist)
#print(idf)



def computeTFIDF(tfBagOfWords, idfs):
    tfidfList= []
    ind=0
    for index in tfBagOfWords:
     tfidf={}
     for word, val in index.items():
        tfidf[word] = val * idfs[word]
        tfidfList.append(tfidf)
     return tfidfList

tfidf=computeTFIDF(tf,idf)
vec=[]
#print(tfidf)

for ind in tfidf:

    value =list(ind.values())
    vec.append(value)
print(vec)


def kmeans(vectors, k):
    centroids = random.sample(vectors, k)
    clusters = []
    n = 0
    while n < 100:
        clusters = [[] for x in range(k)]

        for file in vectors:
            distance = []
            for c in centroids:
                import math
                distance.append(math.dist(file, c))
            # print(distance)
            clusters[distance.index(min(distance))].append(file)

        centroids = []
        for cl in clusters:
            centroids.append(get_centroids(cl))

        n += 1
    return (centroids, clusters)









# this function encrypts the given text using the Caesar cipher algorithm
def encrypt(text, key):
  # create the list of alphabets
  alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

  # encrypt the text
  ciphertext = ''
  for ch in text.lower():
    if ch in alphabets:
      ciphertext += alphabets[(alphabets.index(ch) + key) % 26]
    else:
      ciphertext += ch

  return ciphertext

# this function decrypts the given text using the Caesar cipher algorithm
def decrypt(ciphertext, key):
  # create the list of alphabets
  alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

  # decrypt the text
  plaintext = ''
  for ch in ciphertext.lower():
    if ch in alphabets:
      plaintext += alphabets[(alphabets.index(ch) - key) % 26]
    else:
      plaintext += ch

  return plaintext

# test the functions
text = input("Enter the text: ")
print(text)

key = int(input("What is key? "))
print(key)

ciphertext = encrypt(text, key)
print('Encrypted text:', ciphertext)

plaintext = decrypt(ciphertext, key)
print('Decrypted text:', plaintext)