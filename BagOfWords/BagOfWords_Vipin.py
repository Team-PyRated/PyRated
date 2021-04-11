#!/usr/bin/env python
# coding: utf-8

# In[2]:


file = open(r"fsm-key.asm.txt",'r')
update_line=[]
for line in file:
    #remove whitespaces from start and end and convert to lower characters
    update_line.append(line.lower().strip())


# In[3]:


update_line


# In[4]:


remove_char = [';','#','/*','*/','@','~']
update_line_document=[]
[update_line_document.append(''.join((filter(lambda i: i not in remove_char, line))).strip()) for line in update_line] ;


# In[5]:


update_line_document


# In[6]:


document_lines = []
[document_lines.append(line.split(' ')) for line in update_line_document];


# In[7]:


document_lines


# In[8]:


document_words = []
for i in document_lines:
    for j in i:
        document_words.append(j)


# In[9]:


document_words


# In[10]:


from collections import Counter
BOL = [Counter(lines) for lines in document_lines]
BOW = Counter(document_words)


# In[12]:


BOL


# In[13]:


BOW


# In[ ]:




