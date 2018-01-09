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


class test(object):
    def __init__(self):
        self.__mostprivate = "mostprivate"
        self._semiprivate = "semiprivate"
        self.public = "public"
    def method(self):
        return "this is an instance method"


class test2(test):
    def __init__(self):
        test.__init__(self)
        self.public2 = "public"
        self._semiprivate2 = "semiprivate2"
        self.__mostprivate2 = "mostprivate2"
        
