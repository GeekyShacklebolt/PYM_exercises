#!/usr/bin/python3


# ITERATORS


class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        '''Returns itself as an iterator object'''
        return self

    def __next__(self):
        '''Returns the next value till current is nower than high'''
        if self.current < self.high:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

obj = Counter(1,7)
for i in obj:
    print(" %d" % i)
print("\n")


# GENERATORS


def generator(low, high):
    '''a generator function which uses "yield" to make it an iterator'''
    while low < high:
        yield low
        low += 1

for i in generator(0,10):
    print(" %d" % i)


print(dir(generator(2,5)))
print('\n')

# Infinite Generators

def infinite(num):
    while True:
        yield num
        num += 1
        if num > 15:  # to break the infinite loop
            break

c = infinite(2)

for i in c:
    print(i,end=' ')
print('\n')

for i in c:           # to confirm that generators aren't reusable
    print(i,end=' ')
print('\n')

# Creating Resuable Generotors

class ReuseGen(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        '''Function to make this class' object a reusable generator'''
        temp = self.current
        while temp < self.high:
            yield temp
            temp += 1

c = ReuseGen(4, 12)

for i in c:
    print(i,end=' ')
print('\n')

for i in c:           
    print(i,end=' ')
print('\n')


# GENERATOR EXPRESSSION

print(sum([x**3 for x in range(0,10)])) # takes more memory
print(sum(x**3 for x in range(0,10)))  # takes less memory
a = sum(x**3 for x in range(0,10))
print(a) 
print('\n')


# CLOSURE


def surname(surname):
    def name(name):
        return name + ' ' + surname
    return name
'''
Here "name" is a closure, which adds "name" to a predefined 
"surname"
'''
 
man = surname('saxena')
print(man('shiva'))
print(man('shubham'))

man = surname('singhal')
print(man('mayank'))
print(man('rakshit'))
print('\n')

def shiva(func):
    def inside(*args, **kwargs):
        return "My name is Shiva, %d" % func(*args, **kwargs)
    return inside


@shiva
def sub(a, b):
    return a-b 

print(sub(7, 2))
