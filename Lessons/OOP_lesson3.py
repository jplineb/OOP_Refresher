# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:48:08 2019

@author: jline
"""

class Car:
    
    ## defining a class variable
    wheels = 4
    
    def __init__(self):
        self.mil = 10 # Instance variable
        self.com = "BMW" # Instance variable
        

c1 = Car()
c2 = Car()

c1.mil = 8

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

## Class variables are shared so if you change the class varibles it effects
## Both instances of Car()

Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)