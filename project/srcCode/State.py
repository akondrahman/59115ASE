# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:16:00 2015

@author: akond
"""
from Stock import Stock   
from Flow import Flow   
class State(object):

  def __init__(self, nameP):
    self.ErrGenRate = Flow("ErrGenRate")
    self.PotentiallyDetectableError = Stock("PotentiallyDetectableError")
    self.EscapedError = Stock("EscapedError")    
    self.ErrDetRate = Flow("ErrDetRate") 
    self.name =  nameP
    self.ErrEscapeRate = Flow("ErrEscapeRate")
  def __str__(self):
    stockStr =   str(self.PotentiallyDetectableError.curr )   + " " +  str(self.EscapedError.curr )
    str_ = "Name: " + self.name + " currentStateValue=  " +  stockStr
    return str_ 
  def updateErrGenRate(self, ErrGenRateObj):
    self.ErrGenRate = ErrGenRateObj   
  def updateErrDetRate(self, ErrDetRateObj):
    self.ErrDetRate = ErrDetRateObj       
  def updateErrEscapeRate(self, ErrEscapeRateObj):
    self.ErrEscapeRate = ErrEscapeRateObj 
  def copy(self, nameParam):
    stateObj = State(nameParam)
    stateObj.ErrDetRate = self.ErrDetRate   
    stateObj.ErrGenRate = self.ErrGenRate   
    stateObj.ErrEscapeRate = self.ErrEscapeRate     
    stateObj.PotentiallyDetectableError = self.PotentiallyDetectableError
    stateObj.EscapedError = self.EscapedError
    return stateObj