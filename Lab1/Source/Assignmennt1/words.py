#importing regular expressions
import re
#Taking input from the user
mysent=input('Enter a sentence')
#splitting the sentence
wrdLst = re.sub("[^\w]", " ",  mysent).split()
#Individual words
print(wrdLst)
s=len(wrdLst)
def fndMid(lst):
    l=len(lst)
    middle = float(len(lst))/2
    #If there are even numbers in the list
    if l % 2 == 0:
        return (lst[int(middle-1)], lst[int(middle)])
    #if there are odd number of words
    else:
        return lst[int(middle - .5)]
#Middle words from the function
y=list(fndMid(wrdLst))
print(y)
#Sorted list for the largest word
srtlist=sorted(wrdLst,key=len)
#largest word from sorted array
print(srtlist[-1])
revwrd=' '.join(w[::-1] for w in mysent.split())
print(revwrd)