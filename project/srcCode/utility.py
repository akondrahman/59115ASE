# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:44:38 2015

@author: akond
"""


########## Top Part Obsolete#############
#def createAuxiliaries_Top():
#  dict_={}
#  dict_['Day-0'] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#  dict_['Day-1'] = [1, 1, 1, 1, 1, 1, 1, 15, 1]
#  dict_['Day-2'] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
#  dict_['Day-3'] = [2, 2, 2, 2, 2, 2, 2, 2, 2]
#  dict_['Day-4'] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
#  dict_['Day-5'] = [10, 10, 10, 10, 10, 10, 10, 10, 10]
#  dict_['Day-6'] = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
#  return dict_
#
#
#
#
#
#
#
#def createTestStock_Top():
#  dict_={}
#  dict_['Day-0'] = [0, 0, 0, 0]
#  dict_['Day-1'] = [0, 0, 0, 0]
#  dict_['Day-2'] = [1, -15, 2, 16]
#  dict_['Day-3'] = [2, -16, 4, 18]
#  dict_['Day-4'] = [4, -18, 8, 22]
#  dict_['Day-5'] = [5, -19, 10, 24]
#  dict_['Day-6'] = [15, -29, 30, 44]
#  return dict_
#
#
#
########### Bottom Part #############
#def createTestStock_Bottom():
#  dict_={}
#  dict_['Day-0'] = [0]
#  dict_['Day-1'] = [0]
#  dict_['Day-2'] = [2]
#  dict_['Day-3'] = [4]
#  dict_['Day-4'] = [8]
#  dict_['Day-5'] = [10]
#  dict_['Day-6'] = [30]
#  return dict_
#  
#  
#def createAuxiliaries_Bottom():
#  dict_={}
#  dict_['Day-0'] = [0, 0, 0, 0, 0, 0, 0,0]
#  dict_['Day-1'] = [1, 1, 1, 1, 1, 1, 1,1]
#  dict_['Day-2'] = [1, 1, 1, 1, 1, 1, 1,1]
#  dict_['Day-3'] = [2, 2, 2, 2, 2, 2, 2,2]
#  dict_['Day-4'] = [1, 1, 1, 1, 1, 1, 1,1]
#  dict_['Day-5'] = [10, 10, 10, 10, 10, 10, 10,10]
#  dict_['Day-6'] = [-1, -1, -1, -1, -1, -1, -1,-1]
#  return dict_


########### ALL ##########  
def createAuxiliaries_All():
  dict_={}
  dict_['Day-0'] = [0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0]
  dict_['Day-1'] = [1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1]
  dict_['Day-2'] = [1, 1, 1, 1, 1, 1, 1,1,1, 1, 1, 1, 1, 1, 1,1,1]
  dict_['Day-3'] = [2, 2, 2, 2, 2, 2, 2,2,2, 2, 2, 2, 2, 2, 2,2,2]
  dict_['Day-4'] = [1, 1, 1, 1, 1, 1, 1,1,1, 1, 1, 1, 1, 1, 1,1,1]
  dict_['Day-5'] = [10, 10, 10, 10, 10, 10, 10,10,10, 10, 10, 10, 10, 10, 10,10,10]
  dict_['Day-6'] = [-1, -1, -1, -1, -1, -1, -1,-1,-1, -1, -1, -1, -1, -1, -1,-1,-1]
  return dict_  
  



def createTestStock_All():
  dict_={}
  dict_['Day-0'] = [0, 0, 0, 0, 0, 0]
  dict_['Day-1'] = [0, 0, 0, 0, 0, 0]
  dict_['Day-2'] = [1, 2, -1, 2, 6, 6]
  dict_['Day-3'] = [2, 4, -2, 4, 12, 6]
  dict_['Day-4'] = [4, 8, -4, 8, 24, 12]
  dict_['Day-5'] = [5, 10, -5, 10, 30, 6]
  dict_['Day-6'] = [15, 30, -15, 30, 90, 60]
  return dict_
  