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
    ## Top Stocks
    self.PotentiallyDetectableError_ = Stock("PotentiallyDetectableError")
    self.EscapedError_ = Stock("EscapedError")
    self.DetectedError_ = Stock("DetectedError")
    self.ReworkedError_ = Stock("ReworkedError")

    # Test Top Stock List
    #self.stockList = [self.PotentiallyDetectableError_, self.EscapedError_, self.DetectedError_, self.ReworkedError_]

    ## Bottom Stocks
    self.UndetectedActiveErrors_ = Stock("UndetectedActiveErrors")

    # Test Bottom Stock List
    self.stockList = [self.UndetectedActiveErrors_]

    ## Top Flows
    self.ErrGenRate_ = Flow("ErrGenRate")
    self.ErrDetRate_ = Flow("ErrDetRate")
    self.ErrEscapeRate_ = Flow("ErrEscapeRate")
    self.ReworkRate_ = Flow("ReworkRate")

    # Test Top Flows
    #self.flowList = [self.ErrGenRate_, self.ErrDetRate_, self.ErrEscapeRate_, self.ReworkRate_]

    ## Bottom Flows
    self.ActiveErrorRegenRate_ = Flow("ActiveErrorRegenRate")
    self.ActiveErrorDetectAndCorrectRate_ = Flow("ActiveErrorDetectAndCorrectRate")
    self.ActiveErrorRetirementRate_ = Flow("ActiveErrorRetirementRate")
    # self.PassiveErrorDetectionRate_ = Flow("PassiveErrorDetectionRate")
    # self.PassiveErrorGenRate_ = Flow("PassiveErrorGenRate")
    self.ActiveErrorGenRate_ = Flow("ActiveErrorGenRate")

    # Test Bottom Lists
    self.flowList = [self.ActiveErrorRegenRate_, self.ActiveErrorDetectAndCorrectRate_, self.ActiveErrorRetirementRate_, self.ActiveErrorGenRate_]

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

  # Flow updates methods for Top
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

  ## Flow update methods for Bottom
  def updateActiveErrorRegenRate(self, Obj):
    self.ActiveErrorRegenRate_ = Obj
    self.flowList[0] = self.ActiveErrorRegenRate_

  def updateActiveErrorDetectAndCorrectRate(self, Obj):
    self.ActiveErrorDetectAndCorrectRate_ = Obj
    self.flowList[1] = self.ActiveErrorDetectAndCorrectRate_

  def updateActiveErrorRetirementRate(self, Obj):
    self.ActiveErrorRetirementRate_ = Obj
    self.flowList[2] = self.ActiveErrorRetirementRate_

  def updateActiveErrorGenRate(self, Obj):
    self.ActiveErrorGenRate_ = Obj
    self.flowList[3] = self.ActiveErrorGenRate_

  ## to copy prev_ from curr_
  def copyTop(self, nameParam):
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


  def copyBottom(self, nameParam):
    stateObj = State(nameParam)

    #Flows
    stateObj.ActiveErrorGenRate_ = self.ActiveErrorGenRate_
    stateObj.ActiveErrorDetectAndCorrectRate_ = self.ActiveErrorDetectAndCorrectRate_
    stateObj.ActiveErrorRetirementRate_ = self.ActiveErrorRetirementRate_
    stateObj.ActiveErrorRegenRate_ = self.ActiveErrorRegenRate_
    stateObj.flowList = self.flowList

    #Stocks
    stateObj.UndetectedActiveErrors_ = self.UndetectedActiveErrors_
    stateObj.stockList = self.stockList

    return stateObj
