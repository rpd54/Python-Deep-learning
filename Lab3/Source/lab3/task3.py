from nltk.corpus import wordnet as wn
from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
import re, collections
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from collections import Counter
from nltk import FreqDist
import nltk
from nltk import ngrams
from operator import itemgetter


#-	Take an Inputfile. Use the simple approach below to summarize a text file
with open('input.txt' , 'r') as f:
    lines = f.readlines()
print("lines",lines)
fr=''
#Multi- line file into single string
for m in lines:
    fr=fr+m
print(fr)
#tokenize word
fr_word = word_tokenize(fr)
fr_sent = sent_tokenize(fr)

#-	Using Lemmatization, apply lemmatization on the remaining words
lemmatizer = WordNetLemmatizer()
fr_lemma = []
for word in fr_word:
    fr_lema = lemmatizer.lemmatize(word.lower())
    fr_lemma.append(fr_lema)

print("\n -----------lemmetaizion----------  ")
print(fr_lemma)
fr_pos = pos_tag(fr_lemma)

print("--------------BIGRAM-------------")

n = 2
gram=[]
bigrams = ngrams(fr_lemma, n)
for grams in bigrams:
    gram.append(grams)
print(gram)
str1 = " ".join(str(x) for x,y in fr_pos)
str1_word = word_tokenize(str1)
print("--------Bi-Grams with word  frequency----------")
fdist1 = nltk.FreqDist(gram)
top_fiv = fdist1.most_common()
top_five = fdist1.most_common(5)

top=sorted(top_fiv,key=itemgetter(0))
print(top)
print('---------Top 5 bi-grams word freq with count--------')
print(top_five)
sent1 = sent_tokenize(fr)
rep_sent1 = []

for sent in sent1:
    for word,words in gram:
        for ((c,m), l) in top_five:
            if (word,words == c,m):
                rep_sent1.append(sent)  # Creating sentences containing the most common words
print ("\n Sentences with top five Bigrams")
s=max(rep_sent1,key=len)
print(s)