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
# from optimizers import de
from optimizers import *
from utilities import compute_loss, rdivDemo

scottknott_list = {}

baselineDict={}
def runOptimizer(optimizerNameP, modelNameP, runP):
 loss_list = []
 for i in xrange(runP):
   seed(i)
   #baselineDict[str(i)] = [ random.uniform(0,1), BaseLine.baseline_min, BaseLine.baseline_max]
   print "Optimizer '{}' will now work on Model '{}'".format(optimizerNameP.__name__, modelNameP.__name__)
   print "-------------------------------------------------------------------------------------"

   bestSol, eraDict = optimizerNameP(modelNameP)
   first_era = eraDict[1]
   last_era = eraDict[len(eraDict)]
   total_loss = compute_loss(first_era, last_era)
   loss_list.append(total_loss)

   print "-------------------------------------------------------------------------------------"
   print "Optimizer '{}' has finished working  on Model '{}'".format(optimizerNameP.__name__, modelNameP.__name__)
   print "-------------------------------------------------------------------------------------"

 return loss_list

runs=20
#modelList=[Schaffer]

for model in [dtlz7]:
       scottknott_list["SimulatedAnnealing"] = runOptimizer(SimulatedAnnealing, model, runs)
       scottknott_list["MaxWalkSat"] = runOptimizer(MaxWalkSat, model, runs)
       # runOptimizer(de, model, runs)

all_loss = []
for key, item in scottknott_list.items():
  item.insert(0,key)
  all_loss.append(item)

rdivDemo(all_loss)


#print("Note-1(a): For MaxWlakSat, '?' means *mutated solution* is better than *best solution* ")
#print("Note-1(b): For MaxWlakSat, '!' means *old solution* is better than *mutated solution* ")
#print("Note-1(c): For MaxWlakSat, '+' means *mutated solution* is better than *old solution* ")

