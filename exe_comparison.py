import subprocess
import re

#subprocess.Popen("g++ original.cpp -o original.out", shell=True, executable='/bin/bash')
#subprocess.Popen("g++ test.cpp -o test.out", shell=True, executable='/bin/bash')
def lenLCS(X, Y):
	n = len(X); m=len(Y)
	this_row = [0 for i in range(m+1)]
	last_row = [0 for i in range(m+1)]
	for i in range(1,n+1):
		for j in range(1,m+1):
			if X[i] == Y[j]:
				this_row[j] = last_row[j-1]+1
			else:
				this_row[j] = max( this_row[j-1], last_row[j])



x = subprocess.Popen('cmp -l original.out test.out', shell=True, executable='/bin/bash', stdout = subprocess.PIPE)
result, error = x.communicate()
temp = re.findall(r'\\n', str(result))
differ = len(temp)
with open('test.out', 'rb') as f:
	total_t = len(f.read())
with open('original.out', 'rb') as f:
	total_o = len(f.read())
perc = (1-differ/total_t)*100
print(differ, total_t, total_o, perc, sep=' ')