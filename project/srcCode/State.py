# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:16:00 2015

@author: akond
"""
from Stock import Stock   
from Flow import Flow   
class State(object):
  def __init__(self, nameP):
    ##Name   
    self.name_ =  nameP      
    ##Stocks  
    self.PotentiallyDetectableError_ = Stock("PotentiallyDetectableError")
    self.EscapedError_ = Stock("EscapedError") 
    self.DetectedError_ = Stock("DetectedError")
    self.ReworkedError_ = Stock("ReworkedError")
    self.stockList = [self.PotentiallyDetectableError_, self.EscapedError_, self.DetectedError_, self.ReworkedError_]
    ## Flow 
    self.ErrGenRate_ = Flow("ErrGenRate")
    self.ErrDetRate_ = Flow("ErrDetRate") 
    self.ErrEscapeRate_ = Flow("ErrEscapeRate")
    self.ReworkRate_ = Flow("ReworkRate") 
    self.flowList = [self.ErrGenRate_, self.ErrDetRate_, self.ErrEscapeRate_, self.ReworkRate_]
  def __str__(self):
    stockStr , dummyStr ="" , ""
    for ite_ in self.stockList:
      dummyStr += "\t" + ite_.name
      stockStr += "\t" + str(ite_.curr)
    str_ = dummyStr + "\n" + "Name: " + self.name_ + " currentStateValues= " +  stockStr 
    return str_ 
  ##All flow related   
  def getFlows(self):
    #dummyStr = "\nFrom left to right ... ErrGenRate_, ErrDetRate_, ErrEscapeRate_, ReworkRate_: "     
    #str_ = str(self.ErrGenRate_.curr) +"\t" + str(self.ErrDetRate_.curr) +"\t"+ str(self.ErrEscapeRate_.curr) +"\t"+ str(self.ReworkRate_.curr)
    #str_ = dummyStr + str_ 
    dummyStr , flowStr ="" , ""
    for ite_ in self.flowList:
      dummyStr += "\t" + ite_.name
      flowStr += "\t" + str(ite_.curr)
    str_ = dummyStr + "\n" + "Name: " + self.name_ + " flow values= " +  flowStr   
    return str_      
  def updateErrGenRate(self, ErrGenRateObj):
    self.ErrGenRate_ = ErrGenRateObj   
    self.flowList[0] = self.ErrGenRate_
  def updateErrDetRate(self, ErrDetRateObj):
    self.ErrDetRate_ = ErrDetRateObj   
    self.flowList[1] = self.ErrDetRate_    
  def updateErrEscapeRate(self, ErrEscapeRateObj):
    self.ErrEscapeRate_ = ErrEscapeRateObj 
    self.flowList[2] = self.ErrEscapeRate_        
  def updateReworkRate(self, ReworkRateObj):
    self.ReworkRate_ = ReworkRateObj 
    self.flowList[3] = self.ReworkRate_            
  ## to copy prev_ from curr_    
  def copy(self, nameParam):
    stateObj = State(nameParam)
    #Flows
    stateObj.ErrDetRate_ = self.ErrDetRate_   
    stateObj.ErrGenRate_ = self.ErrGenRate_   
    stateObj.ErrEscapeRate_ = self.ErrEscapeRate_   
    stateObj.flowList = self.flowList
    #Stocks 
    stateObj.PotentiallyDetectableError_ = self.PotentiallyDetectableError_
    stateObj.EscapedError_ = self.EscapedError_
    stateObj.DetectedError_ = self.DetectedError_
    stateObj.stockList = self.stockList
    return stateObj