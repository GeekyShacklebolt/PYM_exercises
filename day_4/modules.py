#!/usr/bin/python3

# modules
# first module I created 'bars' that is a submodule of 'newmodule'
import newmodule.bars
import newmodule.utils

newmodule.bars.normal(20)

import os
print(os.getuid())   # this prints the current processes's effective user's ID
print(os.getpid())   # this prints the current process's ID
print(os.getppid())  # this prints the parent process's ID

# uname(), it returns a tuple

print(os.uname())

print(os.getcwd())
os.chdir('newmodule')
print(os.getcwd())

newmodule.utils.list()

import requests
obj = requests.get('http://google.com')
print(obj.status_code)


