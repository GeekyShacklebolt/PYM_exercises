#!/usr/bin/python3
from typing import Dict

class Student(object):
    '''
    
    Returns a "Student" object. Takes Student's Name, batch, branch,
    roll. Returns total score and the result of student.
    
    '''
    def __init__(self, name, batch, branch, roll) -> None:
        self.name = name
        self.batch = batch
        self.branch = branch
        self.roll = roll  
        # todo: remove ": Dict[str, int]" if using python version < 3.6
        self.papers: Dict[str, int] = {}     
        self.total = 0
    
    def is_passed(self) -> str:
        '''Function to return the result of Student'''
        for i, j in self.papers.items():
            if j < 40:
                return "failed"

        return "passed"

    def total_score(self) -> int:
        '''Function to return the total marks of a Student'''
        for i, j in self.papers.items():
            self.total += j
        
        return self.total


obj1 = Student('Jack', '2016', 'IT', '128')
obj1.papers = {'English': 86, 'Math': 90, 'Science': 85}
obj2 = Student('Mack', '2015', 'CS', '423')
obj2.papers = {'English': 87, 'Math': 80, 'Science': 81}
obj3 = Student('Hack', '2014', 'CS', '124')
obj3.papers = {'English': 83, 'Math': 92, 'Science': 89}

for obj in [obj1, obj2, obj3]:
    print("{0} is {1} with {2} score".format(obj.name, obj.is_passed(), obj.total_score()))


# errorneous in mypy
# remove these 2 lines to remove errors while analysing this program with "mypy"
# you may install "mypy" with "pip install mypy"
obj1.papers = ['hello', 'error', 'in', 'mypy']
obj2.papers = {0: 'opposite', 1: 'as', 2: 'defined'}
