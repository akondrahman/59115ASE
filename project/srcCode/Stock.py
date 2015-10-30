# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:53:31 2015

@author: akond
"""



from ModelComponent import ModelComponent
class Stock(ModelComponent):
  def setInput(self, inputVal):
   self.curr = self.curr + inputVal
             