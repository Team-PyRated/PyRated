
import re
# Remove comments.
# Analyse and remove unused functions, classes.

def remove_comments(file): # x is file
	p = r"(#.*\n)|((['\"])\3{2}(?:.|\n)*?\3{3})"
	return re.sub( p, '', file)

def remove_unused_functions(file):
	x = file
	if not re.match(r"\n", x): x = "\n" + x # For lookbehind to work.
	# The regex which matches for a function (or method) defined
	p = r"(?<=\n)(?P<indent>\t*)def (?P<f_name>\w+)(?:.|\n)*?:(?:.|\n)*?(?=\n(?P=indent)?[^\t\n]|$)"
	functions = re.finditer( p, x, flags=re.ASCII) # Returns match objects, the start and end of which we will use.
	tbr = [] # to be removed

	for func in functions:
		
		p1 = func.group('f_name')
		if p1[:2]=="__": # __init__ and other magic methods are defined but never explicitly used, 
						 # but we shouldn't delete them.
			continue 
		start = func.start()
		end = func.end()
		# Checking if the function was used anywhere aside from inside itself:
		used_before = bool(re.search( p1, x[:start]))
		used_after = bool(re.search( p1, x[end:]))
		# If not, add it to the list of useless functions.
		if not( used_before or used_after ):
			tbr.append((start,end)) # The start and end of the useless bit is saved.
	n = len(tbr)
	try:
		# The following adds in the parts of x other than what should be removed.
		# Eg, x = x[:start] + x[end:] for one match to be removed.
		# The following is the same, but for multiple matches.
		sum = ""
		sum += x[:tbr[0][0]] 
		sum += "".join([ x[ tbr[i-1][1]:tbr[i][0] ] for i in range(1,n)]) 
		sum += x[tbr[n-1][1]:]
		return sum

	except IndexError:
		return x

def remove_unused_classes(file):
	# Practically the same as the remove_unused_functions code
	x = file
	if not re.match(r"\n", x): x = "\n" + x # For lookbehind to work.
	p = r"(?<=\n)class (?P<c_name>\w+)(?:.|\n)*?:(?:.|\n)*?(?=\n[^\t\n]|$)"
	classes = re.finditer( p, x, flags=re.ASCII)
	tbr = [] # to be removed
	for clss in classes:
		
		p1 = clss.group('c_name')
		start = clss.start()
		end = clss.end()
		used_before = bool(re.search( p1, x[:start]))
		used_after = bool(re.search( p1, x[end:]))
		if not( used_before or used_after ):
			tbr.append((start,end))
	n = len(tbr)
	try:
		sum = ""
		sum += x[:tbr[0][0]] 
		sum += "".join([ x[ tbr[i-1][1]:tbr[i][0] ] for i in range(1,n)]) 
		sum += x[tbr[n-1][1]:]
		return sum
	except IndexError:
		return x


'''
name = input("Name of the file:")
with open(name, 'r') as f:
	code = f.read()
'''
with open('test.py', 'r') as f:
	code = f.read()

code = remove_comments(code)
# Run the following function twice, to clean up any functions
# used only by unused functions and the like.
code = remove_unused_functions(code)
code = remove_unused_classes(code)
code = remove_unused_functions(code)

#print(code)
res_file = open("result.py", 'w')
res_file.write(code)
res_file.close()
