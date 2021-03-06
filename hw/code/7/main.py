# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:39:44 2015

@author: akond
"""


from __future__ import absolute_import, division
from random import seed
from time import time
#import numpy as np
#from pdb import set_trace
from model import Schaffer, Osyczka2, Kursawe, Golinski
from optimizers import SimulatedAnnealing, MaxWalkSat, DiffEvol




seed(time())
for model in [Kursawe, Osyczka2, Schaffer, Golinski]:
  for optimizer in [MaxWalkSat, SimulatedAnnealing, DiffEvol]:
     print "Optimizer '{}' will now work on Model '{}'".format(optimizer.__name__, model.__name__)
     print "-------------------------------------------------------------------------------------"
     optimizer(model)
     print "-------------------------------------------------------------------------------------"
     print "Optimizer '{}' has finished working  on Model '{}'".format(optimizer.__name__, model.__name__)
     print "-------------------------------------------------------------------------------------"     
     
print("Note-1(a): For MaxWlakSat, '?' means *mutated solution* is better than *best solution* ")
print("Note-1(b): For MaxWlakSat, '+' means *old solution* is better than *mutated solution* ")        
print("Note-1(c): For MaxWlakSat, '!' means *mutated solution* is better than *old solution* ")          
 