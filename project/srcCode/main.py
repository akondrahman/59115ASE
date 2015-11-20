# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:07:08 2015

@author: akond
"""



from models import IntegratedDefectModel
import tests, ModelExecAll, integrator, utility, IO_Utility 
########### Obsolete ########
#def execBottom(showFlows):
#  print "############# BOTTOM #########"
#  # print "Executing test cases for bottom ... no fail means passing !"
#  # tests.testBottom(showFlows)
#  print "Executing the 'bottom' part of the model ... "
#  ModelExec.executeModelBottom(showFlows)
#
#
#    
#def execTop(showFlows):
#  print "############# TOP #########"
#  print "Executing test cases for top ... no fail means passing !"
#  tests.testTop(showFlows)
#  print "Executing the 'top' part of the model ... "
#  ModelExec.executeModelTop(showFlows) 


def execAll(showFlows):

  print "############# ALL #########"
  print "Executing test cases for whole model ... no fail means passing !"
  tests.testAll(showFlows)
  print "Executing the 'ALL' part of the model ... "
  ModelExecAll.executeModelAll(showFlows) 



def runIntegrator():
  print "############# Dummy Integration #########"
  print "Executing test cases for whole model with dummy integration ... no fail means passing !"
  tests.testDummyIntegration()
  
def getBaselineForModel(cntParam, dirToWriteP, fileNameToWriteP, constFlagForBaselineP):
  print "Getting baseline for {} times".format(cntParam) 
  baselineDict = integrator.runModelForBaseline(cntParam, constFlagForBaselineP)  
  print "Writing dictionary to file ... ",   IO_Utility.writeDictToFile(dirToWriteP, fileNameToWriteP, baselineDict)
  minOfBaseline_ = utility.getFeatureFromDict(baselineDict,  "min") 
  maxOfBaseline_ = utility.getFeatureFromDict(baselineDict,  "max")  

  return minOfBaseline_, maxOfBaseline_
  
def createConstraintFile(dirP, fileP): 
  auxNames= utility.getAuxNameList()     
  lowerRange = utility.createAuxList()[0]
  upperRange = utility.createAuxList()[1]
  IO_Utility.createConstraintFiles(dirP, fileP, auxNames, lowerRange, upperRange)
  return "Created  file " + fileP  

showFlows=False
#execAll(showFlows)
#runIntegrator()
runCount = 365
constFlagForBaseline = False
deRunCount=100
dirToWriteP="/Users/akond/Documents/Fall_2015/ase/59115ASE/project/supplementary/"
constraintFileNameParam= dirToWriteP +  "0_1_constraints.csv"
# gettting baseline 

fileNameToWriteP = "baseline_" + str(runCount)
#print createConstraintFile(dirToWriteP, constraintFileNameParam)
minB, maxB = getBaselineForModel(runCount, dirToWriteP, fileNameToWriteP, constFlagForBaseline)
print "And the baseline is (min, max format) \n", minB, maxB


print "Executing D.E (minimized version) ... for {} D.E. runs and {} model runs".format(deRunCount, runCount)
print "================================================"
with  utility.duration(): 
  integrator.runDE(minB, maxB, IntegratedDefectModel, deRunCount, runCount, constraintFileNameParam)

   