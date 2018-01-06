#!/usr/bin/python3

def list(path='.'):
    import os
    '''
    this function returns all the directories available in the given path
    if path not given then current path is taked as default
    '''
    ls = os.listdir(path)
    ls.sort()
    for i in ls:
        print(i,'')


