# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:36:31 2019

@author: jline
"""

class Computer:
    
    def __init__(self):
        self.name = 'JP'
        self.age = 22
    
    def update(self):
        self.age = 30
        
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
        
    
    
c1 = Computer() # this is the constructor
c2 = Computer()

'''
print(id(c1)) # look at location in heap memory
print(id(c2))
'''

print(c1.name) # prints the name in init


## changes the variable in the class
c1.name = 'Bob'
c1.age = 4
print(c1.name, c1.age) 
##

## Call update to modify variable age in class c1
c1.update()
print(c1.age)
##

## Compare strings
c2.update()
if c1.compare(c2):
    print("They are same")