# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:21:32 2015

@author: akond
"""



def getRandVal():
  import random 
  maxRange=100000
  minRange=-100000
  randToret = 0 
  randToret = random.randrange(minRange, maxRange)
  return randToret



def getProbOfAcceptance(currEnergyP, neighbourEnergyP, tParam):
  # t = k/kmax
  import math
  equation = float(1*(currEnergyP-neighbourEnergyP)/float(tParam))
  accepProbToret = math.exp(equation)
  return accepProbToret




def getRandomProb():
   import random 
   return random.random()       