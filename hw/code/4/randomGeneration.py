# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:21:32 2015

@author: akond
"""

maxRange= 100000
minRange=-100000

def getNeighborRandonmly(neighborVec):
  import math, random 
  vecToRet=[]
  maxRange=neighborVec[2]
  minRange=neighborVec[0]
  currentValP=neighborVec[1]
  disFromMin=math.sqrt(math.pow( float(currentValP - minRange), 2))    
  disFromMax=math.sqrt(math.pow( float(currentValP - maxRange), 2))   
  #print "minDist = {}, maxDist={}".format(disFromMin, disFromMax)
  disToLook = max(disFromMin, disFromMax)
  randToRet = random.randrange(currentValP - disToLook, currentValP + disToLook)
  #print  "rand to ret ....", randToRet
  vecToRet = [currentValP - disToLook, randToRet , currentValP + disToLook]
  return vecToRet

def getRandVec():
  import random 
  randToret = 0 
  randToret = random.randrange(minRange, maxRange)
  vecToRet=[minRange, randToret ,maxRange]
  return vecToRet


def getRandVal():
  import random 
  #maxRange=100000
  #minRange=-100000
  #randToret = 0 
  randToret = random.randrange(minRange, maxRange)
  #vecToRet=[minRange, randToret ,maxRange]
  return randToret
  
def getProbOfAcceptance(currEnergyP, neighbourEnergyP, tParam):
  # t = k/kmax
  import math
  equation = float(1*(currEnergyP-neighbourEnergyP)/float(tParam))
  accepProbToret = math.exp(equation)
  return accepProbToret




def getRandomProb():
   import random 
   return random.random()   




#getNeighborRandonmly(-100)    