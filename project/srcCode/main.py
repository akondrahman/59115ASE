# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:07:08 2015

@author: akond
"""



import tests, ModelExecAll
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

showFlows=False
#execAll(showFlows)
runIntegrator()

   