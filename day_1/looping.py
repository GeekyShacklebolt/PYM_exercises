#!/usr/bin/python3

# while loop
n = 10
while n>0:
    print(n, end=':')
    n -= 1
print("\n")


# FIBONACCI SERIES
a, b = 0, 1
n = 10
while n>0:
   print(a, end=' ')
   a, b = b, a+b
   n -= 1
print('\n')

# find e**x =1+x+x**2/2! +x**3/3! +....+ x**n/n! where 0 < x < 1
x = float(input("Enter the value of x: "))
n = 1
SUM = 1 
term = 1
while n <= 100:
    term *= x/n 
    SUM += term
    n += 1
    if term < 0.0001:
        break
print("no. of terms: %d, Sum is: %f" % (n,SUM))
print("\n")


# MULTIPLICATION TABLE
print('_'*50)
r = 1
while(r <= 10):
   c = 1
   while(c <= 10):
      print("%4d" % (r*c), end=' ')
      c += 1
   print("\n")
   r += 1

print('_'*50)
print("\n")

# PATTERNS
n = 5
while n>0:
    print("*"*n)
    n -= 1
print("\n")

while n<=5:
    print("*"*n)
    n += 1
print("\n")

n = 5
while n>0:
   print(" "*(5-n), end='')
   print("*"*n)
   n -= 1
print("\n")


# LIST

list2 = ["one","two","three","four","five","six"]
print(list2[0])
print(list2[-1])
print(list2[3])
print(list2[0:4])
print(list2[0::2])
print(list2[0:])
print('\n')


print('one' in list2)
print('seven' in list2)
print(len(list2))

if list2:
   print("yes")
print('\n')


# FOR LOOP

for x in list2:
    print(x)

for x in list2[::2]:
    print(x)
print('\n')


# RANGE FUNCTION

list2 = list(range(3,10))
print(list2)
list2 = list(range(3,10,2))
print(list2)
list2 = list(range(10))
print(list2)


# CONTINUE STATEMENT
m = 1
while m < 10:
    m += 1
    n = int(input("Enter a num: "))
    if n < 0:
        print("Please enter again!")
        continue
    elif n == 0:
        print('bye with break')
        break
    else:
        print('square of %d is %d' % (n,n*n))

else:
    print('loop is over successfully')


# GAME OF STICKS
sticks = 21
turn = int(input("Enter zero to catch the chance first: "))
if turn:
    turn = 'computer'
else:
    turn = 'user'

user = 0
comp = 0
while sticks >= 1:
    if turn == 'user':
        user = 0
        while user > 4 or user < 1 or user > sticks:
            user = int(input("Enter how many stick you want: "))
            if user > 4 or user < 1 or user > sticks:
                print("wrong entry, enter again!")
        sticks -= user
        print("You picked %d sticks now left %d" % (user, sticks))
        turn = 'computer'
    else:
       comp = 4 - user + 1
       sticks -= comp 
       print("Computer is picking up %d sticks now left %d" % (comp, sticks))
       turn = 'user'
if turn == 'computer':
    print("Computer won")
else:   
    print("You won!")
