# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:30:45 2015

@author: akond
"""



class ModelComponent(object): 
  def __init__(self, nameStr):
    self.curr = 0   
    self.name =  nameStr
  def __str__(self): 
   strToRet =  self.name + ": "  + ", current=" + str(self.curr)
   return strToRet 