#!/usr/bin/python3

# BASIC OPERATORS

print(5+2)
print(5/2)
print(5%2)
print('\n')


# INTEGER ARITHMATIC

days = int(input("Enter the no. of days: "))
months, days = divmod(days,30)
print("It is %d months and %d days" % (months,days))
print("\n")

# using divmod function
days = int(input("Enter the no. of days again: "))
print("It is %d months and %d days" % divmod(days,30))
print("\n")

# using relational operators
print(1<2)
print(1>2)
print(1==2)
print(1!=2)
print("\n")
print(5//2)
print(5/2)
print("\n")

# using logical operators. And | Or
print(4 and 5)  # ans 5
print(4 and 0)  # ans 0
print(0 or 1)   # ans 1
print(4 or 5)   # ans 4
print("\n")


# SHORTHAND OPERATOR

num = 90
num += 10
print(num)
print('\n')


# PROBLEM OF EXPONENT BY 2

num = int(input("Enter the number: "))
val = int(input("Enter how many numbers would you want: "))
ctr = 1 
newnum = 1
while ctr <= val:
    newnum *= num
    print("{0} ".format(newnum))
    ctr += 1
print('\n')


# TYPE CONVERSION
num = 2.3146
print(num)
print(str(num))
print("\n")


# EVALUATEEQUAL
# series is ans = 1/x + 1/(x+1) + 1/(x+2) + ... + 1/n
n = 10
x = 1
SUM = 0
ctr = 1
while ctr <= n:
    SUM = SUM + (1/x)
    print(SUM)
    x += 1
    ctr += 1
print("Final result %f" % (SUM))


# QUADRATIC EQUATION
import math
a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant: "))
D = b**2 - 4*a*c
if D<0:
   print("Roots are not real!")
else:
   root1 = (-b+math.sqrt(D))/(2*a)
   root2 = (-b-math.sqrt(D))/(2*a)
   print("Roots are %f and %f" % (root1,root1))
print("\n")


# SALESMAN SALARY PROBLEM

basic = 10000
commission_rate = 0.02
bonus_per_camera = 100
sold_cameras = int(input("Enter the number of cameras sold: "))
price_camera = int(input("Enter the price of each camera: "))
bonus = sold_cameras*bonus_per_camera
commission = commission_rate*price_camera*sold_cameras
print("Bonus is %d " % (bonus))
print("Commission is %d " % (commission))
print("Salary is %d " % (basic + bonus + commission))
print('\n')
