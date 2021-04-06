import nltk
import re
import numpy as np
import random
import string
import urllib.request
import bs4 as bs

#For HTML/XML files
#dataset = urllib.request.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
#dataset = dataset.read()
#parsedataset = bs.BeautifulSoup(dataset, 'html.parser')
#parse_para = parsedataset.find_all('p')
#parse_text = ''
#for para in parse_para:
#    parse_text += para.text
#
#    corpus = nltk.sent_tokenize(parse_text)

#for txt file
#data = C:\Users\Nemichand\Desktop\Source_code.txt
data = open(r'C:\Users\Nemichand\Desktop\Source_code.txt', 'r')
print(data)
dataset = ''

for line in data:
    dataset += line.strip()

#print(dataset)

corpus = nltk.sent_tokenize(dataset)
#print(corpus)

for i in range(len(corpus)):
    corpus[i] = corpus[i].lower()
    corpus[i] = re.sub(r'\W', ' ', corpus[i])
    corpus[i] = re.sub(r'\s+', ' ', corpus[i])
    #print(corpus[i])

print(len(corpus))

wordfreq = {}
for sentence in corpus:
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
        if token not in wordfreq.keys():
            wordfreq[token] = 1
        else:
            wordfreq[token] += 1
#print(wordfreq)

import heapq
most_freq = heapq.nlargest(300, wordfreq, key=wordfreq.get)

sentence_vectors = []
for sentence in corpus:
    sentence_tokens = nltk.word_tokenize(sentence)
    #print(sentence_tokens)
    sent_vec = []
    for token in most_freq:
        if token in sentence_tokens:
            sent_vec.append(1)
        else:
            sent_vec.append(0)
            #print(sent_vec)
    sentence_vectors.append(sent_vec)
#print(sentence_vectors)
sentence_vectors = np.asarray(sentence_vectors)
print(sentence_vectors)
