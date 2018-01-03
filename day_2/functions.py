#!/usr/bin/python3

def add(a,b):
    return a + b

print(add(2,4))
print('\n')

def palin(s):
   z = s[::-1]
   if s == z:
       print("String is a palindrom")
   else:
       print("String is a not a palindrom")

st = input("Enter an input: ")
palin(st)
print('\n')

# local and global variables

def swap(a,b):
   a, b = b, a
   print('in swap', a, '', b)

a = 1
b = 3
print('before swap', a, '', b)
swap(a,b)
print('after swap', a, '', b)
print('\n')

def swap():
   global a, b
   a, b = b, a
   print('in swap', a, '', b)

a = 1
b = 3
print('before swap', a, '', b)
swap()
print('after swap', a, '', b)
print('\n')

# default argument

def defarg(a, b=0):
    return a + b

print(defarg(2))
print(defarg(2,5))
print('\n')

# second example

def example(a, dic=[]):
    dic.append(a)
    return dic

print(example(5))
print(example(6))
print('\n')

def example(a,dic = None):
    if dic == None:
         dic = []
    dic.append(a)
    return dic

print(example(5))
print(example(6))
print('\n')

# keyword argument

def foo(a = 9, b = 10, c = 11):
    print(a, '', b, '', c)
    
foo()
foo(5,8,c = 6)
foo(3,c=1,b=4)
print('\n')

# keyword only argument

def foo(a = 9, b = 10, *, last = 10):
    print(a, '', b, '', last)

foo()
foo(3,b=8)
foo(3,5,last=9)
print('\n')

# Docstrings

import math

def hypo(a, b):
    ''' 
    this is a function in 
    which we give 2 sides of 
    a triangle and this 
    returns hypotenus.
    '''
    return math.sqrt(a**2 + b**2)

if __name__ == '__main__':
    print(hypo(3,4)) 
print('\n')

# higher order function

def call1(a,b):
   return a+b

def call2(a,b,c):
   return a(b,c)

print(call2(call1,3,5))
print('\n')


it = [1,2,3,4,5]
def twice(a):
    return 2*a

print(list(map(twice,it)))

print('\n')
