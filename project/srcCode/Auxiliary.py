# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:32:07 2015

@author: akond
"""



from ModelComponent import ModelComponent
class Auxiliary(ModelComponent):
  def setInput(self, inputVal):
   self.curr = self.curr + inputVal