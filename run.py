import os,sys
import math


print ""
print ""
print "***************Running Naive Bayesian Classifier*************"
print ""
print "Orignal            Predicted             File_Name"
print "-----------------------------------------------------"
import bayesianClassifier

print ""
print ""
print "**************Running K-Nearest Neighbour Classifier**********"
print ""
                         
print "Orignal            Predicted             File_Name"
print "-----------------------------------------------------"
import KNN

print ""
print ""
print "**************************Accuracy*****************************"
print " "
print "Naive Bayesian Classifier:", bayesianClassifier.Accuracy_NBC(),"%"
print "K-Nearest Neighbour Classifier:", KNN.Accuracy_KNN(),"%"
print " "
