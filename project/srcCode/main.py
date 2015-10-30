# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:07:08 2015

@author: akond
"""

#from Diapers import Diapers
#from IntegratedDefectModel import IntegratedDefectModel
#import utility 
from Stock import Stock 
from Auxiliary import Auxiliary
from Flow import Flow 
#utility.printm(Diapers().run())
#print "Auxiliary Model ..."
#utility.printm(IntegratedDefectModel().run())
### Auxiliaries 
print "Auxiliaries ..."
MultiplierSchedPressure = Auxiliary("MultiplierSchedPressure")
print "Before update : ", MultiplierSchedPressure 
MultiplierSchedPressure.setInput(50)
print "After update : ", MultiplierSchedPressure 
MultiplierWorkforce = Auxiliary("MultiplierWorkforce")
print "Before update : ", MultiplierWorkforce 
MultiplierWorkforce.setInput(5)
print "After update : ", MultiplierWorkforce 
NominalErr = Auxiliary("NominalErr")
print "Before update : ", NominalErr 
NominalErr.setInput(15)
print "After update : ", NominalErr 
SWDevelopmentRate = Auxiliary("SWDevelopmentRate")
print "Before update : ", SWDevelopmentRate 
SWDevelopmentRate.setInput(-10)
print "After update : ", SWDevelopmentRate 
PotErrDetectRate = Auxiliary("PotErrDetectRate")
print "Before update: ", PotErrDetectRate 
PotErrDetectRate.setInput(99)
print "After update: ", PotErrDetectRate
QARate = Auxiliary("QARate")
print "Before Update: ", QARate 
QARate.setInput(63) 
print "After Update: ", QARate
AvgErrPerTask = Auxiliary("AvgErrPerTask")
print "Before Update: ", AvgErrPerTask 
AvgErrPerTask.setInput(92) 
print "After Update: ", AvgErrPerTask
ActualReworkMP = Auxiliary("ActualReworkMP")
print "Before Update: ", ActualReworkMP
ActualReworkMP.setInput(123)
print "After Update: ", ActualReworkMP
DailyMPRework = Auxiliary("DailyMPRework")
print "Before Update: ", DailyMPRework
DailyMPRework.setInput(87)
print "After Update: ", DailyMPRework
### Flows 
print "Flows ..."
ErrGenRate = Flow("ErrGenRate")
print "Before update : ", ErrGenRate 
ErrGenRate.setInput(MultiplierSchedPressure.curr)
ErrGenRate.setInput(MultiplierWorkforce.curr)
ErrGenRate.setInput(NominalErr.curr)
ErrGenRate.setInput(SWDevelopmentRate.curr)                           
print "After update : ", ErrGenRate 
ErrDetRate = Flow("ErrDetRate")
print "Before Update: ", ErrDetRate
ErrDetRate.setInput(PotErrDetectRate.curr)
print "After Update: ", ErrDetRate
ErrEscapeRate = Flow("ErrEscapeRate")
print "Before Update: ", ErrEscapeRate
ErrEscapeRate.setInput(AvgErrPerTask.curr)
ErrEscapeRate.setInput(QARate.curr)
print "After Update: ", ErrEscapeRate
ReworkRate = Flow("ReworkRate")
print "Before Update: ", ReworkRate
ReworkRate.setInput(ActualReworkMP.curr)
ReworkRate.setInput(DailyMPRework.curr)
print "After Update: ", ReworkRate
### Stocks 
print "Stocks ..."
print "Stock # 1: "
PotentiallyDetectableError = Stock("PotentiallyDetectableError")
print "Before update : ", PotentiallyDetectableError 
PotentiallyDetectableError.setInput(ErrGenRate.curr)
print "After update : ", PotentiallyDetectableError 
print "Stock # 2: "
EscapedError = Stock("EscapedError")
print "Before update : ", EscapedError 
EscapedError.setInput(ErrEscapeRate.curr)
print "After update : ", EscapedError 
print "Stock # 3: "
DetectedError = Stock("DetectedError")
print "Before update : ", DetectedError 
DetectedError.setInput(ErrDetRate.curr)
print "After update : ", DetectedError 
#def initComponents():
    