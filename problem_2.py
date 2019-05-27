#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

def find_files(suffix, path):
    def goToDir(path, pathsWithSuffix):
        if os.path.isfile(path) :
            if path.endswith(suffix):
                pathsWithSuffix.append(path)
        else:
            availableFiles = os.listdir(path)
            for file in availableFiles:
                goToDir(os.path.join(path, file), pathsWithSuffix)
    
    pathsWithSuffix = list()
    goToDir(path, pathsWithSuffix)
    return pathsWithSuffix

def test_sample_dir():
    files = find_files(".c",".")
    print(files)

test_sample_dir()

