# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:29:30 2015

@author: akond
"""



def calcNormEnergy(valP, minSchafferP, maxSchafferP):
  #print maxSchafferP   
  return (float(_getEnergy(valP)) - minSchafferP) / (maxSchafferP - minSchafferP)    
  
def _getEnergy(valP):
  import math  
  f1 = math.pow(valP, 2)
  f2 = math.pow((valP - 2), 2)
  valToRet = f1 + f2 
  #print "**********", valToRet
  return  valToRet     


def getBaselineMinMaxForSchaffer():
  import random  
  minMaxTuple=[]  
  minVal = -100000
  maxVal = 100000
  val = random.randrange(minVal, maxVal)   
  minEnergy = _getEnergy(val)   
  maxEnergy = _getEnergy(val)
  for cnt in range(100): 
   valToUse  = random.randrange(minVal, maxVal)   
   energyToCheck = _getEnergy(valToUse)
   if energyToCheck < minEnergy: 
     minEnergy = energyToCheck
   if energyToCheck > maxEnergy: 
     maxEnergy = energyToCheck
  
  minMaxTuple.append(minEnergy)
  minMaxTuple.append(maxEnergy)
  return minMaxTuple