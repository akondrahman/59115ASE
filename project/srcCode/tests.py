# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:10:56 2015

@author: akond
"""



from ok import * 
import utility , ModelExec
testDictSyn = utility.createTestStock_Top()  
testDictMod = ModelExec.executeModelTop()
@ok
def _testStock_PotentiallyDetectableError():
  auxDictLen = len(utility.createAuxiliaries_Top())
  for i_ in xrange(auxDictLen):
    key_ = "Day-"+ str(i_) 
    assert testDictSyn[key_][0]== testDictMod[key_][0]    
    
@ok
def _testStock_DetectedError_():
  auxDictLen = len(utility.createAuxiliaries_Top())
  for i_ in xrange(auxDictLen):
    key_ = "Day-"+ str(i_) 
    assert testDictSyn[key_][1]== testDictMod[key_][1] 


@ok
def _testStock_EscapedError_():
  auxDictLen = len(utility.createAuxiliaries_Top())
  for i_ in xrange(auxDictLen):
    key_ = "Day-"+ str(i_) 
    assert testDictSyn[key_][2]== testDictMod[key_][2]       
    
    
@ok
def _testStock_ReworkedError_():
  auxDictLen = len(utility.createAuxiliaries_Top())
  for i_ in xrange(auxDictLen):
    key_ = "Day-"+ str(i_) 
    assert testDictSyn[key_][3]== testDictMod[key_][3]           