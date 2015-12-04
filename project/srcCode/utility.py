# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:44:38 2015

@author: akond
"""



from contextlib import contextmanager
########## Top Part Obsolete#############
#def createAuxiliaries_Top():
#  dict_={}
#  dict_['Day-0'] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#  dict_['Day-1'] = [1, 1, 1, 1, 1, 1, 1, 15, 1]
#  dict_['Day-2'] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
#  dict_['Day-3'] = [2, 2, 2, 2, 2, 2, 2, 2, 2]
#  dict_['Day-4'] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
#  dict_['Day-5'] = [10, 10, 10, 10, 10, 10, 10, 10, 10]
#  dict_['Day-6'] = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
#  return dict_
#
#
#
#
#
#
#
#def createTestStock_Top():
#  dict_={}
#  dict_['Day-0'] = [0, 0, 0, 0]
#  dict_['Day-1'] = [0, 0, 0, 0]
#  dict_['Day-2'] = [1, -15, 2, 16]
#  dict_['Day-3'] = [2, -16, 4, 18]
#  dict_['Day-4'] = [4, -18, 8, 22]
#  dict_['Day-5'] = [5, -19, 10, 24]
#  dict_['Day-6'] = [15, -29, 30, 44]
#  return dict_
#
#
#
########### Bottom Part #############
#def createTestStock_Bottom():
#  dict_={}
#  dict_['Day-0'] = [0]
#  dict_['Day-1'] = [0]
#  dict_['Day-2'] = [2]
#  dict_['Day-3'] = [4]
#  dict_['Day-4'] = [8]
#  dict_['Day-5'] = [10]
#  dict_['Day-6'] = [30]
#  return dict_
#  
#  
#def createAuxiliaries_Bottom():
#  dict_={}
#  dict_['Day-0'] = [0, 0, 0, 0, 0, 0, 0,0]
#  dict_['Day-1'] = [1, 1, 1, 1, 1, 1, 1,1]
#  dict_['Day-2'] = [1, 1, 1, 1, 1, 1, 1,1]
#  dict_['Day-3'] = [2, 2, 2, 2, 2, 2, 2,2]
#  dict_['Day-4'] = [1, 1, 1, 1, 1, 1, 1,1]
#  dict_['Day-5'] = [10, 10, 10, 10, 10, 10, 10,10]
#  dict_['Day-6'] = [-1, -1, -1, -1, -1, -1, -1,-1]
#  return dict_


########### ALL ##########  
def createAuxiliaries_All():
  dict_={}
  dict_['Day-0'] = [0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0]
  dict_['Day-1'] = [1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1]
  dict_['Day-2'] = [1, 1, 1, 1, 1, 1, 1,1,1, 1, 1, 1, 1, 1, 1,1,1]
  dict_['Day-3'] = [2, 2, 2, 2, 2, 2, 2,2,2, 2, 2, 2, 2, 2, 2,2,2]
  dict_['Day-4'] = [1, 1, 1, 1, 1, 1, 1,1,1, 1, 1, 1, 1, 1, 1,1,1]
  dict_['Day-5'] = [10, 10, 10, 10, 10, 10, 10,10,10, 10, 10, 10, 10, 10, 10,10,10]
  dict_['Day-6'] = [-1, -1, -1, -1, -1, -1, -1,-1,-1, -1, -1, -1, -1, -1, -1,-1,-1]
  return dict_  
  



def createTestStock_All():
  dict_={}
  dict_['Day-0'] = [0, 0, 0, 0, 0, 0]
  dict_['Day-1'] = [0, 0, 0, 0, 0, 0]
  dict_['Day-2'] = [1, 2, -1, 2, 6, 6]
  dict_['Day-3'] = [2, 4, -2, 4, 12, 6]
  dict_['Day-4'] = [4, 8, -4, 8, 24, 12]
  dict_['Day-5'] = [5, 10, -5, 10, 30, 6]
  dict_['Day-6'] = [15, 30, -15, 30, 90, 60]
  return dict_
def giveAuxiliariesForBaseline(constFlagParam):
 import random    , math
 listToret= [] 
 
 ##for setting up auxiliaries that need regression equation 
 if constFlagParam:
   a01_equation = lambda x : 0.2128 * math.pow(x, 2) + 0.2955 * x + 0.9888
   a02_equation = lambda x : -x + 2 
   a11_equation = lambda x : 0.828 * math.exp(0.0173 * x)
   a14_equation = lambda x : 0.0004 * math.exp(7.2984 * x) 
   a15_equation = lambda x : -1.0286 * math.pow(x,2)  - 0.2283 * x + 1.0719 if x>= 0.4 else 0
 else:
   a01_equation = lambda x : random.uniform(x, 1)
   a02_equation = lambda x : random.uniform(x, 1) 
   a11_equation = lambda x : random.uniform(x, 1)
   a14_equation = lambda x : random.uniform(x, 1)
   a15_equation = lambda x : random.uniform(x, 1)    
 
 ## some auxiliaries need equations 
 a01_MultiplierSchedPressure = a01_equation(random.uniform(0, 1))
 listToret.append(a01_MultiplierSchedPressure)
 a02_MultiplierWorkforce = a02_equation(random.uniform(0, 1))
 listToret.append(a02_MultiplierWorkforce) 

 ## most aixiliaries are assumed to be between 0 & 1 
 a03_NominalErr = random.uniform(0, 1)
 listToret.append(a03_NominalErr) 
 a04_SWDevelopmentRate = random.uniform(0, 1)
 listToret.append(a04_SWDevelopmentRate) 
 a05_PotErrDetectRate = random.uniform(0, 1)
 listToret.append(a05_PotErrDetectRate) 
 a06_AvgErrPerTask = random.uniform(0, 1)
 listToret.append(a06_AvgErrPerTask) 
 a07_QARate = random.uniform(0, 1)
 listToret.append(a07_QARate) 
 a08_ActualReworkMP = random.uniform(0, 1)
 listToret.append(a08_ActualReworkMP) 
 a09_DailyMPRework = random.uniform(0, 1)
 listToret.append(a09_DailyMPRework) 


 ## Only oen auxiliary has a direct value  
 a10_TimeToSmooth = random.uniform(0, 1)
 listToret.append(a10_TimeToSmooth)  
 
 a11_MultiplierToRegen = a11_equation(random.uniform(0, 1))
 listToret.append(a11_MultiplierToRegen)  


 a12_ActiveErrorDensity = random.uniform(0, 1)
 listToret.append(a12_ActiveErrorDensity) 
 a13_TestingRate = random.uniform(0, 1)
 listToret.append(a13_TestingRate) 


 a14_ActiveErrorsRetiringFraction = a14_equation(random.uniform(0, 1))
 listToret.append(a14_ActiveErrorsRetiringFraction) 
 a15_FractionEscapingErrors = a15_equation(random.uniform(0, 1))
 listToret.append(a15_FractionEscapingErrors)  
 

 a16_BadFixGenRate = random.uniform(0, 1)
 listToret.append(a16_BadFixGenRate) 
 a17_PassiveErrorDensity = random.uniform(0, 1)
 listToret.append(a17_PassiveErrorDensity) 
 

 
 if len(listToret) != 17: 
   print "Something is wrong "   
   exit()
 return listToret   

def getStockOnInterestBasedOnValue(dictP, valP, temp_):
    indexOfInterest = temp_.index(valP)
    stock_1= dictP[indexOfInterest][0]
    stock_2= dictP[indexOfInterest][1]    
    return stock_1, stock_2    
def getFeatureFromDict(dictParam, opType): 
  temp_ = []  
  valToRet = 0 
  for  key_, val_ in dictParam.items():   
    temp_.append(val_[0] + val_[1])
  if opType=="min":
    valToRet = min(temp_) 
    stock_1, stock_2 =getStockOnInterestBasedOnValue(dictParam, valToRet, temp_)
    print "Corresponding index item for baseline min: UndetectedActiveErrors= {}, UndetectedPassiveErrors={}".format(stock_1, stock_2)
  elif opType=="max": 
    valToRet = max(temp_)
    stock_1, stock_2 =getStockOnInterestBasedOnValue(dictParam, valToRet, temp_)
    print "Corresponding index item for baseline max: UndetectedActiveErrors= {}, UndetectedPassiveErrors={}".format(stock_1, stock_2)    
  else: 
    print "operation not recongized ... provided operation type: ", opType
  return   valToRet  

@contextmanager
def duration():
  import time  
  t1 = time.time()
  yield
  t2 = time.time()
  print("\n" + "-" * 72)
  print("# Runtime: %.3f secs" % (t2-t1)) 
def getAuxNameList():
  auxNameList = []      
  auxNameList.append("a01_MultiplierSchedPressure")
  auxNameList.append("a02_MultiplierWorkforce")
  auxNameList.append("a03_NominalErr")
  auxNameList.append("a04_SWDevelopmentRate")
  auxNameList.append("a05_PotErrDetectRate")
  auxNameList.append("a06_AvgErrPerTask")
  auxNameList.append("a07_QARate")
  auxNameList.append("a08_ActualReworkMP")
  auxNameList.append("a09_DailyMPRework")
  auxNameList.append("a10_TimeToSmooth")
  auxNameList.append("a11_MultiplierToRegen")
  auxNameList.append("a12_ActiveErrorDensity")
  auxNameList.append("a13_TestingRate")
  auxNameList.append("a14_ActiveErrorsRetiringFraction")
  auxNameList.append("a15_FractionEscapingErrors")
  auxNameList.append("a16_BadFixGenRate")
  auxNameList.append("a17_PassiveErrorDensity")    
  return auxNameList
  
def createAuxList(lowerRange, upperRange, constFlagParam): 
  import random   , math

  lowRangeList = []
  upperRangeList = []

  ## fixing low range 

  ##for setting up auxiliaries that need regression equation 
  if constFlagParam:
   a01_equation = lambda x : 0.2128 * math.pow(x, 2) + 0.2955 * x + 0.9888
   a02_equation = lambda x : -x + 2 
   a11_equation = lambda x : 0.828 * math.exp(0.0173 * x)
   a14_equation = lambda x : 0.0004 * math.exp(7.2984 * x) 
   a15_equation = lambda x : -1.0286 * math.pow(x,2)  - 0.2283 * x + 1.0719 if x>= 0.4 else 0
  else:
   a01_equation = lambda x : random.uniform(x, 1)
   a02_equation = lambda x : random.uniform(x, 1) 
   a11_equation = lambda x : random.uniform(x, 1)
   a14_equation = lambda x : random.uniform(x, 1)
   a15_equation = lambda x : random.uniform(x, 1)    
 
  ## some auxiliaries need equations 
  temprand1 = random.uniform(lowerRange, upperRange)
  a01_MultiplierSchedPressure = a01_equation(temprand1)
  #print "Aux # 1: low: {} & high: {}".format(temprand1, a01_MultiplierSchedPressure)
  upperRangeList.append(a01_MultiplierSchedPressure)
  lowRangeList.append(lowerRange)
  #temprand1 = 0 
  #a01_MultiplierSchedPressure = 0 

  ## the equations of auxiary 2 is  weird in the sense that as x increases, y decreases, for x >=1 as the equation is -x+2 . 
  ## as a result we get a range that is impossible to satisfy. Therefore we use the follwoing heuristic: 
  ## to get y plug in any random value between 0 & 1 or 0 & 10,but the corresponding lower range will be parameter lowerRange 
  ##for A11 

  temprand2 = random.uniform(lowerRange, upperRange)  
  a02_MultiplierWorkforce = a02_equation(temprand2)
  #print "Aux # 2: low: {} & high: {}".format(temprand2, a02_MultiplierWorkforce)  
  upperRangeList.append(a02_MultiplierWorkforce) 
  lowRangeList.append(lowerRange) 
  
  
  ## most auxiliaries are assumed to be between 0 & 1 
  a03_NominalErr = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a03_NominalErr) 
  lowRangeList.append(lowerRange)
  
  a04_SWDevelopmentRate = random.uniform(lowerRange, upperRange)
  lowRangeList.append(lowerRange)
  upperRangeList.append(a04_SWDevelopmentRate) 
  
  a05_PotErrDetectRate = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a05_PotErrDetectRate) 
  lowRangeList.append(lowerRange)
  
  a06_AvgErrPerTask = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a06_AvgErrPerTask) 
  lowRangeList.append(lowerRange)
  
  a07_QARate = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a07_QARate) 
  lowRangeList.append(lowerRange)
  
  a08_ActualReworkMP = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a08_ActualReworkMP) 
  lowRangeList.append(lowerRange)
  
  a09_DailyMPRework = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a09_DailyMPRework) 
  lowRangeList.append(lowerRange)

  ## Only oen auxiliary has a direct value  
  a10_TimeToSmooth = random.uniform(lowerRange, upperRange) 
  upperRangeList.append(a10_TimeToSmooth)   
  lowRangeList.append(lowerRange)

  ## the equations of auxiary 11 is  weird in the sense that as x increases, y decreases. 
  ## as a result we get a range that is impossible to satisfy. Therefore we use the follwoing heuristic: 
  ## to get y plug in any random value btween 0 & 1,but the corresponding lower range will be parameter lowerRange 
  ##for A11 

  temprand3 = random.uniform(lowerRange, upperRange)    
  a11_MultiplierToRegen = a11_equation(temprand3)
  #print "Aux # 11: low: {} & high: {}".format(temprand3, a11_MultiplierToRegen)    
  upperRangeList.append(a11_MultiplierToRegen)  
  lowRangeList.append(lowerRange)

  a12_ActiveErrorDensity = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a12_ActiveErrorDensity) 
  lowRangeList.append(lowerRange)
  
  a13_TestingRate = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a13_TestingRate) 
  lowRangeList.append(lowerRange)
  
  ## teh quations of auxiary 14 and 15 are weird in the sense that as x increases,y decreases. 
  ## as a result we get a range that is impossible to satisfy. Therefore we use teh follwoing heuristic: 
  ## to get y plugin ina ny random value btween 0 & 1,but the corresponding lower range will be parameter lowerRange 
  ##for both A14 & A15 
  
  temprand4 = random.uniform(lowerRange, upperRange)    
  a14_ActiveErrorsRetiringFraction = a14_equation(temprand4)
  #print "Aux # 14: low: {} & high: {}".format(temprand4, a14_ActiveErrorsRetiringFraction)      
  upperRangeList.append(a14_ActiveErrorsRetiringFraction) 
  lowRangeList.append(lowerRange)  
  
  temprand5 = random.uniform(lowerRange, upperRange)      
  a15_FractionEscapingErrors = a15_equation(temprand5)
  #print "Aux # 15: low : {} & high: {}".format(temprand5, a15_FractionEscapingErrors)        
  upperRangeList.append(a15_FractionEscapingErrors)  
  lowRangeList.append(lowerRange)     

  a16_BadFixGenRate = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a16_BadFixGenRate) 
  lowRangeList.append(lowerRange)
  
  a17_PassiveErrorDensity = random.uniform(lowerRange, upperRange)
  upperRangeList.append(a17_PassiveErrorDensity) 
  lowRangeList.append(lowerRange)
  
  
  
  return lowRangeList, upperRangeList
#### normalized score with respect to baseline for gale  
def getNormalizedScoreForGale(minBP, maxBP, scoreParam ):
  score = (scoreParam - minBP) / ( maxBP - minBP + 0.001)  
  return score   