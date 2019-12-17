# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:17:54 2019

@author: jline
"""
### Duck Typing

class PyCharm:
    
    def execute(self):
        print('Compiling')
        print('Running')


class MyEditor:
    
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print('Compiling')
        print('Running')

class Laptop:
    
    def code(self, ide):
        ide.execute()
        

ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)

## Changing to something that looks like and acts like PyCharm:
ide = MyEditor()
lap1.code(ide)