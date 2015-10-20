import os,sys

fcom=open('allkeys.txt')
lcom=[]
for line in fcom:
	lcom.append(line[:-1])

lcom = sorted([l for l in set(lcom)])
f=open("newstopwords.txt",'w')


for l in lcom:
	ans=raw_input(l)
	if ans=='2':
		f.write(l)
		f.write("\n")
		#print stop


		


