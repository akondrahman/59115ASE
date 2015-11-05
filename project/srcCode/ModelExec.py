# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:40:29 2015

@author: akond
"""
#from Stock import Stock
from Auxiliary import Auxiliary
from Flow import Flow
from State import State
import utility

def executeModelTop(showFlows):

  ##Auxiliaries
  MultiplierSchedPressure = Auxiliary("MultiplierSchedPressure")
  MultiplierWorkforce = Auxiliary("MultiplierWorkforce")
  NominalErr = Auxiliary("NominalErr")
  SWDevelopmentRate = Auxiliary("SWDevelopmentRate")
  PotErrDetectRate = Auxiliary("PotErrDetectRate")
  QARate = Auxiliary("QARate")
  AvgErrPerTask = Auxiliary("AvgErrPerTask")
  ActualReworkMP = Auxiliary("ActualReworkMP")
  DailyMPRework = Auxiliary("DailyMPRework")
  ### Flows
  ErrGenRate = Flow("ErrGenRate")
  ErrDetRate = Flow("ErrDetRate")
  ErrEscapeRate = Flow("ErrEscapeRate")
  ReworkRate = Flow("ReworkRate")

  ## we need to fill up auxiliaries ...
  auxDict = utility.createAuxiliaries_Top()
  ##States
  curr = State("CurrentState", True)
  prev = State("PrevState", True)
  dt = 1
  ##output & test purpose
  stockDict ={}
  for key_,val_ in auxDict.items():
   # current state's stocks are dependent on prev. state's flows
   # some have in and out flows
   curr.PotentiallyDetectableError_.setInput(dt * (prev.ErrGenRate_.curr - prev.ErrDetRate_.curr - prev.ErrEscapeRate_.curr ))
   curr.DetectedError_.setInput( dt*( ErrDetRate.curr - ReworkRate.curr  ))
   # some only have in flows
   curr.EscapedError_.setInput( dt*(ErrEscapeRate.curr))
   curr.ReworkedError_.setInput(dt*(ReworkRate.curr))
   print "{} ---> {}".format( key_,  curr)
   #setup output
   stockDict[key_]=[curr.PotentiallyDetectableError_.curr, curr.DetectedError_.curr, curr.EscapedError_.curr, curr.ReworkedError_.curr]
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
   #filling flows
   ErrGenRate.fillFlowsByAuxs(MultiplierSchedPressure, MultiplierWorkforce, NominalErr, SWDevelopmentRate)
   ErrDetRate.fillFlowsByAuxs(PotErrDetectRate)
   ErrEscapeRate.fillFlowsByAuxs(AvgErrPerTask, QARate)
   ReworkRate.fillFlowsByAuxs(ActualReworkMP, DailyMPRework)
   # updating current state's flows
   curr.updateErrGenRate(ErrGenRate)
   curr.updateErrDetRate(ErrDetRate)
   curr.updateErrEscapeRate(ErrEscapeRate)
   curr.updateReworkRate(ReworkRate)
   if(showFlows):
    print "{} ---> {}".format( key_,  curr.getFlows())
    print "---------------"
   prev = curr.copyTop("Prev")
   #print "Prev: ZZZ ",prev_
   print "###################"
  return stockDict


def executeModelBottom(showFlows):

  ## Auxiliaries
  TimeToSmooth = Auxiliary("TimeToSmooth")
  MultiplierToRegen = Auxiliary("MultiplierToRegen")
  ActiveErrorDensity = Auxiliary("ActiveErrorDensity")
  TestingRate = Auxiliary("TestingRate")
  PassiveErrorDensity = Auxiliary("PassiveErrorDensity")
  FractionEscapingErrors = Auxiliary("FractionEscapingErrors")
  ActiveErrorsRetiringFraction = Auxiliary("ActiveErrorsRetiringFraction")
  BadFixGenRate = Auxiliary("BadFixGenRate")

  ## Flows
  ActiveErrorRegenRate = Flow("ActiveErrorRegenRate")
  ActiveErrorDetectAndCorrectRate = Flow("ActiveErrorDetectAndCorrectRate")
  ActiveErrorRetirementRate = Flow("ActiveErrorRetirementRate")
  PassiveErrorDetectionRate = Flow("PassiveErrorDetectionRate")
  PassiveErrorGenRate = Flow("PassiveErrorGenRate")
  ActiveErrorGenRate = Flow("ActiveErrorGenRate")

  auxDict = utility.createAuxiliaries_Bottom()

  ##States
  curr = State("CurrentState", False)
  prev = State("PrevState", False)
  dt = 1
  ##output & test purpose
  stockDict ={}


  for key_, val_ in auxDict.items():

    # Update stock from inflows and outflows
    curr.UndetectedActiveErrors_.setInput(dt * (prev.ActiveErrorRegenRate_.curr + prev.ActiveErrorGenRate_.curr) - (prev.ActiveErrorRetirementRate_.curr + prev.ActiveErrorDetectAndCorrectRate_.curr) )
    print "{} ---> {}".format( key_,  curr)

    stockDict[key_]=[curr.UndetectedActiveErrors_.curr]
    print "---------------"

    #Setting up Auxiliaries
    TimeToSmooth.setInput(val_[0])
    MultiplierToRegen.setInput(val_[1])
    ActiveErrorDensity.setInput(val_[2])
    TestingRate.setInput(val_[3])
    ActiveErrorsRetiringFraction.setInput(val_[4])
    FractionEscapingErrors.setInput(val_[5])
    BadFixGenRate.setInput(val_[6])

    # Filling Flows
    ActiveErrorRegenRate.fillFlowsByAuxs(TimeToSmooth, MultiplierToRegen, ActiveErrorDensity)
    ActiveErrorDetectAndCorrectRate.fillFlowsByAuxs(ActiveErrorDensity)
    ActiveErrorRetirementRate.fillFlowsByAuxs(TestingRate, ActiveErrorsRetiringFraction)
    ActiveErrorGenRate.fillFlowsByAuxs(FractionEscapingErrors, BadFixGenRate)

    # updating current state's flows
    curr.updateActiveErrorRegenRate(ActiveErrorRegenRate)
    curr.updateActiveErrorDetectAndCorrectRate(ActiveErrorDetectAndCorrectRate)
    curr.updateActiveErrorRetirementRate(ActiveErrorRetirementRate)
    curr.updateActiveErrorGenRate(ActiveErrorGenRate)
    if(showFlows):
      print "{} ---> {}".format( key_,  curr.getFlows())
      print "---------------"
    prev = curr.copyBottom("Prev")
    #print "Prev: ZZZ ",prev_
    print "###################"
  return stockDict








