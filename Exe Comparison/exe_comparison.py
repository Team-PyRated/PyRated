import subprocess
import re

def exe_comp(file_o, file_t):
    '''
    Compares the compiled exes of the two source codes to check for plagiarism.
    file_o, file_t are names of the files to be compared, without extensions, as strings. o is original, t is the one to be tested.
    Returns true for plagiarised (>80% match), else false.
    file_o must not be considerably larger than file_t, because the excess length of one file is also counted in difference.
    '''
    subprocess.call("rm original.out test.out", shell=True, executable='/bin/bash', stderr = subprocess.PIPE)
    subprocess.call("g++ "+file_o+".cpp -o original.out", shell=True, executable='/bin/bash')
    subprocess.call("g++ "+file_t+".cpp -o test.out", shell=True, executable='/bin/bash')

    comp_process = subprocess.Popen('cmp -l original.out test.out', shell=True, executable='/bin/bash', stdout = subprocess.PIPE)
    result, error = comp_process.communicate()
    differ = re.findall(r'\\n', str(result))
    num_diff = len(differ)
    with open('test.out', 'rb') as f:
        total_t = len(f.read())
    with open('original.out', 'rb') as f:
        total_o = len(f.read())
    perc = (1-num_diff/total_t)*100
    if perc>80:
        return True
    else:
        return False
