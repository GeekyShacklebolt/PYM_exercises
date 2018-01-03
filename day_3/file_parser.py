#!/usr/bin/python

import os
import sys

def parse_file(path):
    '''
    parse the text file in the given path
    
    :arg path: path of the txt file to parse
    :return: A tuple with count of spaces, tabs and lines
    '''
    with open(path) as obj:
        spaces = 0
        tabs = 0
        for i,j in enumerate(obj):
            spaces += j.count(' ')
            tabs += j.count('\t')
        print(j)

    return spaces, tabs, i+1

def main(path):
    '''
    this prints the counts of spces, tabs and lines
    :arg path: path of the txt file to parse
    :return: False if file not found otherwise True
    '''
    
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("spaces: %s, tabs: %s, lines %s" % (spaces,tabs,lines))
        return True
    else:
        print("file doesn't exits!")
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)
