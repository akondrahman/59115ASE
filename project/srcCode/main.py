# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:07:08 2015

@author: akond
"""



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
  
def getBaselineForModel(cntParam, dirToWriteP, fileNameToWriteP):
  print "Getting baseline for {} times".format(cntParam) 
  baselineDict = integrator.runModelForBaseline(cntParam)  
  print "Writing dictionary to file ... ",   IO_Utility.writeDictToFile(dirToWriteP, fileNameToWriteP, baselineDict)
  minOfBaseline_uae = utility.getFeatureFromDict(baselineDict, 0, "min") 
  maxOfBaseline_uae = utility.getFeatureFromDict(baselineDict, 0, "max")  
  minOfBaseline_upe = utility.getFeatureFromDict(baselineDict, 1, "min")  
  maxOfBaseline_upe = utility.getFeatureFromDict(baselineDict, 1, "max")   
  return minOfBaseline_uae, maxOfBaseline_uae, minOfBaseline_upe, maxOfBaseline_upe

showFlows=False
#execAll(showFlows)
#runIntegrator()
runCount = 1000000
dirToWriteP="/Users/akond/Documents/Fall_2015/ase/59115ASE/project/supplementary/"
fileNameToWriteP = "baseline_" + str(runCount)
print "And the baseline is (min, max format, UAE first) \n", getBaselineForModel(runCount, dirToWriteP, fileNameToWriteP)

   