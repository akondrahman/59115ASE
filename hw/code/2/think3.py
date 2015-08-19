# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:43:20 2015

@author: akond
"""

## Exercise 3.1 

#repeat_lyrics()
    
#def print_lyrics():
#    print "I'm a lumberjack, and I'm okay."
#    print "I sleep all night and I work all day."      

#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()
    
## Exercise 3.2 
    

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
  
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."      
    
print "----------------------"    
print "Output of repeat_lyrics()"     
repeat_lyrics()     
print "----------------------"    

def right_justify(s): 
    print "{:>70}".format(s)
    
print "----------------------"    
print "Output of right_justify()"    
right_justify("Akond")
print "----------------------"    

def do_twice(f, valueParam):
    f(valueParam)
    f(valueParam)
    
def mod_do_twice(f, valueParam):
    f(valueParam)
    f(valueParam)    

def print_spam(dummyParam):
    #print 'spam' + ' ' + dummyParam 
    print 'spam' 
    
def mod_print_spam(dummyParam):
    #print 'spam' + ' ' + dummyParam 
    print 'spam'  + ' ' + dummyParam    
    
def print_twice(dummyParam):
    print dummyParam 
    print dummyParam

print "----------------------"    
print "Output of do_twice()"
do_twice(print_twice, "spam")
print "----------------------"    

def do_four(f, valParam):
    do_twice(f, valParam)
    do_twice(f, valParam)
    
#def another_do_four(f, valParam):
#    do_twice(f, valParam)
#    mod_do_twice(f, valParam)    
    

#mod_do_twice(print_twice, "spam")
print "----------------------"    
print "Output of do_four()"
do_four(mod_print_spam, "dummy test string")    
print "----------------------"  


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
           print "/" , 
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