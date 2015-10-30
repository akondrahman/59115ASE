# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:40:32 2015

@author: akond
"""



from ModelComponent import ModelComponent 
class Flow(ModelComponent):
  def setInput(self, inputVal):
   self.curr = self.curr + inputVal
        