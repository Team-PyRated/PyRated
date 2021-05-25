'''
This code compares two text files for similarity based on the degree of indent match.
fname1, fname2 are the two files being compared. Change path accordingly

'''
import numpy as np
from array import *

def lcs(seq1 , seq2):
    
    n1 = len(seq1)                                                               #Length of sequences (n2>=n1)   
    n2= len(seq2)

    L = [[0 for seq1 in range(n2+1)] for iter in range(n1+1)]                    #Create 2D array to store values

    for iter1 in range(n1+1):
        for iter2 in range(n2+1):
            if iter1 == 0 or iter2 == 0 :
                L[iter1][iter2] = 0
            elif seq1[iter1-1] == seq2[iter2-1]:                                #If elements match
                L[iter1][iter2] = 1+L[iter1-1][iter2-1]
            else:
                L[iter1][iter2] = max(L[iter1-1][iter2] , L[iter1][iter2-1])    #If elements do not match
    return L[n1][n2]                                                            #Return length of LCS

fname1=r'./original.txt'                              #Path for original file
fname2=r'./copy.txt'                                  #Path for file that is being checked for plagiarism (copy)

#Read files
f1=open(fname1,'r')
f2=open(fname2,'r')

#Array containing size of indent for each line 
space1=[]
space2=[]

#Generate indent size sequence for original file
for line1 in f1:
    ct=0
    index=0
    
    for char1 in line1:
        if char1==' ':
            ct+=1
        else:
            break
    space1.append(ct)
    index+=1

#Generate indent size sequence for copy file
for line2 in f2:
    ct=0
    index=0
    
    for char2 in line2:
        if char2==' ':
            ct+=1
        else:
            break
    space2.append(ct)
    index+=1

#Print sequence of indents for both files
print(space1)
print(space2)

indentmatch=lcs(space1,space2)/len(space1)                                          #Calculate Percentage indent match
print("Percentage indent match = ",100*indentmatch)

    
