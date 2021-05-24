import nltk
import string
from LCS import lcs

C_Keywords = ['auto', 'double', 'int', 'struct', 'break', 'else', 'long', 'switch', 'case', 'enum', 'register', 'typedef', 'char', 'extern', 'return', 'union', 'continue', 'for', 'signed', 'void', 'do', 'if', 'static', 'while', 'default', 'goto', 'sizeof', 'volatile', 'const', 'float', 'short', 'unsigned' ]
#print(C_Keywords)

code1 = open(r'C:\Users\Nemichand\Desktop\Source_code1.txt', 'r')
code2 = open(r'C:\Users\Nemichand\Desktop\Source_code2.txt', 'r')

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

#print(lines1)
#print(lines2)
#print(words1)
#print(words2)

for word in words1:
    if word in C_Keywords:
        keyword_sequence1.append(word)

for word in words2:
    if word in C_Keywords:
        keyword_sequence2.append(word)

#print(keyword_sequence1)
#print(keyword_sequence2)
LCS_kw = ''
LCS_kw = lcs(keyword_sequence1,keyword_sequence2)
#print(LCS_kw)

a = len(LCS_kw)
b = max(len(keyword_sequence1),len(keyword_sequence2))

matching = (a/b)*100
print(matching)
