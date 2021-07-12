import subprocess, re
from Multi_Layer_Comparison import multiLayerComparison, indentComparison, varAndOperCount, functionSignature, exe_comp, keywordSeqCom



functions = ["multiLayerComparison","indentComparison","varAndOperCount","functionSignature","keywordSeqCom","exe_comp"]
n_funcs = len(functions)
start = 0
end = start+5

def func_num(x, f1, f2):
    if x==0: return multiLayerComparison(f1,f2)
    elif x==1: return indentComparison(f1,f2)
    elif x==2: return varAndOperCount(f1,f2)
    elif x==3: return functionSignature(f1,f2)
    elif x==4: return keywordSeqCom(f1,f2)
    elif x==5: return exe_comp(f1,f2)

with open('truth.txt', 'r') as f:
	plag_files_str = f.read()
#print("%r"%plag_files_str)
plag_files = plag_files_str.split('- ')

i=0
while i < len(plag_files):
    if re.match('B', plag_files[i]) == None:
        plag_files.pop(i)
        i-=1
    else:
        plag_files[i] = plag_files[i].split('\n')
        plag_files[i].pop()
        t = [plag_files[i][0], re.sub('/','_',plag_files[i][0])]
        for x in plag_files[i][1:]:
            t.append(x.split(','))
        plag_files[i] = t
    i+=1

#print(*plag_files, sep='\n')

c_pos,c_neg, f_pos, f_neg, error = [0 for i in range(n_funcs)], [0 for i in range(n_funcs)], [0 for i in range(n_funcs)], [0 for i in range(n_funcs)], [0 for i in range(n_funcs)]
thresholds = [None, 80, 90, 75, 78, 85]

for assignment in plag_files:
    
    folder = assignment[1]
    #print(folder)
    
    process_list_files = subprocess.run(f"ls dataset/{folder}", shell=True, executable='/bin/bash', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    print(process_list_files.stderr)

    test_files_str = process_list_files.stdout.decode('ascii')
    #print(test_files_str)
    test_files = test_files_str.split('\n')
    test_files.pop()
    n_files = len(test_files)
    
    for i in range(n_files//1):
        for j in range(i+1,n_files//1):
            #print(i,j)
            x = test_files[i]
            y = test_files[j]
            #print(x,y)
            # Be VERY careful about format of file to be sent, extensions, address, and all.
            plagiarised = [None for i in range(n_funcs)]
            for k in assignment[2:]:
            #print(x,y,k,sep = '\n')
                if (x[:-4] in k) and (y[:-4] in k):
                    actually_plagiarised = True
                    break
                else:
                    actually_plagiarised = False
            
            for v in range(start, end):
                try:
                    value = func_num(v, 'dataset/'+folder+'/'+x,'dataset/'+folder+'/'+y)
                    
                    if v>0:
                        if value>thresholds[v]:
                            plagiarised[v] = True
                        else: plagiarised[v] = False
                    else:
                        plagiarised[v] = value
                    #print(plagiarised[v])
                    
                    if actually_plagiarised:
                        if plagiarised[v] == actually_plagiarised:
                            c_pos[v] += 1
                        else:
                            f_neg[v] += 1
                    else:
                        if plagiarised[v] == actually_plagiarised:
                            c_neg[v] += 1
                        else:
                            f_pos[v] += 1
                    
                except ZeroDivisionError:
                    print(functions[v],folder, x, y, '/0')
                    error[v] += 1
                except:
                    print(functions[v],folder, x, y, 'ERROR\n\n\n')
                    error[v]+=1
print('\n')
perc, perc_plag, perc_nplag = [0 for i in range(n_funcs)], [0 for i in range(n_funcs)], [0 for i in range(n_funcs)]

for i in range(start, end):
    perc[i] = 100*(c_pos[i] + c_neg[i])/(c_pos[i] + c_neg[i]+f_pos[i]+f_neg[i])
    perc_plag[i] = 100*c_pos[i]/(c_pos[i]+f_neg[i])
    perc_nplag[i] = 100*c_neg[i]/(c_neg[i]+f_pos[i])
    print(f"{functions[i]}: {perc_plag[i]}% of plag pairs and {perc_nplag[i]}% of non-plag pairs correctly identified. Tested {c_pos[i] + c_neg[i]+f_pos[i]+f_neg[i]} pairs. {error[i]} pairs gave an error.")


