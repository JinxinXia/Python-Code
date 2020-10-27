# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:41:57 2020

@author: Jinxin
"""

# Ways to track employee information

# Use list to store employee information
kirk = ["James Kirk",34,'Captain',2265]
spock = ["Spock",35,"Science Officer",2254]
mccoy = ["Leonard McCoy","Chief Medical Officer",2266]


# Use class to store information about object
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self,sound):
        return f"{self.name} barks {sound}"
    
    # str method will show description
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
     
# Parent Classes & Child Classes
class JackRussellTerrier(Dog):

    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

