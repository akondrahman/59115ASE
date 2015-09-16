import random
from baseline import getVariableBounds, getValidVector, getBaselineMinMaxForO2, calcNormEnergy
import checker

def maxWalkSat(maxTries=100000, maxChanges=10, threshold=.95, p=0.5):
  ''' This is the main place holder fo the MaxSatWalk() Algo '''
  minMaxTuple = getBaselineMinMaxForO2()
  vec = getValidVector()
  start = calcNormEnergy(vec, minMaxTuple)

  for i in range(maxTries):
    solution = start
    for j in range(maxChanges):
      if solution > threshold:
        return solution

      if p < random.random():
        ## when probailility is > 0.5 then we randomly select a variable and mutate it        
        mutate(vec)
        solution = calcNormEnergy(vec, minMaxTuple)
      else:
        ## when probailility is <= 0.5 then we  mutate all the variables in the vector 
        ## one by one ,see which gives the maximum energy, and keep it as solution           
        energyVecList = mutateSelectively(vec, minMaxTuple)
        tempMax = energyVecList[0][1]
        tempVec = energyVecList[0][0]
        for tupE in energyVecList:
          if tempMax <= tupE[1]:
            tempMax= tupE[1]
            tempVec = tupE[0]
        print " Output of mutateSelectively-----> maximum energy: ", tempMax
        print " Output of mutateSelectively-----> corresponding vector: ", tempVec
        solution = tempMax
        tempMax = float(0)
        tempVec = []






def mutate(xVecParam):
  '''This module selects any one of the six variables, and then mutates it only '''
  index = random.randrange(0,6)
  vec = xVecParam
  vec[index] = getVariableBounds(index)

  while not checker.checkConstraints(vec):
   vec[index] = getVariableBounds(index)

  return vec



def mutateSelectively(xVecParam, minMaxTuple):
  '''This module selects any all of the six variables, one by one, mutates it, and keeps track of the energy '''    
  energyVecList = []
  for cnt in range(len(xVecParam)):
    vec = xVecParam
    vec[cnt] = getVariableBounds(cnt)
    while not checker.checkConstraints(vec):
      vec[cnt] = getVariableBounds(cnt)
    energyVecList.append((vec, calcNormEnergy(vec, minMaxTuple)))

  return energyVecList
  
  
maxWalkSat()  
