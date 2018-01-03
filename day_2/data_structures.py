#!/usr/bin/python3

# DATA STRUCTURES

# LISTS

data = ['zero','one','two','three','four','five']
print(data)

data.append('six')  # append()
print(data)

data.insert(2,1.5)  # insert()
print(data)

data.insert(-2,4.5)
print(data)

data.remove(1.5)    # remove()
print(data)

del data[-2]        # del
print(data)

data.reverse()      # reverse()
print(data)

print(data.count('two'))


# USING LISTS AS STACKS

data.pop()
print(data)

data.pop()
print(data)

data.append(5)
print(data)

data.append(5)
print(data)
print('\n')


# USING LISTS AS QUEUE

print(data)
data.pop(0)
print(data)

data.append(10)
print(data)

data.pop(0)
print(data)

data.append(20)
print(data)

# LIST COMPREHENSION
# prime numbers using list comprehension
x = list(range(1,100))
p = [x for x in x if all(x%z!=0 for z in range(2,x))]
print(p)
print('\n')


# TUPLES

tup = ('a','b','c','d','e','f')
print(tup)
print(tup[2])
a, b, c = tup[0:3]
print(a,'',b,'',c)


# SETS

st = set('lskfdjlaskjdflaksdlfaksjf')
print(st)

st2 = set('asjghgkdhfasjdalaksfdkh')
print(st2)

sub = st2-st
print(sub)
uni = st2 | st
print(uni)
an = st2 & st
print(an)
xor = st2 ^ st
print(xor)


st.add('z')
print(st)
st.pop()
print(st)


# DICTIONARIES

dic = {'name': 'shiva', 'course': 'btech', 'college': 'niec'}
print(dic)
print(dic['name'])
print(dic['college'])

print('shiva' in dic)
print('name' in dic)

dic2 = dict((('one','two'),('three','four')))
print(dic2)

for x,y in dic.items():
    print("%s is %s" % (x,y))
print(dic2)

dic2.setdefault('names',[]).append('mayank')
dic2.setdefault('names',[]).append('shubham')
print(dic2)

print(dic2.get('name','default'))

# using inumeration

for i, j in enumerate(['a', 'b', 'c', 'd']):
    print("%s -> %s" % (i,j))

# STUDENT'S PROBLEM

data = {}
languages = ('python','c','java')
n = int(input("Enter the number of students: "))
for i in range(0,n):
    marks=[]
    name = input("Enter the name of the students: ")
    for x in languages:
        marks.append(int(input("Enter the marks of %s in subject %s: " % (name,x))))
    data[name] = marks

for x,y in data.items():
    if(sum(y) < 120):
        print("%s is Failed with total marks %d." % (x,sum(y)))
    else:
        print("%s is Passed with total marks %d." % (x,sum(y)))


# MATRIX MULTIPLICATION

a = []
b = []
c = []
n = int(input("Enter the value of n: "))
print("Enter first matrix")
for i in range(0,n):
    a.append([int(x) for x in input("").split(" ")])
print("Enter second matrix")
for i in range(0,n):
    b.append([int(x) for x in input("").split(" ")])
print("Resultant matrix")
for i in range(0,n):
    c.append([a[i][j]*b[j][i] for j in range(0,n)])
print('-'*10*n)
for i in c:
   for k in i:
     print("%5d" % k, end=' ')
   print('\n')
print('-'*10*n)
