# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:53:56 2019

@author: jline
"""
'''
Three different types of methods
    1) Instance methods
    2) Class methods
    3) Static methods
'''

class Student:
    
    school = 'Clemson' # static variable    
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3 # Instance variable
    
    def avg(self): # caluclate average marks. This is an instance method
        return (self.m1 + self.m3 + self.m3)/3        
    
    def get_m1(self): # getter
        return self.m1
    
    def set_m1(self, value): # setter
        self.m1 = value
        
    @classmethod # class method decorator    
    def getSchool(cls): # Class method
        return cls.school
    
    @staticmethod # static method decorator    
    def info():
        print("This is Student Class... in abc module")
        
        
        
s1 = Student(34,47,32)
s2 = Student(89,32,12)



print(s1.avg()) # Prints the average mark
print(Student.getSchool())

Student.info() # Prints the output of the static method