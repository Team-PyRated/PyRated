import re

# To count the operators
def countOperators(s, dict):
    operators = ['+', '-', '*', '/', '%', '++', '--', '==', '!=', '>=', '<=', '>', '<', '&&', '||', '!', '&', '|', '^', '~', '<<', '>>']
    
    for op in operators:
        if len(op) == 1:
            _op = '\\' + op
            pat = '[^' + _op + ']' + _op
            if op in ['!', '<', '>']:
                pat += '[^' + _op + '\=]'
            else:
                pat += '[^' + _op + ']'
            dict[op] = len(re.findall(pat, s))
        else:
            dict[op] = len(re.findall('\\'+'\\'.join(op), s))

# To count the variable types
def countVariables(s, dict):
    pass

# Function to make dictionary with var and operator counts
def makeDict(f):
    dict = {}
    s = f.read()
    to_replace = {}

    for line in f:
        line = line.strip()
        if not line.startswith('#define'):
            continue
        st = line.split()
        to_replace[st[1]] = ' '.join(st[2:])
    
    s = re.sub('#.*\n', '', s)
    s = re.sub('\/\/(.*?)\n', '', s)
    s = re.sub('\"(.*?)\"', '', s)
    s = re.sub('\s+', ' ', s)
    s = re.sub('\/\*(.*?)\*\/', '', s)

    for k,v in to_replace.items():
        s = re.sub('(?:[^a-zA-Z0-9_])' + k + '(?:[^a-zA-Z0-9_])', v, s)

    countOperators(s, dict)
    s = re.sub('\((.*?)\)', '()', s)
    print(s)
    print('=============================')
    countVariables(s, dict)
    return dict

def varAndOperCount(f1, f2):
    dict1 = makeDict(f1)
    dict2 = makeDict(f2)
    print(dict1)
    # Write logic to find percent similarity
    return 60

if __name__ == "__main__":
    fname1=r'./original.cpp'                              #Path for original file
    fname2=r'./copy.cpp'                                  #Path for file that is being checked for plagiarism (copy)

    # Read the files
    f1 = open(fname1, 'r')
    f2 = open(fname2, 'r')

    print("Percentage VariableAndOperator match = ", varAndOperCount(f1, f2))

    # Close the files
    f1.close()
    f2.close()