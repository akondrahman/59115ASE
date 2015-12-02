# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:00:57 2015

@author: akond
"""



from random import uniform
class IPMDFC:
  """
  IPMDFC
  """
  def __init__(self, runParam=365):
    self.n_dec = 17
    self.n_obj = 2
    self.runCount = runParam


  def generate(i, n):
    return [[uniform(0,1) for _ in xrange(i.n_dec)] for _ in xrange(n)]


  def solve(self,dec):
     from StateAll import StateAll
     import ModelExecAll
     ##States
     curr = StateAll("CurrentState_inte")
     prev = StateAll("PrevState_inte")
     dt = 1
     stockToRet ={}
     for cnt in xrange(self.runCount):
        val_ = dec
        prev, curr = ModelExecAll.executeModelForBaseline(val_, curr, prev, dt)
        stockToRet[cnt]=[ curr.UndetectedActiveErrors_.curr, curr.UndetectedPassiveErrors_.curr]
     #print("length of stock ", len(stockToRet))   
     return stockToRet[self.runCount -  1]            