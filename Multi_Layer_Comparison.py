from typing import Sequence
import numpy as np
from array import *
import subprocess
import re
import nltk
import string
from collections import Counter

def lcs(a, b):
    '''Returns the SUBSEQUENCE, not the length'''
    tbl = [[0 for B in range(len(b) + 1)] for A in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            tbl[i + 1][j + 1] = tbl[i][j] + 1 if x == y else max(
                tbl[i + 1][j], tbl[i][j + 1])
    res = []
    i, j = len(a), len(b)
    while i and j:
        if tbl[i][j] == tbl[i - 1][j]:
            i -= 1
        elif tbl[i][j] == tbl[i][j - 1]:
            j -= 1
        else:
            res.append(a[i - 1])
            i -= 1
            j -= 1
    return res[::-1]

def indentComparison(fname1, fname2):
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
    #print(space1)
    #print(space2)
    try:
        indentmatch= len(lcs(space1,space2))*2/(len(space1)+len(space2))                       #Calculate Percentage indent match
    except ZeroDivisionError:
        indentmatch = 1
    return 100*indentmatch

# For next function,
# All Operators are considered. Just remove whatever you don't want
count={'int':0,'float':0, 'char':0, 'short':0, 'long':0, 'double':0, '=':0, '+':0, '-':0, '*':0, '%':0, '/':0, '++':0, '--':0, '==':0, '!=':0, '>':0, '<':0, '<=':0, '>=':0, '&&':0, '!':0, '||':0, '&':0, '|':0, '^':0, '~':0, '<<':0, '>>':0, '+=':0, '-=':0, '*=':0, '/=':0, '^=':0, '%=':0, '&=':0}

def varAndOperCount(fname1, fname2):
    code1=open(fname1,'r')
    code2=open(fname2,'r')
    codefile1=[]
    codefile2=[]
    
    # Reading the code file and filtering out unnecessary symbols.
    for line in code1:
        codefile1.append(line.strip(';').strip('\n').strip().strip('{').strip('}').strip('#').strip('').strip('(').strip(')').strip(',').strip("''"))
    for line in code2:
        codefile2.append(line.strip(';').strip('\n').strip().strip('{').strip('}').strip('#').strip('').strip('(').strip(')').strip(',').strip("''"))
    #print(codefile1)
    coderef1=[]
    coderef2=[]
    # Performing split on each of the string for easy comparison
    for word in codefile1:
        coderef1.append(word.split())
    for word in codefile2:
        coderef2.append(word.split())

    # Comparing each items in code file and storing the occurance count in above dictionary.
    count1=count
    count2=count
    countfname1=0
    countfname2=0
    for elements in coderef1:
        for items in elements:
            for key in count1.keys():
                if items == key or items.startswith(key):
                    count1[key] += 1
                    countfname1 += 1
    for elements in coderef2:
        for items in elements:
            for key in count2.keys():
                if items == key or items.startswith(key):
                    count2[key] += 1
                    countfname2 += 1

    similarity=0
    for elem in (count1 and count2):
        similarity +=1
    code1.close();code2.close()
    try:
        return (similarity*100*2)/(countfname1+countfname2)
    except ZeroDivisionError:
        return 100
    

def lines_words(file):
    updated_lines = []
    change_words={}
    for line in file:
        if(not line.startswith("//") and line!="\n"  and not line.startswith('#') and not line.startswith('using')):
            updated_lines.append(line.lower().strip())
        if(line.startswith("#define")):
            words = line.split(' ')
            #print(words)
            replace = words[1]
            string = ""
            for i in range(2,len(words)):
                string += words[i]
                string += " "
            string = string[:-2]
            #print(string)
            change_words[replace] = string
    code=""
    for i in range(len(updated_lines)):
        code += updated_lines[i]
        
    code = code.translate({ord("}"):"}; ",ord("("):" ( ",ord("{"):" { ;"})
    for key,value in change_words.items():
        code=code.replace(key,value)
        
    lines_code=code.split(';')
    return lines_code

def hashmap_function(lines_code,hashmap):

    pattern ="\((.*?)\)"
    for i in range(len(lines_code)):
        if ('{'in lines_code[i] and '(' in lines_code[i] and ')' in lines_code[i] and not('for ' in lines_code[i]) and not('while ' in lines_code[i]) and not('main' in lines_code[i]) and not('if ' in lines_code[i])):

            #substring = re.search(pattern, lines_code[i]).group(1)
            try:
                substring = re.search(pattern, lines_code[i]).group(1)
            except AttributeError:
                substring = ""
            #print(substring)
            count_parameter=[]
            type_parameter=[]
            parameters = (substring.split(','))
            #print(parameters)
            parameter_type = [i.strip().rsplit(' ', 1)[0] for i in parameters]
            #print(parameter_type)
            count_parameter_all = dict(Counter(parameter_type))
            for key,value in count_parameter_all.items():
                if key != "":
                    count_parameter.append(value)
                    type_parameter.append(key)

            #print(lines_code[i])
            words = lines_code[i].strip().split()
            if(words[0]=='static' or words[0]=='inline'):
                words[0]=''
            return_type=""
            #print(words)
            for j in range(len(words)):
                if(words[j]=='('):
                    for k in range(j-1):
                        return_type +=words[k]
                        return_type +=" "
                    break
            #print(count_parameter)
            function_signature=(return_type.strip(),tuple(count_parameter),tuple(type_parameter))
            #print(function_signature)
            hash_value=hash(function_signature)
            if hash_value not in hashmap:
                hashmap[hash_value]=1
            else:
                hashmap[hash_value]+=1

def common_percentage(hashmap1,hashmap2):
    common=[min(hashmap1[i],hashmap2[i]) for i in hashmap1 if i in hashmap2]
    try:
        val = (2*sum(common)/(sum(hashmap1.values())+sum(hashmap2.values())))*100
        if(not error_flag):
            return val
        elif (val!=0):
            return val
        else:
            return 100
    except:
        return 100

def functionSignature(fname1, fname2):
    hashmap1={}
    code1 = open(fname1,'r')
    lines_code=lines_words(code1)
    hashmap_function(lines_code,hashmap1)
   
    hashmap2={}
    code2 = open(fname2,'r')
    lines_code=lines_words(code2)
    hashmap_function(lines_code,hashmap2)
    
    #print(hashmap1, hashmap2)
    percentage_same=common_percentage(hashmap1,hashmap2)
    code1.close()
    code2.close()
    return percentage_same

def exe_comp(fname1, fname2):
    file_o = fname1
    file_t = fname2
    '''
    Compares the compiled exes of the two source codes to check for plagiarism.
    file_o, file_t are names of the files to be compared, with extensions, as strings. o is original, t is the one to be tested.
    Returns true for plagiarised (>80% match), else false.
    file_o must not be considerably larger than file_t, because the excess length of one file is also counted in difference.
    '''
    subprocess.call("rm original.out test.out", shell=True, executable='/bin/bash', stderr = subprocess.PIPE)
    subprocess.call("g++ "+file_o+" -o original.out", shell=True, executable='/bin/bash')
    subprocess.call("g++ "+file_t+" -o test.out", shell=True, executable='/bin/bash')

    comp_process = subprocess.Popen('cmp -l original.out test.out', shell=True, executable='/bin/bash', stdout = subprocess.PIPE)
    result, error = comp_process.communicate()
    differ = re.findall(r'\\n', str(result))
    num_diff = len(differ)
    with open('test.out', 'rb') as f:
        total_t = len(f.read())
    with open('original.out', 'rb') as f:
        total_o = len(f.read())
    perc = (1-num_diff/total_t)*100
    return perc
        # if perc>80:
        #     return True
        # else:
        #     return False

C_Keywords = ['auto', 'double', 'int', 'struct', 'break', 'else', 'long', 'switch', 'case', 'enum', 'register', 'typedef', 'char', 'extern', 'return', 'union', 'continue', 'for', 'signed', 'void', 'do', 'if', 'static', 'while', 'default', 'goto', 'sizeof', 'volatile', 'const', 'float', 'short', 'unsigned' ]

def keywordSeqCom(fname1, fname2):
    '''Takes in the file text, the code.'''
    code1 = open(fname1, 'r')
    code2 = open(fname2, 'r')

    keyword_sequence1 = []
    keyword_sequence2 = []
    words1 = []
    words2 = []
    lines1 = ''
    lines2 = ''

    for line in code1:
        lines1 += line.strip()
    for line in code2:
        lines2 += line.strip()

    Lines1 = nltk.sent_tokenize(lines1)
    Lines2 = nltk.sent_tokenize(lines2)

    for line in Lines1:
        words1 += nltk.word_tokenize(line)

    for line in Lines2:
        words2 += nltk.word_tokenize(line)

    for word in words1:
        if word in C_Keywords:
            keyword_sequence1.append(word)

    for word in words2:
        if word in C_Keywords:
            keyword_sequence2.append(word)

    LCS_kw = ''
    LCS_kw = lcs(keyword_sequence1,keyword_sequence2)

    a = len(LCS_kw)
    b = max(len(keyword_sequence1),len(keyword_sequence2))

    try:
        matching = (a/b)*100
    except:
        matching = 100
    code1.close();code2.close()
    return matching




def multiLayerComparison(file_name1,file_name2, key=0):
    
    #print(code_text1.read())
    '''
    Return True for plagiarised, False for non-plagiarised, at key=0 (default). key=1 returns percentage matches at each test. If some test not done, None instead of percentage for that test.
    If threshold crossed at any test, then file passed forwards, else declared non-plagiarised.
    Test order: Indentation Comparison, Variable & Operator Count Comparison, Function Signature, Exe Comparison, Keyword Sequence Comparison.'''
    perc_list, pass_list = [None for i in range(5)], [None for i in range(5)]
    # List of percentage matches at each test,
    # And whether the threshold was crossed at each test.
    
    def key_result(plag): # Used to return value as per key. 'plag' should be True/False
        if key==0:
            return plag
        else:
            return [plag].extend(perc_list)
    
    ## LAYER 0
    code1 = open(file_name1, 'r')
    code2 = open(file_name2, 'r')
    if code1.read() == code2.read():
        return key_result(True)
    code1.close();code2.close()
    ## LAYER 1
    # INDENTATION COMPARISON
    '''
    This code compares two text files for similarity based on the degree of indent match.
    file_name1, file_name2 are the two files being compared. Change path accordingly
    '''
    # file_name1=r'./original.txt'                              #Path for original file
    # file_name2=r'./copy.txt'                                  #Path for file that is being checked for plagiarism (copy)
    perc_list[0] = indentComparison(file_name1,file_name2)
    if perc_list[0] > 80:
        pass_list[0] = True

    # VARIABLE AND OPERATOR COUNT COMPARISON
    ''' This function is intended to perform variable and opeartor count on both the codefiles in an order to determine their variable and operator
    percentage match '''
    perc_list[1] = varAndOperCount(file_name1,file_name2)
    if perc_list[1] > 90:
        pass_list[1] = True
    
    # FUNCTION SIGNATURE
    perc_list[2] = functionSignature(file_name1, file_name2)
    if perc_list[2] > 75:
        pass_list[2] = True
    
    if any(perc_list[:3]):
        pass
    else:
        return key_result(False)
    
    ## LAYER 2
    #  EXE COMPARISON
    '''perc_list[3] = exe_comp(file_name1, file_name2)
    if perc_list[3] > 85:
        pass_list[3] = True'''

    # KEYWORD SEQUENCE COMPARISON
    perc_list[4] = keywordSeqCom(file_name1, file_name1)
    if perc_list[4] > 78:
        pass_list[4] = True
    
    if any(perc_list[3:5]):
        pass
    else:
        return key_result(False)
    
    return key_result(True)
