#!/usr/bin/python3

import sys

def fact(num):
    '''
    Function to find the factorial of a given number.

    args: a number
    returns: factorial of a number

    '''
    
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


def div(num):
    '''
    Function to divide 10 with the given number.

    args: a number
    returns: division of 10 by a number.

    '''
    res = 10/num 
    return res


def main(num):
    res = fact(num)
    print(res)
    res = div(num)
    print(res)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if int(sys.argv[1]) < 0:
            print("Sorry, can't find the factorial of negative numbers")
        else:
            main(int(sys.argv[1]))
    else:
        print("SyntaxError: Invalid Syntax\n")
        print("Use \"./factorial.py <number>\"\n")
 
