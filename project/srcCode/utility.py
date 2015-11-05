# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:44:38 2015

@author: akond
"""



def createAuxiliaries():
  dict_={}
  dict_['Day-0'] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  dict_['Day-1'] = [1, 1, 1, 1, 1, 1, 1, 15, 1]
  dict_['Day-2'] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
  dict_['Day-3'] = [2, 2, 2, 2, 2, 2, 2, 2, 2]
  dict_['Day-4'] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
  dict_['Day-5'] = [10, 10, 10, 10, 10, 10, 10, 10, 10]
  dict_['Day-6'] = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
  return dict_


def createAuxiliariesBottom():
  dict_={}
  dict_['Day-0'] = [0, 0, 0, 0, 0, 0, 0]
  dict_['Day-1'] = [1, 1, 1, 1, 1, 1, 1]
  dict_['Day-2'] = [1, 1, 1, 1, 1, 1, 1]
  dict_['Day-3'] = [2, 2, 2, 2, 2, 2, 2]
  dict_['Day-4'] = [1, 1, 1, 1, 1, 1, 1]
  dict_['Day-5'] = [10, 10, 10, 10, 10, 10, 10]
  dict_['Day-6'] = [-1, -1, -1, -1, -1, -1, -1]
  return dict_


def createTestStock():
  dict_={}
  dict_['Day-0'] = [0, 0, 0, 0]
  dict_['Day-1'] = [0, 0, 0, 0]
  dict_['Day-2'] = [1, -15, 2, 16]
  dict_['Day-3'] = [2, -16, 4, 18]
  dict_['Day-4'] = [4, -18, 8, 22]
  dict_['Day-5'] = [5, -19, 10, 24]
  dict_['Day-6'] = [15, -29, 30, 44]
  return dict_

