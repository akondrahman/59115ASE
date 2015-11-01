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
from State import State
import utility 
#utility.printm(Diapers().run())
#print "Auxiliary Model ..."
#utility.printm(IntegratedDefectModel().run())
### Auxiliaries 
#print "Auxiliaries ..."
#print "-----\t A1 \t-----"
MultiplierSchedPressure = Auxiliary("MultiplierSchedPressure")
#print "Before update : ", MultiplierSchedPressure 
#MultiplierSchedPressure.setInput(50)
#print "After update : ", MultiplierSchedPressure 
#print "-----\t A2 \t-----"
MultiplierWorkforce = Auxiliary("MultiplierWorkforce")
#print "Before update : ", MultiplierWorkforce 
#MultiplierWorkforce.setInput(5)
#print "After update : ", MultiplierWorkforce 
#print "-----\t A3 \t-----"
NominalErr = Auxiliary("NominalErr")
#print "Before update : ", NominalErr 
NominalErr.setInput(15)
#print "After update : ", NominalErr 
#print "-----\t A4 \t-----" 
SWDevelopmentRate = Auxiliary("SWDevelopmentRate")
#print "Before update : ", SWDevelopmentRate 
#SWDevelopmentRate.setInput(-10)
#print "After update : ", SWDevelopmentRate 
#print "-----\t A5 \t-----"
PotErrDetectRate = Auxiliary("PotErrDetectRate")
#print "Before update: ", PotErrDetectRate 
#PotErrDetectRate.setInput(99)
#print "After update: ", PotErrDetectRate
QARate = Auxiliary("QARate")
#print "-----\t A6 \t-----"
#print "Before Update: ", QARate 
#QARate.setInput(63) 
#print "After Update: ", QARate
AvgErrPerTask = Auxiliary("AvgErrPerTask")
#print "-----\t A7 \t-----"
#print "Before Update: ", AvgErrPerTask 
#AvgErrPerTask.setInput(92) 
#print "After Update: ", AvgErrPerTask
#print "-----\t A8 \t-----"
ActualReworkMP = Auxiliary("ActualReworkMP")
#print "Before Update: ", ActualReworkMP
#ActualReworkMP.setInput(123)
#print "After Update: ", ActualReworkMP
#print "-----\t A9 \t-----"
DailyMPRework = Auxiliary("DailyMPRework")
#print "Before Update: ", DailyMPRework
#DailyMPRework.setInput(87)
#print "After Update: ", DailyMPRework
### Flows 
#print "Flows ..."
#print "-----\t F1 \t-----"
ErrGenRate = Flow("ErrGenRate")
#print "Before update : ", ErrGenRate 
#ErrGenRate.setInput(MultiplierSchedPressure.curr)
#ErrGenRate.setInput(MultiplierWorkforce.curr)
#ErrGenRate.setInput(NominalErr.curr)
#ErrGenRate.setInput(SWDevelopmentRate.curr)                           
#print "After update : ", ErrGenRate 
#print "-----\t F2 \t-----"
ErrDetRate = Flow("ErrDetRate")
#print "Before Update: ", ErrDetRate
#ErrDetRate.setInput(PotErrDetectRate.curr)
#print "After Update: ", ErrDetRate
#print "-----\t F3 \t-----"
ErrEscapeRate = Flow("ErrEscapeRate")
#print "Before Update: ", ErrEscapeRate
#ErrEscapeRate.setInput(AvgErrPerTask.curr)
#ErrEscapeRate.setInput(QARate.curr)
#print "After Update: ", ErrEscapeRate 
#print "-----\t F4 \t-----"
ReworkRate = Flow("ReworkRate")
#print "Before Update: ", ReworkRate
#ReworkRate.setInput(ActualReworkMP.curr)
#ReworkRate.setInput(DailyMPRework.curr)
#print "After Update: ", ReworkRate
### Stocks 
#print "Stocks ..."
#print "Stock # 1: "
PotentiallyDetectableError = Stock("PotentiallyDetectableError")
#print "Before update : ", PotentiallyDetectableError 
#PotentiallyDetectableError.setInput(ErrGenRate.curr)
#print "After update : ", PotentiallyDetectableError 
#print "Stock # 2: "
EscapedError = Stock("EscapedError")
#print "Before update : ", EscapedError 
#EscapedError.setInput(ErrEscapeRate.curr)
#print "After update : ", EscapedError 
#print "Stock # 3: "
DetectedError = Stock("DetectedError")
#print "Before update : ", DetectedError 
#DetectedError.setInput(ErrDetRate.curr)
#print "After update : ", DetectedError 
#print "Stock # 4: "
ReworkedError = Stock("ReworkedError")
#print "Before update : ", ReworkedError 
#ReworkedError.setInput(ReworkRate.curr)
#print "After update : ", ReworkedError 
#def initComponents():
###State 
## get the auxiliairies 
auxList = [MultiplierSchedPressure, MultiplierWorkforce, NominalErr, SWDevelopmentRate] 
auxDict = utility.createAuxiliaries(len(auxList))
#print auxDict
curr = State("CurrentState")
prev = State("PrevState")
dt = 1
for key_,val_ in auxDict.items():
 # current state's stocks are dependent on prev. state's flows    
 # some have in and out flows  
 curr.PotentiallyDetectableError_.setInput(dt * (prev.ErrGenRate_.curr - prev.ErrDetRate_.curr - prev.ErrEscapeRate_.curr ))
 curr.DetectedError_.setInput( dt*( ErrDetRate.curr - ReworkRate.curr  ))
 # some only ahve in flows  
 curr.EscapedError_.setInput( dt*(ErrEscapeRate.curr))
 curr.ReworkedError_.setInput(dt*(ReworkRate.curr))
 print "{} ---> {}".format( key_,  curr)   
 print "---------------" 
 #setting up auxiliaries 
 MultiplierSchedPressure.setInput(val_[0])   
 MultiplierWorkforce.setInput(val_[1])   
 NominalErr.setInput(val_[2])
 SWDevelopmentRate.setInput(val_[3]) 
 PotErrDetectRate.setInput(val_[4])
 AvgErrPerTask.setInput(val_[5])
 QARate.setInput(val_[6])
 ActualReworkMP.setInput(val_[7])
 DailyMPRework.setInput(val_[8])
 #fillign flows 
 ErrGenRate.fillFlowsByAuxs(MultiplierSchedPressure, MultiplierWorkforce, NominalErr, SWDevelopmentRate)
 ErrDetRate.fillFlowsByAuxs(PotErrDetectRate)
 ErrEscapeRate.fillFlowsByAuxs(AvgErrPerTask, QARate)
 ReworkRate.fillFlowsByAuxs(ActualReworkMP, DailyMPRework)
 # updating current state's flows  
 curr.updateErrGenRate(ErrGenRate)
 curr.updateErrDetRate(ErrDetRate)
 curr.updateErrEscapeRate(ErrEscapeRate) 
 curr.updateReworkRate(ReworkRate)
 print "{} ---> {}".format( key_,  curr.getFlows())    
 print "---------------"  
 prev = curr.copy("Prev") 

  
 #print "Prev: ZZZ ",prev_ 
 # MultiplierSchedPressure.setInput(0)   
 # MultiplierWorkforce.setInput(0)   
 # NominalErr.setInput(0)
 # SWDevelopmentRate.setInput(0)  
 # ErrGenRate.fillFlowsByAuxs(MultiplierSchedPressure, MultiplierWorkforce, NominalErr, SWDevelopmentRate) 
 
 #ErrGenRate.resetInput()
 #ErrDetRate.resetInput()
 #ErrEscapeRate.resetInput()
 #print "Prev summary ... "
 #prevStr = key_ + "----ErrGen" + str(prev.ErrGenRate_.curr) + "-ErrDet" + str(prev.ErrDetRate_.curr) + "-Erresc" +str(prev.ErrEscapeRate_.curr) 
 #print prevStr  
 print "###################"
#ErrDetRate.fillFlowsByAuxs(PotErrDetectRate)
#ErrEscapeRate.fillFlowsByAuxs()

#flowList =[ErrGenRate, ErrDetRate, ErrEscapeRate]
#stockList = [PotentiallyDetectableError ]

#print curr_  

#print "auxiliaries: ", auxDict 


