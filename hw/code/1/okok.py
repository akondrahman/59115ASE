"""

# Examples of Unit tests  in Python

"""
'''
This code works on top of Dr. Tim Menzies' code 
provided in CSC 591 class of Fall 2015 @ NCSU 
I have added two more test cases: one fails, one passes 
I have adjusted _ok4() accordingly 
'''
import time
from ok import *

print time.strftime("%H:%M:%S\n")

@ok
def _ok1():
  assert 1==1

@ok
def _ok2():
  assert 2==1

@ok
def _ok3():
  assert 3==3 

@ok
def _okx():
  assert 100==100 
  
@ok
def _oky():
  assert 31==13   
  

@ok
def _ok4():
  assert unittest.tries==6
  assert unittest.fails==2
  print unittest.score() 
