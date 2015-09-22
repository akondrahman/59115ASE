import random
#import math
from oscyzaka2 import _firstObj, _secondObj
import checker

def calcNormEnergy(xVecParam, minMaxTuple):
  ''' reused materials from code 4 '''  
  #print maxSchafferP
  minO2P = minMaxTuple[0]
  maxO2P = minMaxTuple[1]
  return (float(_getEnergy(xVecParam)) - minO2P) / (maxO2P - minO2P)


def _getEnergy(xVecParam):

  f1 = _firstObj(xVecParam)
  f2 = _secondObj(xVecParam)

  valToRet = f1 + f2
  #print "**********", valToRet
  return  valToRet


def getBaselineMinMaxForO2():
  ''' reused materials from code 4 '''
  minMaxTuple=[]
  #minVal = -100000
  #maxVal = 100000
  val = getValidVector()
  minEnergy = _getEnergy(val)
  maxEnergy = _getEnergy(val)
  for cnt in range(100):
   valToUse  =  getValidVector()
   energyToCheck = _getEnergy(valToUse)
   if energyToCheck < minEnergy:
     minEnergy = energyToCheck
   if energyToCheck > maxEnergy:
     maxEnergy = energyToCheck

  minMaxTuple.append(minEnergy)
  minMaxTuple.append(maxEnergy)
  return minMaxTuple


# A function for retrieving a random value within the upper and lower bounds for each variable
def getVariableBounds(varIndex):

  if (varIndex == 0):
    return random.randrange(0, 11)

  if (varIndex == 1):
    return random.randrange(0, 11)

  if (varIndex == 2):
    return random.randrange(1, 6)

  if (varIndex == 3):
    return random.randrange(0, 7)

  if (varIndex == 4):
    return random.randrange(1, 6)

  if (varIndex == 5):
    return random.randrange(0, 11)


# Ensures that the generated vector passes constraints
def getValidVector():
  vec =  [getVariableBounds(0), getVariableBounds(1), getVariableBounds(2), getVariableBounds(3), getVariableBounds(4), getVariableBounds(5)]
  while not checker.checkConstraints(vec):
    vec =  [getVariableBounds(0), getVariableBounds(1), getVariableBounds(2), getVariableBounds(3), getVariableBounds(4), getVariableBounds(5)]

  return vec

# A function for retrieving a random value within the upper and lower bounds for each variable
def getCompleteRange(varIndex):
  tupToRet=()
  if (varIndex == 0):
    tupToRet=(0, 11)

  if (varIndex == 1):
    tupToRet=(0, 11)

  if (varIndex == 2):
    tupToRet=(1, 6)

  if (varIndex == 3):
    tupToRet=(0, 7)

  if (varIndex == 4):
    tupToRet=(1, 6)

  if (varIndex == 5):
    tupToRet=(0, 11)
    
    
    
  return  tupToRet

