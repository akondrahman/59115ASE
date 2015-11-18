# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:57:12 2015

@author: akond
"""



from random import uniform
class Model(object):
  def __init__(self):
      self.decisionVec=[0]        
      self.lowerRange=[0]
      self.numOfDec=0
      self.numOfObjs=0        
      self.upperRange=[0]


  def check(self):
    for count in range(0,self.numOfDec):
            if (self.decisionVec[count]<self.lowerRange[count]) or (self.decisionVec[count]>self.upperRange[count]):
              return False
    return True
    
  def generateInitialVector(self):
        ## we use random.uniform() as it geives floating point values as well 
        while True:
            for cnt in range(0,self.numOfDec):
                self.decisionVec[cnt]=uniform(self.lowerRange[cnt],self.upperRange[cnt])
            if self.check(): break

  def getobj(self):
        return []    
        
        
        
        
        
class IntegratedDefectModel(Model): 
  def __init__(self):
    self.decisionVec=[0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0 ] 
    self.lowerRange= [0,0,0, 0,0,0, 0,0,0, 40,0,0, 0,0,0, 0,0 ] 
    self.numOfDec = 17 
    self.numOfObjs = 2
    self.upperRange= [1,1,1, 1,1,1, 1,1,1, 40,1,1, 1,1,1, 1,1 ]
    self.generateInitialVector()     
    
  def check(self):
    for cnt in range(0,self.numOfDec):
      if (self.decisionVec[cnt] < self.lowerRange[cnt]) or (self.decisionVec[cnt]>self.upperRange[cnt]):
         return False
    return True  
    
  def getobj(self, runCountParam):
     from StateAll import StateAll
     import ModelExecAll
     ##States
     curr = StateAll("CurrentState_inte")
     prev = StateAll("PrevState_inte")
     dt = 1
     stockToRet ={}
     for cnt in xrange(runCountParam):
        val_ = self.decisionVec
        prev, curr = ModelExecAll.executeModelForBaseline(val_, curr, prev, dt)
        stockToRet[cnt]=[ curr.UndetectedActiveErrors_.curr, curr.UndetectedPassiveErrors_.curr]
     return stockToRet[runCountParam -  1]             