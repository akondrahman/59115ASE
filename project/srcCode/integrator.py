# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:13:00 2015

@author: akond
"""



from de import *
def integrateWithDummies():
  import utility , ModelExecAll
  from StateAll import StateAll
  testStockToRet={}
  ##States
  curr = StateAll("CurrentState_inte")
  prev = StateAll("PrevState_inte")
  dt = 1
  ## dict to use now has dummy auxuliaries .... D.E will create a  list of auxiliaries 
  dictToUse = utility.createAuxiliaries_All() 
  for key_, val_ in dictToUse.items():
    prev, curr = ModelExecAll.executeModelForDE(val_, curr, prev, dt)
    print "{} -----> {}".format(key_, curr)
    ## other than printing we not doign anythign with the 'current state' : when D.E. come sinto play D.E. will use 
    ## the current state's two objectives and do its own mutation. No baseline needed  
    testStockToRet[key_]=[curr.PotentiallyDetectableError_.curr, curr.EscapedError_.curr, curr.DetectedError_.curr, curr.ReworkedError_.curr, curr.UndetectedActiveErrors_.curr, curr.UndetectedPassiveErrors_.curr]
  return testStockToRet  

           
           
def runModelForBaseline(runCountParam, constFlagForBaselineP):
  import  ModelExecAll, utility 
  from StateAll import StateAll
  stockToRet={}
  ##States
  curr = StateAll("CurrentState_inte")
  prev = StateAll("PrevState_inte")
  dt = 1
  for cnt in xrange(runCountParam):
    val_ = utility.giveAuxiliariesForBaseline(constFlagForBaselineP)  
    prev, curr = ModelExecAll.executeModelForBaseline(val_, curr, prev, dt)
    stockToRet[cnt]=[ curr.UndetectedActiveErrors_.curr, curr.UndetectedPassiveErrors_.curr]
  return stockToRet             
  

def runDE(baselineMin, baselineMax, modelObj, deRunCountParam, runCountParam, constraintFileNameParam):
   
  #print "### Executing D.E. "
  de(runCountParam, constraintFileNameParam, modelObj,baselineMin,baselineMax,deRunCountParam)    
    