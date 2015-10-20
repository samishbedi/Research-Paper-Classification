from nltkwordextraction import *
import os,sys
import time


traindir = "Dataset/NBC/Train/"
testdir = "Dataset/NBC/Test/"

files = os.listdir(traindir)

classList = []	#frequency dictionary corresponding to every class
classCount = []  #no of words in every class
classes = []
V = 0

#print files
for f in files:
	classList.append(make_token(traindir+f))
	#print len(classList[-1]),f
	V = V + len(classList[-1])
	classes.append(f)

#print V
for d in classList:
	count = 0
	for val in d.values():
		count+=val
	classCount.append(count)

#print classCount
#print classList
def prob(w,i):
	if w in classList[i]: 
		return classList[i][w]
	else:
		return 0
	"""if(classList[i][w]>0):
		return 1
	else:
		return 0"""

totalc=0.0
correct=0.0
tfolders = os.listdir(testdir)
for folder in tfolders:
	tfiles = os.listdir(testdir+folder)
	for f in tfiles:
		#print f
		ftoken = make_token(testdir+folder+"/"+f).keys()
		#print ftoken
		probList = []
		totalc+=1
		for i in range(0,5):
			probList.append(1.0)
		prob1 = 0.0
		index = 0
		for w in ftoken:
			for i in range(0,5):
				#print classCount[i]*1.0
				#print prob(w,i)
				probList[i] = probList[i]*((prob(w,i)+1)/((classCount[i])*1.0))
				#print prob(w,i)
		for i in range(0,5):
			if probList[i]>prob1:
				prob1 = probList[i]
				index = i
			#print probList
		#print index, probList
		print folder,classes[index][:-4],f
		if folder==classes[index][:-4]:
			correct+=1
		
	print " "

def Accuracy_NBC():
	return correct/totalc*100.0





