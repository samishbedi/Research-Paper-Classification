import nltk
import numpy
import re
from nltk import word_tokenize
import string
import re
import operator
import sys
from nltk.corpus import stopwords

stop=open('newstopwords.txt') 
newstop=[]
for line in stop:
	newstop.append(line[:-1])
filename1 = sys.argv[-1]

def openfile(filename):
	#subprocess.call(['./pdf2txt.sh'])
	
	f = open(filename, 'rU')
	raw= f.read()
	raw = unicode(raw, errors='ignore')
	return raw

def make_token(filename):
	raw=openfile(filename)
	tokens = word_tokenize(raw)
	tokens=[t.lower() for t in tokens if t not in string.punctuation and t.isalpha()]
	lemmatizer = nltk.WordNetLemmatizer()
	tokens = [lemmatizer.lemmatize(token) for token in tokens]
	stopwords1 = stopwords.words('english')
	tokens = [token for token in tokens if token not in stopwords1]
	tokens = [token for token in tokens if token not in newstop]
	fdist = nltk.FreqDist(tokens)
	tokens = ([w for w in tokens if len(w)> 4 and fdist[w]>25])
	fdist = nltk.FreqDist(tokens)
	return fdist

def make_token_knn(filename):
	raw=openfile(filename)
	tokens = word_tokenize(raw)
	tokens=[t.lower() for t in tokens if t not in string.punctuation and t.isalpha()]
	lemmatizer = nltk.WordNetLemmatizer()
	tokens = [lemmatizer.lemmatize(token) for token in tokens]
	stopwords1 = stopwords.words('english')
	tokens = [token for token in tokens if token not in stopwords1]
	tokens = [token for token in tokens if token not in newstop]
	fdist = nltk.FreqDist(tokens)
	tokens = ([w for w in tokens if len(w)> 4 and fdist[w]>5])
	fdist = nltk.FreqDist(tokens)
	return fdist

#print newstop
def freq(tokens):
	#tokens=make_token()
	fdist = nltk.FreqDist(tokens)
	return fdist	
	

def no_of_voc_words(tokens):
	#tokens=make_token()
	tokenset = sorted([w for w in set(tokens)])
	return len(tokenset)

#print len(tokens)


#f=open(filename1[:-4]+"keywords.txt",'w')
#for i in tokens:
	#f.write(i)
	#f.write("\n")
#print tokens
#f.close()
"""sum=0;
for k in sorted(fdist,key = fdist.get,reverse=True):
    	print k," ",fdist[k]
	sum+= fdist[k]
prob=0
for k in sorted(fdist,key = fdist.get,reverse=True):
    	prob+= fdist[k]/(sum * 1.0)
	

print prob


"""
