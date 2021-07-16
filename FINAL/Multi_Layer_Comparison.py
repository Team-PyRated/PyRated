import re

from Functions.indent import indentComparison
from Functions.Function_Signature import functionSignatureComp
from Functions.Variable_And_Operator_Count import varAndOperCount
from Functions.exe_comparison import exe_comp
from Functions.ksc import ksc
from Functions.AST_comp import ASTmatch

def multiLayerComparison(file_name1,file_name2):
    '''
    Pass file locations starting from the same directory as this functions's file.
    Return True for plagiarised, False for non-plagiarised. If some test not done, None instead of percentage for that test.
    If threshold crossed at any test, then file passed forwards, else declared non-plagiarised.
    If all tests fail to be executed (give some error), None returned.
    Test order: Indentation Comparison, Variable & Operator Count Comparison, Function Signature, Exe Comparison, Keyword Sequence Comparison, AST Comparison.'''

    perc_list, pass_list = [None for i in range(6)], [None for i in range(6)]
    
    func_layer1 = [indentComparison, varAndOperCount, functionSignatureComp]
    func_layer2 = [exe_comp,ksc, ASTmatch]
    size = [len(func_layer1), len(func_layer2)]
    
    thresholds = [80,80,75,90,90,90]
    
    
    ## LAYER 0
    with open(file_name1, 'r') as f1, open(file_name2, 'r') as f2:
        # Removing comments:
        text1 = re.sub(r"(//.*?$)|(/\*.*?\*\\)","",f1.read(), flags = re.DOTALL|re.MULTILINE)
        text2 = re.sub(r"(//.*?$)|(/\*.*?\*\\)","",f2.read(), flags = re.DOTALL|re.MULTILINE)
        if text1 == text2:
            return True
    
    ## LAYER 1
    for i in range(size[0]):
        try:
            with open(file_name1, 'r') as f1, open(file_name2, 'r') as f2:
                perc_list[i] = func_layer1[i](f1, f2)
            if perc_list[i]>thresholds[i]:
                pass_list[i] = True
            else:
                pass_list[i] = False
        except:
            print(f"Error in function #{i} in Layer 1")
        
    print(perc_list[:size[0]])
    if any(perc_list[:size[0]]):
        pass
    elif perc_list[:size[0]] == [None for i in range(size[0])]:
        pass
    else:
        return False
    
    ## LAYER 2
    #  EXE COMPARISON
    # ENTER FILENAME INSTEAD OF OPEN() OBJECT.
    try:
        perc_list[size[0]] = func_layer2[0](file_name1, file_name2)
        if perc_list[size[0]] > thresholds[size[0]]:
            pass_list[size[0]] = True
    except:
        print("Error in exe_comp")

    # KEYWORD SEQUENCE COMPARISON
    try:
        with open(file_name1, 'r') as f1, open(file_name2, 'r') as f2:
            perc_list[size[0]+1] = func_layer2[1](f1, f2)
        if perc_list[size[0]+1] > thresholds[size[0]+1]:
            pass_list[size[0]+1] = True
    except:
        print("Error in ksc")
    
    # AST COMPARISON
    i = size[0]+2
    try:
        with open(file_name1, 'r') as f1, open(file_name2, 'r') as f2:
            perc_list[i] = func_layer2[2](f1, f2)
        if perc_list[i]>thresholds[i]:
            pass_list[i] = True
        else:
            pass_list[i] = False
    except:
        print("Error in AST comparison")
    
    print(perc_list[ size[0] : size[0]+size[1] ] )
    if any(perc_list[ size[0] : size[0]+size[1] ] ):
        return True
    else:
        return False

if __name__ == '__main__':
    print(multiLayerComparison('dataset3/Arithmetic/student1.cpp','dataset3/Arithmetic/student5.cpp'))
