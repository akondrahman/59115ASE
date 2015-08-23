# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:38:54 2015

@author: akond
"""

def print_plusgrid(colToExpandParam):
    for x in range(0, colToExpandParam):
        temp = x % 5
        if temp==0:      
           print "+" , 
        else:
            print "-" ,
            
def print_slashgrid(colToExpandParam):
    for x in range(0, colToExpandParam):
        temp = x % 5
        if temp==0:      
           print "|" , 
        else:
            print " " ,

def print_grid1():
    colToExpand=11
    for y in range(0, 2): 
        print_plusgrid(colToExpand)
        print " "
        print_slashgrid(colToExpand)
        print " "
        print_slashgrid(colToExpand)
        print " "
        print_slashgrid(colToExpand)
        print " "
        print_slashgrid(colToExpand)
        print " "
    print_plusgrid(colToExpand)    
    
    
def print_grid2():
    colToExpand=16
    for y in range(0, 3): 
        print_plusgrid(colToExpand)
        print " "
        print_slashgrid(colToExpand)
        print " "
        print_slashgrid(colToExpand)
        print " "
        print_slashgrid(colToExpand)
        print " "
        print_slashgrid(colToExpand)
        print " "
    print_plusgrid(colToExpand)    

print " "
print "Grid with three rows and three columns "           
print_grid1() 
print " "
print "Grid with four rows and four columns "           
print_grid2() 
 