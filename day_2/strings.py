#!/usr/bin/python3

s = 'My name is Shiva'
print(s)

s = '''this is a multiline
       comment, so I am writing
                   one more line'''
print(s)

# different methods of strings

s = 'shiva saxena IS LeArNinG pYtHon'
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.isalpha())
print(s.isalnum())
s = 'hello123'
print(s.isalnum())

s = 'lower'
print(s.islower())
s = s.upper()
print(s.isupper())
s = 'Title'
print(s.istitle())

s = 'shiva saxena is learning python'
l = s.split(' ')
print(l)
j = '_'.join(l)
print(j)

s = "   shive is learning python\n    "
print(s.strip())

s = "wwwwssssHere I am learningggggg"
print(s.lstrip('wsg'))

print(s.rstrip('wsg'))


# finding text using 

s = 'shiva is learning with fun'
print(s.find('is'))
print(s.find('are'))
print(s.startswith("sh"))
print(s.endswith('th'))


# checking palindrome

s = input("Enter the input string: ")
z = s[::-1]
if s == z:
    print("Yes it is a palindrome!")
else:
    print("No it is not a palindrome!") 

# counting number of words in a given line

s = input("Enter a line ")
s = s.strip()
z = s.split(' ')
count = len(z)
print("Number of words are: %d" % (count))
