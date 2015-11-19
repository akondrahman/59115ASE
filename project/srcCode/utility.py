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
   a01_equation = lambda x : random.uniform(0, 1)
   a02_equation = lambda x : random.uniform(0, 1) 
   a11_equation = lambda x : random.uniform(0, 1)
   a14_equation = lambda x : random.uniform(0, 1)
   a15_equation = lambda x : random.uniform(0, 1)    
 
 ## some auxiliaries need equations 
 a01_MultiplierSchedPressure = a01_equation(random.uniform(0, 1))
 listToret.append(a01_MultiplierSchedPressure)
 a02_MultiplierWorkforce = a02_equation(random.uniform(0, 1))
 listToret.append(a02_MultiplierWorkforce) 
 
 a11_MultiplierToRegen = a11_equation(random.uniform(0, 1))
 listToret.append(a11_MultiplierToRegen)  

 a14_ActiveErrorsRetiringFraction = a14_equation(random.uniform(0, 1))
 listToret.append(a14_ActiveErrorsRetiringFraction) 
 a15_FractionEscapingErrors = a15_equation(random.uniform(0, 1))
 listToret.append(a15_FractionEscapingErrors)  
 
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
 

 a12_ActiveErrorDensity = random.uniform(0, 1)
 listToret.append(a12_ActiveErrorDensity) 
 a13_TestingRate = random.uniform(0, 1)
 listToret.append(a13_TestingRate) 

 a16_BadFixGenRate = random.uniform(0, 1)
 listToret.append(a16_BadFixGenRate) 
 a17_PassiveErrorDensity = random.uniform(0, 1)
 listToret.append(a17_PassiveErrorDensity) 
 
 ## Only oen auxiliary has a direct value  
 a10_TimeToSmooth = 40 
 listToret.append(a10_TimeToSmooth)  
 
 if len(listToret) != 17: 
   print "Something is wrong "   
   exit()
 return listToret   
def getFeatureFromDict(dictParam, opType): 
  temp_ = []  
  valToRet = 0 
  for  key_, val_ in dictParam.items():   
    temp_.append(val_[0] + val_[1])
  if opType=="min":
    valToRet = min(temp_) 
  elif opType=="max": 
    valToRet = max(temp_)
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