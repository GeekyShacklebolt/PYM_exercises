#!/usr/bin/python3

fobj = open("fl1.txt")
print(fobj)
fobj.close()

fobj = open("fl2.txt")
print(fobj.read())
fobj.close()

fobj = open("fl2.txt")
print(fobj.readline())
fobj.close()

fobj = open("fl2.txt")
print(fobj.readlines())
fobj.close()

fobj = open("fl2.txt")
for x in fobj:
    print(x, end='')
fobj.close()

name = input("\nEnter the name of the file: ")
fobj = open(name)
print(fobj.read())

# with satatement

with open("fl2.txt") as fobj:
    for x in fobj:
        print(x, end='')

with open("fl3.txt", "w") as fobj:
    name = []
    st = input("Enter a string: ")
    st = st.split(' ')
    for i in range(0,len(st)):
        fobj.write(st[i]+'\n')
    fobj.close()

with open("fl3.txt") as fobj:
    print(fobj.read())

def tocopy(a,b):
    with open(a) as fobj:
        buf = fobj.read()
    
    with open(b, "w") as fobj:
        fobj.write(buf)

    with open(b) as fobj:
        print(fobj.read())

tocopy("fl3.txt","fl1.txt")
with open("fl1.txt", "w") as fobj:
    pass
# just to flush the content of fl1.txt

import sys

if sys.argv[1] != 'copy':
    print("Wrong command!")
else:
    tocopy(sys.argv[2],sys.argv[3])
