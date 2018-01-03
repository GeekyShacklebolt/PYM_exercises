#!/usr/bin/python

# first class

class First(object):
   shiva = 10
   saxena = 10

obj = First()

# more functional classes with __init__

class Second(object):
    '''
    returns the name, surname and age of student
    '''
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Object created successfully")

    def print_details(self):
        print("Name: %s" % self.name)
        print("Surname: %s" % self.surname)
        print("age: %s" % self.age)

obj = Second('shiva','saxena',20)
obj.print_details()

# inheritance

class Mammal(object):
    '''
    returns a ```Mammal``` object with the given name
    '''
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name


class Whale(Mammal):
    '''
    returns a ```Whale``` object, takes 2 arguments environment, lifetime
    '''
    def __init__(self, name, environment, lifetime):
        Mammal.__init__(self, name)
        self.environment = environment
        self.lifetime = lifetime

    def get_details(self):
        return "Name: %s, Lives in: %s, Avg. lifetime: %s" % (self.name, self.environment, self.lifetime)


class Rabbit(Mammal):
    '''
    returns a ```Rabbit``` object, takes 2 argument food, behaviour
    '''
    def __init__(self, name, food, behaviour):
        Mammal.__init__(self, name)
        self.food = food
        self.behaviour = behaviour

    def get_details(self):
        return "Name: %s, Food: %s, Behaviour: %s" % (self.name, self.food, self.behaviour)


obj1 = Mammal('Man')
obj2 = Whale('Whale', 'Water', '90 yrs')
obj3 = Rabbit('Rabbit', 'carrot', 'Sweat and harmless')

print(obj1.get_details())
print(obj2.get_details())
print(obj3.get_details())   

# multiple inheritance

class One(object):
    a = 10

class Two(object):
    b = 20

class Three(One, Two):
    c = 30
    def disp(self):
        return "%d : %d : %d" % (self.a,self.b,self.c)

obj = Three()
print(obj.disp())

print(dir(obj))

del obj

# implementing properties and setter in class

class Student(object):
    '''
    returns a ```Student``` object, takes argunments marks and make sure that they are not -ve
    '''
    def __init__(self,name):
        self.name = name
        self.__score = 0

    @property
    def marks(self):
        " returns marks in numbers "
        return self.__score

    @property
    def result(self):
        " returns the result of student rather than numbers "
        if self.__score > 50:
            return 'pass'
        else:
            return 'fail'

    @marks.setter
    def marks(self, value):
        " set the students marks and take care if -ve marks are provided"
        if value < 0:
            print("Oops! you wrongly entered -ve score!")
            return
        else:
            self.__score = value

obj = Student('shiva')
obj.marks = 80
print("Marks are : %d" % obj.marks)
obj.marks = -20
print("Status is : %s" % obj.result)

