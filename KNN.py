from nltkwordextraction import *
import os,sys
import math

traindir = "Dataset/KNN_DATASET/TRAINING/"
testdir = "Dataset/KNN_DATASET/TESTING/"
k=5
folders = os.listdir(traindir)

data = []
for folder in folders:
	files = os.listdir(traindir+folder)
	for f in files:
#		ftoken = make_token(traindir+folder+"/"+f)
		flist = []
		flist.append(make_token_knn(traindir+folder+"/"+f))
		flist.append(folder)
		data.append(flist)
#print "OK"
#print data

def norm(d):
	n=0.0
	for val in d.values():
		n = n+val*val
	return math.sqrt(n)

def similarity(ftoken):
	similar = []
	for d in data:
		val = 0.0
		for key in ftoken.keys():
			val = val+ftoken[key]*d[0][key]
		if(not ftoken or not d[0]):
			continue
		val = val/norm(ftoken)
		val = val/norm(d[0])
		l = []
		l.append(val)
		l.append(d[-1])
		similar.append(l)
	return similar

totalc=0.0
correct=0.0
def classify(vector):
	knnclass = ""
	maxsum = 0.0
	for folder in folders:		
		s = 0.0
		for v in vector:
			if(v[1]==folder):
				s = s+v[0]
			if(s>maxsum):
				maxsum = s
				knnclass = v[1]
	return knnclass

folders = os.listdir(testdir)
for folder in folders:
	files = os.listdir(testdir+folder)
	for f in files:
		totalc+=1
		ftoken = make_token_knn(testdir+folder+"/"+f)
		knn = similarity(ftoken)
		knn = sorted(knn,key=lambda l:l[0], reverse=True)
		print folder,classify(knn[0:k]),f
		if folder==classify(knn[0:k]):
			correct+=1
	print " "

def Accuracy_KNN():
	return correct/totalc*100.0
























