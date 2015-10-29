# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:06:57 2015

@author: akond
"""
from Model import Model
from Uber import Uber
from Has import Stock, Aux, Flow 
S,A,F = Stock,Aux,Flow
class IntegratedDefectModel(Model):
  def have(i):
    return Uber(ReworkedErrors = S(0), 
                DetectedErrors = S(0), 
                ReworkRate = F(5), 
                activeReWorkNeededPerError = A(8), 
                dailyMPForRework = A(0), 
                PotErrorDetectionRate = F(10), 
                ErrorDetectionRate = F(25), 
                PotDetectableError = S(0), 
                SWDevelopmentRate = A(50),
                NominalError = A(5),
                MultiplierDueToWorkforce = A(10), 
                MultiplierDueToSchedPressure = A(50), 
                ErrorGenerationRate = F(0) )

  def step(i,dt,t,u,v):
    weirdChange = lambda x : int(x) % 7 == 6  
    #def saturday(x): return int(x) % 7 == 6
    # Reworked Errors Part
    v.ReworkedErrors +=  dt*( u.ReworkRate  +  u.activeReWorkNeededPerError + u.dailyMPForRework)
    # Detected Errors Part    
    v.DetectedErrors  +=  dt*(u.ErrorDetectionRate + u.PotErrorDetectionRate - u.ReworkRate) 
    # Potentially Detectable Error 
    v.PotDetectableError += dt* ( u.SWDevelopmentRate + u.NominalError 
                                  + u.MultiplierDueToWorkforce + u.MultiplierDueToSchedPressure
                                  - v.ErrorDetectionRate
                                )
    # the following are dummy values ... needs change 
    v.detectedError  =  5  if weirdChange(t) else 0     
    v.activeReWorkNeededPerError  =  10  if weirdChange(t) else 0 
    v.dailyMPForRework  =  50 if weirdChange(t) else 0
    v.ReworkRate  =  -10 if weirdChange(t) else 0
    # potantially detectable error 


      
      
#class ReworkedErrors(Model):
#  def have(i):
#    return Uber(C = S(100), D = S(0),
#             q = F(0),  r = F(8), s = F(0))
#  def step(i,dt,t,u,v):
#    def saturday(x): return int(x) % 7 == 6
#    v.C +=  dt*(u.q - u.r)
#    v.D +=  dt*(u.r - u.s)
#    v.q  =  70  if saturday(t) else 0 
#    v.s  =  u.D if saturday(t) else 0
#    if t == 27: # special case (the day i forget)
#      v.s = 0      