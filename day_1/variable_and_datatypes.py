#!/usr/bin/python3

a = 21
b = 34
c = a + b
print(c)

print('India')
print("India")
print('India\'s')
print("\n")


# reading input from the keyboard

num = int(input("Enter a number: "))
print(num)
if num < 10:
    print("this is less than 10")
else:
    print("this is bigger than 10")
print("\n")


# INTEREST PROBLEM

amt = float(input("Enter the amount: "))
interest = float(input("Enter the rate of interest: "))
period = float(input("Enter the period: "))
year = 1
tot = 0

while year <= period:
    amt = amt + (interest*amt)
    print("After %d year, your amount will be %f" % (year,amt))
    year = year + 1
print("\n")


# AVERAGE OF N NUMBERS

N = int(input("Enter how many numbers would you like to enter: "))
ctr = 1
SUM = 0
average = 0

while ctr <= N:
    num = int(input("Enter the no. {} : " .format(ctr)))
    SUM = SUM + num
    ctr = ctr + 1

average = float(SUM)/N
print("N is %d, SUM of \'N\' numbers is %d, Average is %f" % (N,SUM,average))
print("\n")


# TEMPERATURE CONVERSION

celcius = 0
while celcius <= 350:
    farhenheit = 1.8 * celcius + 32
    print("Celcius = %d and Farhenheit = %f" % (celcius,farhenheit))
    celcius = celcius + 25
print("\n")


# MULTIPLE ASSIGNMENT

a, b = 50, 10
print(a, '+', b)
# swapping
a, b = b, a
print("%d + %d" % (a,b))
print("\n")


# TUPLE PACKING AND UNPACKING

tuple = ("shiva","Btech","Python")
name, course, language = tuple
print(name, course, language)
print("\n")


# FORMATTING STRINGS
msg = "{0} is studying in {1} and learning {2}".format(name,course,language)
print(msg)
msg2 = f"{name} is studying in {course} an learning {language}"
print(msg2)

