# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:40:29 2015

@author: akond
"""



def executeModel():
  #from Stock import Stock 
  from Auxiliary import Auxiliary
  from Flow import Flow 
  from State import State
  import utility 
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
  auxDict = utility.createAuxiliaries()
  ##States
  curr = State("CurrentState")
  prev = State("PrevState")
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
   print "###################"
  return stockDict 