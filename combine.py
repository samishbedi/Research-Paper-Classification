import os

files = os.listdir(os.getcwd())
f = open('combined.txt','w')
for file1 in files:
  if(file1[-3:]=='txt'):
    #print f
    f1 = open(file1)
    #print f1
    for line in f1:
      f.write(line)
      #print line
    f1.close()
f.close()
