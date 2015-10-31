# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:40:32 2015

@author: akond
"""



from ModelComponent import ModelComponent 
class Flow(ModelComponent):
  def resetInput(self):
   self.curr = 0  
  def setInput(self, inputVal):
   self.curr = self.curr + inputVal
  def fillFlowsByAuxs(self, *auxP):
      for i_ in auxP: 
       self.setInput(i_.curr)            