import sys
sys.path.append('../')


from Indentation.indent import indentComparison
from Function_Signature.Function_Signature import functionSignatureComp
from Variable_and_Operator_Count.Variable_and_Operator_count import varAndOperCount
from Keyword_sequence_comparison.ksc import ksc

from AST.ASTcombine import ASTmatch

def multiLayerComparison(file_name1,file_name2):
    func_layer1 = [indentComparison, functionSignatureComp, varAndOperCount]
    th_layer1 = [30, 30, 30]

    func_layer2 = [ksc]
    func_layer3 = [ASTmatch]

    percents_layer1 = [fun(open(file_name1, 'r'), open(file_name2, 'r')) for fun in func_layer1]
    percents_layer2 = [fun(open(file_name1, 'r'), open(file_name2, 'r')) for fun in func_layer2]
    percents_layer3 = [fun(open(file_name1, 'r'), open(file_name2, 'r')) for fun in func_layer3]

    print(percents_layer1)
    print(percents_layer2)
    print(percents_layer3)

    return 60

if __name__ == "__main__":
    fname1=r'./dataset/B2016_Z1_Z1/student5420.cpp'                              #Path for original file
    fname2=r'./dataset/B2016_Z1_Z1/student5533.cpp'                              #Path for file that is being checked for plagiarism (copy)

    print("Percentage plag confidence = ", multiLayerComparison(fname1, fname2))
