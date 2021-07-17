import re


from Functions.BagOfWords import BOWComparison
from Functions.indent import indentComparison
from Functions.Function_Signature import functionSignatureComp
from Functions.Variable_And_Operator_Count import varAndOperCount
from Functions.exe_comparison import exe_comp
from Functions.ksc import ksc
from Functions.AST_comp import ASTmatch

def multiLayerComparison(file_name1,file_name2, key=0):
    '''
    Pass file locations starting from the same directory as this functions's file.
    Return True for plagiarised, False for non-plagiarised. If some test not done, whether due to an error or that layer not being reached, None instead of percentage for that test.
    If key != 0, a list returned - [result, percentage_returned_from_test_1, ... (all test functions)]
    If threshold crossed at any test, then file passed forwards, else declared non-plagiarised.
    If all tests fail to be executed (give some error), None returned.
    Test order: BOWComparison, Indentation Comparison, Variable & Operator Count Comparison, Function Signature, Exe Comparison, Keyword Sequence Comparison, AST Comparison.'''

    perc_list, pass_list = [None for i in range(6)], [None for i in range(6)]
    func_layer0 = [BOWComparison]
    func_layer1 = [indentComparison, varAndOperCount, functionSignatureComp]
    func_layer2 = [exe_comp,ksc]
    func_layer3 = [ASTmatch]
    size = [len(func_layer0),len(func_layer1), len(func_layer2), len(func_layer3)]
    
    thresholds = [65,65,65,75,85,85,45]
    
    perc_list, pass_list = [None for i in range(sum(size))], [None for i in range(sum(size))]
    def key_result(plag): # Used to return value as per key. 'plag' should be True/False
        if key==0:
            return plag
        else:
            l = [plag]
            l.extend(perc_list)
            return l
    
    ## LAYER 0
    #  String Comparison
    with open(file_name1, 'r') as f1, open(file_name2, 'r') as f2:
        # Removing comments:
        text1 = re.sub(r"(//.*?$)|(/\*.*?\*\\)","",f1.read(), flags = re.DOTALL|re.MULTILINE)
        text2 = re.sub(r"(//.*?$)|(/\*.*?\*\\)","",f2.read(), flags = re.DOTALL|re.MULTILINE)
        if text1 == text2:
            return key_result(True)
    
    #  Bag Of Words Comparison
    try:
        with open(file_name1, 'r') as f1, open(file_name2, 'r') as f2:
            perc_list[0] = func_layer0[0](f1, f2)
        if perc_list[0] > thresholds[0]:
            pass_list[0] = True
    except:
        print("Error in BOW_comp")
    
    if any(pass_list[:size[0]]):
        pass
    elif pass_list[:size[0]] == [None for i in range(size[0])]:
        pass
    else:
        return key_result(False)
    
    
    ## LAYER 1
    for i in range(size[1]):
        j = i + size[0]
        try:
            with open(file_name1, 'r') as f1, open(file_name2, 'r') as f2:
                perc_list[j] = func_layer1[i](f1, f2)
            if perc_list[j]>thresholds[j]:
                pass_list[j] = True
            else:
                pass_list[j] = False
        except:
            print(f"Error in function #{i} in Layer 1")
        
    if any(pass_list[ size[0] : sum(size[:1]) ] ):
        pass
    else:
        return key_result(False)
    
    
    ## LAYER 2
    #  EXE COMPARISON
    # ENTER FILENAME INSTEAD OF OPEN() OBJECT.
    i = sum(size[:1])
    try:
        perc_list[i] = func_layer2[0](file_name1, file_name2)
        if perc_list[i] > thresholds[i]:
            pass_list[i] = True
    except:
        print("Error in exe_comp")

    #  KEYWORD SEQUENCE COMPARISON
    try:
        with open(file_name1, 'r') as f1, open(file_name2, 'r') as f2:
            perc_list[i+1] = func_layer2[1](f1, f2)
        if perc_list[i+1] > thresholds[i+1]:
            pass_list[i+1] = True
    except:
        print("Error in ksc")
    
    if any(pass_list[ i : sum(size[:2]) ] ):
        return key_result(True)
    else:
        return key_result(False)
    
    ## LAYER 3
    #  AST COMPARISON
    i = i+size[2]
    try:
        with open(file_name1, 'r') as f1, open(file_name2, 'r') as f2:
            perc_list[i] = func_layer3[0](f1, f2)
        if perc_list[i]>thresholds[i]:
            pass_list[i] = True
        else:
            pass_list[i] = False
    except:
        print("Error in AST comparison")
    
    if any(pass_list[ i : sum(size) ] ):
        return key_result(True)
    else:
        return key_result(False)

if __name__ == '__main__':
    print(multiLayerComparison('dataset3/Arithmetic/student1.cpp','dataset3/Arithmetic/student5.cpp',1))
