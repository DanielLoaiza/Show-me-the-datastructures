#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os

def find_files(suffix, path):
    def goToDir(path, pathsWithSuffix):
        if not suffix:
            return None
        if os.path.isfile(path) :
            if path.endswith(suffix):
                pathsWithSuffix.append(path)
        elif os.path.isdir(path):
            availableFiles = os.listdir(path)
            for file in availableFiles:
                goToDir(os.path.join(path, file), pathsWithSuffix)
        else:
            return None
    
    pathsWithSuffix = list()
    goToDir(path, pathsWithSuffix)
    return pathsWithSuffix

#normal case
def test_sample_dir():
    files = find_files(".c",".")
    print(files)

#empty suffix
def test_sample_dir_2():
    files = find_files("",".")
    print(files)

#not a dir
def test_sample_dir_3():
    files = find_files(".c",".h")
    print(files)

test_sample_dir()
test_sample_dir_2()
test_sample_dir_3()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




