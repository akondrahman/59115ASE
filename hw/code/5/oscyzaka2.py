# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:48:07 2015

@author: akond
"""

import checker, math

def _firstObj(xVecParam):
  valToRet = 0   
  if(checker.checkVariableBounds(xVecParam)):
    if(checker.checkConstraints(xVecParam)):
      factor1 = 25 * math.pow(xVecParam[0] - 2, 2)
      factor2 = math.pow(xVecParam[1] - 2, 2)
      factor3 = math.pow(xVecParam[2] - 1, 2) * math.pow(xVecParam[3] - 4, 2) 
      factor4 = math.pow(xVecParam[4] - 1, 2)
      valToRet = -1 * (factor1 + factor2 + factor3 + factor4)
    else:
      valToRet =  float('nan')  
      print "First Objective Failed : Input vector violates Oscyzaka-II's constraints !" , xVecParam   
  else:
      valToRet =  float('nan')        
      print "First Objective Failed : Input vector violates Oscyzaka-II's variable bounds !", xVecParam
  return valToRet        
  
  
  
  
def _secondObj(xVecParam):
  valToRet = 0   
  if(checker.checkVariableBounds(xVecParam)):
    if(checker.checkConstraints(xVecParam)):
      for valI in xVecParam:  
        valToRet = valToRet + math.pow(valI, 2)
    else:
      valToRet =  float('nan')  
      print "Second Objective Failed : Input vector violates Oscyzaka-II's constraints !", xVecParam    
  else:
      valToRet =  float('nan')        
      print "Second Objective Failed : Input vector violates Oscyzaka-II's variable bounds !", xVecParam
  #print valToRet    
  return valToRet          