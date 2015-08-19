# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:06:42 2015

@author: akond
"""



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

print "Output of do_twice"
do_twice(print_twice, "spam")

def do_four(f, valParam):
    do_twice(f, valParam)
    do_twice(f, valParam)
    
#def another_do_four(f, valParam):
#    do_twice(f, valParam)
#    mod_do_twice(f, valParam)    
    

#mod_do_twice(print_twice, "spam")
print "Output of do_four"
do_four(mod_print_spam, "dummy test string")    