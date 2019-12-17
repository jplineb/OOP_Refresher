# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:06:54 2019

@author: jline
"""

class Student:
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
    
    ## Create a class inside a class
    
    class Laptop:
        
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
            
        def show(self):
            print (self.brand, self.cpu, self.ram)




s1 = Student("JP",2)
s2 = Student("Jenny",3)


'''
print(s1.name, s1.rollno) ---> this is not a cool way of doing it

use class.show()
'''

## Creating instance of laptop in each class
lap1 = s1.lap
lap2 = s2.lap

print(id(lap1), id(lap2)) # differnt spots in memory
##

## Using constructors to make an instance of lap without it being defined in the init
lap1 = Student.Laptop()
lap2 = Student.Laptop()
##

## Using a method inside a class inside a class to show
s1.show()
