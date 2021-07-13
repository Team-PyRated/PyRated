import sys
sys.path.append('../')

from typing import Sequence
import numpy as np
from array import *
import subprocess
import re
import nltk
import string
from collections import Counter

from Indentation.indent import indentComparison
from Function_Signature.Function_Signature import functionSignatureComp
from Variable_and_Operator_Count.Variable_and_Operator_count import varAndOperCount

def multiLayerComparison(file_name1,file_name2, key=0):
    func_layer1 = [indentComparison, functionSignatureComp, varAndOperCount]
    th_layer1 = [30, 30, 30]

    # Reading the files
    f1 = open(file_name1, 'r')
    f2 = open(file_name2, 'r')

    percents_layer1 = [fun(f1, f2) for fun in func_layer1]
    print(percents_layer1)

    # Close the files
    f1.close()
    f2.close()

    return 60

if __name__ == "__main__":
    fname1=r'./dataset/B2016_Z1_Z1/student5420.cpp'                              #Path for original file
    fname2=r'./dataset/B2016_Z1_Z1/student5533.cpp'                              #Path for file that is being checked for plagiarism (copy)

    print("Percentage plag confidence = ", multiLayerComparison(fname1, fname2))

    
