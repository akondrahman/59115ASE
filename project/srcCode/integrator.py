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
  #import IO_Utility 
  #print "### Executing D.E. "
  out_normscore, out_decVec = de(runCountParam, constraintFileNameParam, modelObj,baselineMin,baselineMax,deRunCountParam)    
  tempObj = modelObj(constraintFileNameParam, runCountParam)  
  objByDecVec  = tempObj.getobjfromdecision(out_decVec)
  
  print "Normalized Score ...", out_normscore
  print "The objective scores after all minimization ....UnAc={}, UnPass={}".format(objByDecVec[0], objByDecVec[1])
  #print "Total Score after all ...", out_toScore
  #print "Size of frontier  ", out_n
  #print "Size of objlist: ", len(out_ObjList)
  #IO_Utility.writeObjListToFile("output", "obj_score"+ "_" +str(deRunCountParam)+ "_" +str(runCountParam), out_ObjList)
def runGALE(iterationsP, minBP, maxBP):
  from galeForModel import GALE  
  from galeForModel import distFromHellScore
  from modelForGALE import IPMDFC
  import utility 
  modelObj=IPMDFC()
  galeOutput = GALE(modelObj, iterationsP)
  #print("Final gale out put ", galeOutput) 
  for item in galeOutput: 
    print("item length is " , len(item))   
    print("item is ", item)
    objectivevals = modelObj.solve(item)
    print("objective values are ", objectivevals)
    fromHellScore = distFromHellScore(objectivevals)
    print("Distance from hell score is: ", fromHellScore)
    finalScore = utility.getNormalizedScoreForGale(minBP, maxBP, fromHellScore)
    print("Final score (after normalization ...)", finalScore)