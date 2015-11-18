# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:40:29 2015

@author: akond
"""
#from Stock import Stock
from Auxiliary import Auxiliary
from Flow import Flow
from StateAll import StateAll
import utility

def executeModelAll(showFlows):

  ##Nine Unique Auxiliaries : Top 
  MultiplierSchedPressure = Auxiliary("MultiplierSchedPressure")
  MultiplierWorkforce = Auxiliary("MultiplierWorkforce")
  NominalErr = Auxiliary("NominalErr")
  SWDevelopmentRate = Auxiliary("SWDevelopmentRate")
  PotErrDetectRate = Auxiliary("PotErrDetectRate")
  QARate = Auxiliary("QARate")
  AvgErrPerTask = Auxiliary("AvgErrPerTask")
  ActualReworkMP = Auxiliary("ActualReworkMP")
  DailyMPRework = Auxiliary("DailyMPRework")


  ## Eight Unique Auxiliaries :Bottom
  TimeToSmooth = Auxiliary("TimeToSmooth")
  MultiplierToRegen = Auxiliary("MultiplierToRegen")
  ActiveErrorDensity = Auxiliary("ActiveErrorDensity")
  TestingRate = Auxiliary("TestingRate")
  PassiveErrorDensity = Auxiliary("PassiveErrorDensity")
  FractionEscapingErrors = Auxiliary("FractionEscapingErrors")
  ActiveErrorsRetiringFraction = Auxiliary("ActiveErrorsRetiringFraction")
  BadFixGenRate = Auxiliary("BadFixGenRate")

  ### Four Flows from Top
  ErrGenRate = Flow("ErrGenRate")
  ErrDetRate = Flow("ErrDetRate")
  ErrEscapeRate = Flow("ErrEscapeRate")
  ReworkRate = Flow("ReworkRate")


  ## Six Flows from Bottom
  ActiveErrorRegenRate = Flow("ActiveErrorRegenRate")
  ActiveErrorDetectAndCorrectRate = Flow("ActiveErrorDetectAndCorrectRate")
  ActiveErrorRetirementRate = Flow("ActiveErrorRetirementRate")
  PassiveErrorDetectAndCorrectRate = Flow("PassiveErrorDetectAndCorrectRate")
  PassiveErrorGenRate = Flow("PassiveErrorGenRate")
  ActiveErrorGenRate = Flow("ActiveErrorGenRate")

  ## we need to fill up auxiliaries ...
  auxDict = utility.createAuxiliaries_All()
  ##States
  curr = StateAll("CurrentState")
  prev = StateAll("PrevState")
  dt = 1
  ##output & test purpose
  stockDict ={}
  for key_,val_ in auxDict.items():
   # current state's stocks are dependent on prev. state's flows
   # some have in and out flows
   curr.PotentiallyDetectableError_.setInput(dt * (prev.ErrGenRate_.curr - prev.ErrDetRate_.curr - prev.ErrEscapeRate_.curr ))
   curr.DetectedError_.setInput( dt*( prev.ErrDetRate_.curr - prev.ReworkRate_.curr  ))

   # some only have in flows from top
   curr.EscapedError_.setInput( dt*(prev.ErrEscapeRate_.curr))
   curr.ReworkedError_.setInput(dt*(prev.ReworkRate_.curr))

   # Update stock from inflows and outflows from Bottom
   curr.UndetectedActiveErrors_.setInput(dt * (prev.ActiveErrorRegenRate_.curr + prev.ActiveErrorGenRate_.curr) - (prev.ActiveErrorRetirementRate_.curr + prev.ActiveErrorDetectAndCorrectRate_.curr) )
   curr.UndetectedPassiveErrors_.setInput(dt * (prev.ActiveErrorRetirementRate_.curr + prev.PassiveErrorGenRate_.curr)- prev.PassiveErrorDetectAndCorrectRate_.curr) 
   
   print "{} ---> {}".format( key_,  curr)
   #setup output
   stockDict[key_]=[curr.PotentiallyDetectableError_.curr, curr.DetectedError_.curr, curr.EscapedError_.curr, curr.ReworkedError_.curr, curr.UndetectedActiveErrors_.curr,curr.UndetectedPassiveErrors_.curr]
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

   #Setting up eight Auxiliaries from Bottom
   TimeToSmooth.setInput(val_[9])
   MultiplierToRegen.setInput(val_[10])
   ActiveErrorDensity.setInput(val_[11])
   TestingRate.setInput(val_[12])
   ActiveErrorsRetiringFraction.setInput(val_[13])
   PassiveErrorDensity.setInput(val_[16] + curr.UndetectedPassiveErrors_.curr)

   #filling flows on the top
   ErrGenRate.fillFlowsByAuxs(MultiplierSchedPressure, MultiplierWorkforce, NominalErr, SWDevelopmentRate)
   ErrDetRate.fillFlowsByAuxs(PotErrDetectRate)
   ErrEscapeRate.fillFlowsByAuxs(AvgErrPerTask, QARate)
   ReworkRate.fillFlowsByAuxs(ActualReworkMP, DailyMPRework)
   
   # updating current state's flows
   curr.updateErrGenRate(ErrGenRate)
   curr.updateErrDetRate(ErrDetRate)
   curr.updateErrEscapeRate(ErrEscapeRate)
   curr.updateReworkRate(ReworkRate)   

   # Connecting top to the bottom 
   # Error Escape Rate -> Fraction Escaping Errors
   # Rework Rate -> Bad Fix Generation Rate   
   FractionEscapingErrors.setInput(val_[14] + ErrEscapeRate.curr) 
   BadFixGenRate.setInput(val_[15] + ReworkRate.curr)
   
   # Filling Flows : six flows from Bottom
   ActiveErrorRegenRate.fillFlowsByAuxs(TimeToSmooth, MultiplierToRegen, ActiveErrorDensity)
   ActiveErrorDetectAndCorrectRate.fillFlowsByAuxs(ActiveErrorDensity)
   ActiveErrorRetirementRate.fillFlowsByAuxs(TestingRate, ActiveErrorsRetiringFraction)
   ActiveErrorGenRate.fillFlowsByAuxs(FractionEscapingErrors, BadFixGenRate)
   PassiveErrorGenRate.fillFlowsByAuxs(BadFixGenRate, FractionEscapingErrors)
   PassiveErrorDetectAndCorrectRate.fillFlowsByAuxs(PassiveErrorDensity, TestingRate)


   # updating current state's flows: six flows from bottom
   curr.updateActiveErrorRegenRate(ActiveErrorRegenRate)
   curr.updateActiveErrorDetectAndCorrectRate(ActiveErrorDetectAndCorrectRate)
   curr.updateActiveErrorRetirementRate(ActiveErrorRetirementRate)
   curr.updateActiveErrorGenRate(ActiveErrorGenRate)
   curr.updatePassiveErrorGenRate(PassiveErrorGenRate)
   curr.updatePassiveErrorDetectAndCorrectRate(PassiveErrorDetectAndCorrectRate)

   if(showFlows):
     print "Printing F-L-O-W-S !"  
     print "key, flow value ---> {}, {}".format(key_, curr.getFlows())      
   ## copying current to prev. 
   prev = curr.copyAll("prev") 
   print "###################"
  return stockDict

def executeModelForDE(auxListParam, currStateParam, prevStateParam, dt):
   ##Nine Unique Auxiliaries : Top 
   MultiplierSchedPressure = Auxiliary("MultiplierSchedPressure")
   MultiplierWorkforce = Auxiliary("MultiplierWorkforce")
   NominalErr = Auxiliary("NominalErr")
   SWDevelopmentRate = Auxiliary("SWDevelopmentRate")
   PotErrDetectRate = Auxiliary("PotErrDetectRate")
   QARate = Auxiliary("QARate")
   AvgErrPerTask = Auxiliary("AvgErrPerTask")
   ActualReworkMP = Auxiliary("ActualReworkMP")
   DailyMPRework = Auxiliary("DailyMPRework")


   ## Eight Unique Auxiliaries :Bottom
   TimeToSmooth = Auxiliary("TimeToSmooth")
   MultiplierToRegen = Auxiliary("MultiplierToRegen")
   ActiveErrorDensity = Auxiliary("ActiveErrorDensity")
   TestingRate = Auxiliary("TestingRate")
   PassiveErrorDensity = Auxiliary("PassiveErrorDensity")
   FractionEscapingErrors = Auxiliary("FractionEscapingErrors")
   ActiveErrorsRetiringFraction = Auxiliary("ActiveErrorsRetiringFraction")
   BadFixGenRate = Auxiliary("BadFixGenRate")

   ### Four Flows from Top
   ErrGenRate = Flow("ErrGenRate")
   ErrDetRate = Flow("ErrDetRate")
   ErrEscapeRate = Flow("ErrEscapeRate")
   ReworkRate = Flow("ReworkRate")


   ## Six Flows from Bottom
   ActiveErrorRegenRate = Flow("ActiveErrorRegenRate")
   ActiveErrorDetectAndCorrectRate = Flow("ActiveErrorDetectAndCorrectRate")
   ActiveErrorRetirementRate = Flow("ActiveErrorRetirementRate")
   PassiveErrorDetectAndCorrectRate = Flow("PassiveErrorDetectAndCorrectRate")
   PassiveErrorGenRate = Flow("PassiveErrorGenRate")
   ActiveErrorGenRate = Flow("ActiveErrorGenRate")    
    
   # current state's stocks are dependent on prev. state's flows
   # some have in and out flows
   currStateParam.PotentiallyDetectableError_.setInput(dt * (prevStateParam.ErrGenRate_.curr - prevStateParam.ErrDetRate_.curr - prevStateParam.ErrEscapeRate_.curr ))
   currStateParam.DetectedError_.setInput( dt*( prevStateParam.ErrDetRate_.curr - prevStateParam.ReworkRate_.curr  ))

   # some only have in flows from top
   currStateParam.EscapedError_.setInput( dt*(prevStateParam.ErrEscapeRate_.curr))
   currStateParam.ReworkedError_.setInput(dt*(prevStateParam.ReworkRate_.curr))

   # Update stock from inflows and outflows from Bottom
   currStateParam.UndetectedActiveErrors_.setInput(dt * (prevStateParam.ActiveErrorRegenRate_.curr + prevStateParam.ActiveErrorGenRate_.curr) - (prevStateParam.ActiveErrorRetirementRate_.curr + prevStateParam.ActiveErrorDetectAndCorrectRate_.curr) )
   currStateParam.UndetectedPassiveErrors_.setInput(dt * (prevStateParam.ActiveErrorRetirementRate_.curr + prevStateParam.PassiveErrorGenRate_.curr)- prevStateParam.PassiveErrorDetectAndCorrectRate_.curr) 
   
   print "---------------"
   #setting up auxiliaries
   MultiplierSchedPressure.setInput(auxListParam[0])
   MultiplierWorkforce.setInput(auxListParam[1])
   NominalErr.setInput(auxListParam[2])
   SWDevelopmentRate.setInput(auxListParam[3])
   PotErrDetectRate.setInput(auxListParam[4])
   AvgErrPerTask.setInput(auxListParam[5])
   QARate.setInput(auxListParam[6])
   ActualReworkMP.setInput(auxListParam[7])
   DailyMPRework.setInput(auxListParam[8])

   #Setting up eight Auxiliaries from Bottom
   TimeToSmooth.setInput(auxListParam[9])
   MultiplierToRegen.setInput(auxListParam[10])
   ActiveErrorDensity.setInput(auxListParam[11])
   TestingRate.setInput(auxListParam[12])
   ActiveErrorsRetiringFraction.setInput(auxListParam[13])
   PassiveErrorDensity.setInput(auxListParam[16] + currStateParam.UndetectedPassiveErrors_.curr)

   #filling flows on the top
   ErrGenRate.fillFlowsByAuxs(MultiplierSchedPressure, MultiplierWorkforce, NominalErr, SWDevelopmentRate)
   ErrDetRate.fillFlowsByAuxs(PotErrDetectRate)
   ErrEscapeRate.fillFlowsByAuxs(AvgErrPerTask, QARate)
   ReworkRate.fillFlowsByAuxs(ActualReworkMP, DailyMPRework)
   
   # updating current state's flows
   currStateParam.updateErrGenRate(ErrGenRate)
   currStateParam.updateErrDetRate(ErrDetRate)
   currStateParam.updateErrEscapeRate(ErrEscapeRate)
   currStateParam.updateReworkRate(ReworkRate)   

   # Connecting top to the bottom 
   # Error Escape Rate -> Fraction Escaping Errors
   # Rework Rate -> Bad Fix Generation Rate   
   FractionEscapingErrors.setInput(auxListParam[14] + ErrEscapeRate.curr) 
   BadFixGenRate.setInput(auxListParam[15] + ReworkRate.curr)
   
   # Filling Flows : six flows from Bottom
   ActiveErrorRegenRate.fillFlowsByAuxs(TimeToSmooth, MultiplierToRegen, ActiveErrorDensity)
   ActiveErrorDetectAndCorrectRate.fillFlowsByAuxs(ActiveErrorDensity)
   ActiveErrorRetirementRate.fillFlowsByAuxs(TestingRate, ActiveErrorsRetiringFraction)
   ActiveErrorGenRate.fillFlowsByAuxs(FractionEscapingErrors, BadFixGenRate)
   PassiveErrorGenRate.fillFlowsByAuxs(BadFixGenRate, FractionEscapingErrors)
   PassiveErrorDetectAndCorrectRate.fillFlowsByAuxs(PassiveErrorDensity, TestingRate)


   # updating current state's flows: six flows from bottom
   currStateParam.updateActiveErrorRegenRate(ActiveErrorRegenRate)
   currStateParam.updateActiveErrorDetectAndCorrectRate(ActiveErrorDetectAndCorrectRate)
   currStateParam.updateActiveErrorRetirementRate(ActiveErrorRetirementRate)
   currStateParam.updateActiveErrorGenRate(ActiveErrorGenRate)
   currStateParam.updatePassiveErrorGenRate(PassiveErrorGenRate)
   currStateParam.updatePassiveErrorDetectAndCorrectRate(PassiveErrorDetectAndCorrectRate)


   ## copying current to prev. 
   prevStateParam = currStateParam.copyAll("prev") 
   print "###################"
   return prevStateParam, currStateParam   
   
   
   
   
def executeModelForBaseline(auxListParam, currStateParam, prevStateParam, dt):
   ##Nine Unique Auxiliaries : Top 
   MultiplierSchedPressure = Auxiliary("MultiplierSchedPressure")
   MultiplierWorkforce = Auxiliary("MultiplierWorkforce")
   NominalErr = Auxiliary("NominalErr")
   SWDevelopmentRate = Auxiliary("SWDevelopmentRate")
   PotErrDetectRate = Auxiliary("PotErrDetectRate")
   QARate = Auxiliary("QARate")
   AvgErrPerTask = Auxiliary("AvgErrPerTask")
   ActualReworkMP = Auxiliary("ActualReworkMP")
   DailyMPRework = Auxiliary("DailyMPRework")


   ## Eight Unique Auxiliaries :Bottom
   TimeToSmooth = Auxiliary("TimeToSmooth")
   MultiplierToRegen = Auxiliary("MultiplierToRegen")
   ActiveErrorDensity = Auxiliary("ActiveErrorDensity")
   TestingRate = Auxiliary("TestingRate")
   PassiveErrorDensity = Auxiliary("PassiveErrorDensity")
   FractionEscapingErrors = Auxiliary("FractionEscapingErrors")
   ActiveErrorsRetiringFraction = Auxiliary("ActiveErrorsRetiringFraction")
   BadFixGenRate = Auxiliary("BadFixGenRate")

   ### Four Flows from Top
   ErrGenRate = Flow("ErrGenRate")
   ErrDetRate = Flow("ErrDetRate")
   ErrEscapeRate = Flow("ErrEscapeRate")
   ReworkRate = Flow("ReworkRate")


   ## Six Flows from Bottom
   ActiveErrorRegenRate = Flow("ActiveErrorRegenRate")
   ActiveErrorDetectAndCorrectRate = Flow("ActiveErrorDetectAndCorrectRate")
   ActiveErrorRetirementRate = Flow("ActiveErrorRetirementRate")
   PassiveErrorDetectAndCorrectRate = Flow("PassiveErrorDetectAndCorrectRate")
   PassiveErrorGenRate = Flow("PassiveErrorGenRate")
   ActiveErrorGenRate = Flow("ActiveErrorGenRate")    
    
   # current state's stocks are dependent on prev. state's flows
   # some have in and out flows
   currStateParam.PotentiallyDetectableError_.setInput(dt * (prevStateParam.ErrGenRate_.curr - prevStateParam.ErrDetRate_.curr - prevStateParam.ErrEscapeRate_.curr ))
   currStateParam.DetectedError_.setInput( dt*( prevStateParam.ErrDetRate_.curr - prevStateParam.ReworkRate_.curr  ))

   # some only have in flows from top
   currStateParam.EscapedError_.setInput( dt*(prevStateParam.ErrEscapeRate_.curr))
   currStateParam.ReworkedError_.setInput(dt*(prevStateParam.ReworkRate_.curr))

   # Update stock from inflows and outflows from Bottom
   currStateParam.UndetectedActiveErrors_.setInput(dt * (prevStateParam.ActiveErrorRegenRate_.curr + prevStateParam.ActiveErrorGenRate_.curr) - (prevStateParam.ActiveErrorRetirementRate_.curr + prevStateParam.ActiveErrorDetectAndCorrectRate_.curr) )
   currStateParam.UndetectedPassiveErrors_.setInput(dt * (prevStateParam.ActiveErrorRetirementRate_.curr + prevStateParam.PassiveErrorGenRate_.curr)- prevStateParam.PassiveErrorDetectAndCorrectRate_.curr) 
   

   #setting up auxiliaries
   MultiplierSchedPressure.setInput(auxListParam[0])
   MultiplierWorkforce.setInput(auxListParam[1])
   NominalErr.setInput(auxListParam[2])
   SWDevelopmentRate.setInput(auxListParam[3])
   PotErrDetectRate.setInput(auxListParam[4])
   AvgErrPerTask.setInput(auxListParam[5])
   QARate.setInput(auxListParam[6])
   ActualReworkMP.setInput(auxListParam[7])
   DailyMPRework.setInput(auxListParam[8])

   #Setting up eight Auxiliaries from Bottom
   TimeToSmooth.setInput(auxListParam[9])
   MultiplierToRegen.setInput(auxListParam[10])
   ActiveErrorDensity.setInput(auxListParam[11])
   TestingRate.setInput(auxListParam[12])
   ActiveErrorsRetiringFraction.setInput(auxListParam[13])
   PassiveErrorDensity.setInput(auxListParam[16] + currStateParam.UndetectedPassiveErrors_.curr)

   #filling flows on the top
   ErrGenRate.fillFlowsByAuxs(MultiplierSchedPressure, MultiplierWorkforce, NominalErr, SWDevelopmentRate)
   ErrDetRate.fillFlowsByAuxs(PotErrDetectRate)
   ErrEscapeRate.fillFlowsByAuxs(AvgErrPerTask, QARate)
   ReworkRate.fillFlowsByAuxs(ActualReworkMP, DailyMPRework)
   
   # updating current state's flows
   currStateParam.updateErrGenRate(ErrGenRate)
   currStateParam.updateErrDetRate(ErrDetRate)
   currStateParam.updateErrEscapeRate(ErrEscapeRate)
   currStateParam.updateReworkRate(ReworkRate)   

   # Connecting top to the bottom 
   # Error Escape Rate -> Fraction Escaping Errors
   # Rework Rate -> Bad Fix Generation Rate   
   FractionEscapingErrors.setInput(auxListParam[14] + ErrEscapeRate.curr) 
   BadFixGenRate.setInput(auxListParam[15] + ReworkRate.curr)
   
   # Filling Flows : six flows from Bottom
   ActiveErrorRegenRate.fillFlowsByAuxs(TimeToSmooth, MultiplierToRegen, ActiveErrorDensity)
   ActiveErrorDetectAndCorrectRate.fillFlowsByAuxs(ActiveErrorDensity)
   ActiveErrorRetirementRate.fillFlowsByAuxs(TestingRate, ActiveErrorsRetiringFraction)
   ActiveErrorGenRate.fillFlowsByAuxs(FractionEscapingErrors, BadFixGenRate)
   PassiveErrorGenRate.fillFlowsByAuxs(BadFixGenRate, FractionEscapingErrors)
   PassiveErrorDetectAndCorrectRate.fillFlowsByAuxs(PassiveErrorDensity, TestingRate)


   # updating current state's flows: six flows from bottom
   currStateParam.updateActiveErrorRegenRate(ActiveErrorRegenRate)
   currStateParam.updateActiveErrorDetectAndCorrectRate(ActiveErrorDetectAndCorrectRate)
   currStateParam.updateActiveErrorRetirementRate(ActiveErrorRetirementRate)
   currStateParam.updateActiveErrorGenRate(ActiveErrorGenRate)
   currStateParam.updatePassiveErrorGenRate(PassiveErrorGenRate)
   currStateParam.updatePassiveErrorDetectAndCorrectRate(PassiveErrorDetectAndCorrectRate)


   ## copying current to prev. 
   prevStateParam = currStateParam.copyAll("prev") 
   return prevStateParam, currStateParam     