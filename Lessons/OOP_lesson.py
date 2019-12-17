# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:21:53 2019

@author: jline
"""

class Computer:
    def __init__(self, cpu, ram): # gets called automatically
        #print("in init")
        self.cpu = cpu
        self.ram = ram
        
    def config(self): # method in class
        print("Config is ", self.cpu, self.ram)
        
com1 = Computer('i5','16GB')
com2 = Computer('Ryzen 3', 8)

'''
Computer.config(com1) # access method config in object com1
Computer.config(com2) # dont use this first syntax
'''


com1.config() # most commonly used syntax
com2.config()