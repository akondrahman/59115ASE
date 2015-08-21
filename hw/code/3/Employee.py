# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 12:02:46 2015

@author: akond
"""

class Employee(object):
    def __initialize__(self, nameP, ageP):
        self.name = nameP 
        self.age = ageP 
    def __str__(self): 
        #import pprint
        strToRet =  object.__str__(self) + " name" + "    " + self.name + ", age     " + str(self.age)
        #myPrinter = pprint.PrettyPrinter()
        #myPrinter.pprint(self)        
        return strToRet

    #def printEmployeeDetails(self):
        #if you don't pass *self* as a parameter, python can't fidn what object to reference to !!
        #print "Employee details--name-{}-age-{}".format(self.name, self.age)

    def __gt__(self, other):
        ##operator overloading to compare Employee type objects based on age
        return self.age > other.age

    def __lt__(self, other):
        ##operator overloading to compare Employee type objects based on age
        return self.age < other.age
        
    def __eq__(self, other):
        return self.age == other.age


emp1 = Employee()       
emp2 = Employee()
emp1.age=50
emp1.name="Bob"
emp2.name="Alice"
emp2.age=25
#emp1.printEmployeeDetails()
print emp1
print "---------------"
#emp2.printEmployeeDetails()
print emp2        
print "---------------"
print "Comparison: is {}'s age greater than {}'s ?".format(emp1.name, emp2.name) 
print emp1 > emp2
print "---------------"
print "Comparison: is {}'s age same as {}'s ?".format(emp1.name, emp2.name) 
print emp1 == emp2
print "---------------"
print "Comparison: is {}'s age lesser than {}'s ?".format(emp1.name, emp2.name) 
print emp1 < emp2 