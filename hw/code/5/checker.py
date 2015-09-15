# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:23:44 2015

@author: akond
"""

from ok import *

def checkVariableBounds(xVecParam):
  valToRet = False
  trueCount = 0
  constList=[]
  if (xVecParam[0] <= 10) and (xVecParam[0]>=0): 
    constList.append(xVecParam[0])       
    trueCount = trueCount + 1 
  if (xVecParam[1] <= 10) and (xVecParam[1]>=0): 
    constList.append(xVecParam[1])    
    trueCount = trueCount + 1 
  if (xVecParam[2] >= 1) and (xVecParam[2] <=5): 
    constList.append(xVecParam[2])    
    trueCount = trueCount + 1 
  if (xVecParam[3] >= 0) and (xVecParam[3] <=6):
    constList.append(xVecParam[3])    
    trueCount = trueCount + 1 
  if (xVecParam[4] >= 1) and (xVecParam[4] <=5):
    constList.append(xVecParam[4])     
    trueCount = trueCount + 1 
  if (xVecParam[-1] >= 0) and (xVecParam[-1] <=10):
    constList.append(xVecParam[-1])    
    trueCount = trueCount + 1 
  #print "*************"
  #print "All conditions are true ? ", trueCount
  #print "*************"
  #print valToRet        
  if(trueCount == 6):
    valToRet = True     
  return valToRet        
  
def checkConstraints(xVecParam):
  import math   
  valToRet = False 
  trueCount = 0 
  if checkVariableBounds(xVecParam): 
      if (xVecParam[0] + xVecParam[1] - 2) >=0: 
        trueCount = trueCount + 1
      if (6 - xVecParam[0] - xVecParam[1] ) >=0:     
        trueCount = trueCount + 1    
      if (2 - xVecParam[1] + xVecParam[0] ) >=0:     
        trueCount = trueCount + 1        
      if (2 - xVecParam[0] + 3 * xVecParam[1] ) >=0: 
        trueCount = trueCount + 1            
      if (4 - math.pow(xVecParam[2] - 3, 2) - xVecParam[3] ) >=0:     
        trueCount = trueCount + 1                
      if (math.pow(xVecParam[4] - 3, 3) + xVecParam[-1] - 4) >=0: 
        trueCount = trueCount + 1                    
  else:
        trueCount = 0       
  #print "true count so far ", trueCount  
  if trueCount==6:
     valToRet =True     
  return valToRet                 