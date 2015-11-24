# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:39:44 2015

@author: akond
"""


from __future__ import absolute_import, division
from random import seed
from time import time
import random 
#import numpy as np
#from pdb import set_trace
from model import  dtlz7, BaseLine, Schaffer
from optimizers import SimulatedAnnealing, MaxWalkSat 



baselineDict={}
def runOptimizer(optimizerNameP, modelNameP, runP):
 for i in xrange(runP):
   seed(i)    
   #baselineDict[str(i)] = [ random.uniform(0,1), BaseLine.baseline_min, BaseLine.baseline_max]      
   print "Optimizer '{}' will now work on Model '{}'".format(optimizerNameP.__name__, modelNameP.__name__)
   print "-------------------------------------------------------------------------------------"

   optimizerNameP(modelNameP)

   print "-------------------------------------------------------------------------------------"
   print "Optimizer '{}' has finished working  on Model '{}'".format(optimizerNameP.__name__, modelNameP.__name__)
   print "-------------------------------------------------------------------------------------"

runs=20
#modelList=[Schaffer]

for model in [dtlz7]:
       runOptimizer(SimulatedAnnealing, model, runs) 
       runOptimizer(MaxWalkSat, model, runs) 


#print("Note-1(a): For MaxWlakSat, '?' means *mutated solution* is better than *best solution* ")
#print("Note-1(b): For MaxWlakSat, '!' means *old solution* is better than *mutated solution* ")        
#print("Note-1(c): For MaxWlakSat, '+' means *mutated solution* is better than *old solution* ")          
 