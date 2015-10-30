# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:02:08 2015

@author: akond
"""
#import random
#r   = random.random
#isa = isinstance
from Model import Model
from Uber import Uber
from Has import Stock, Aux, Flow 
S,A,F = Stock,Aux,Flow
class Diapers(Model):
  def have(i):
    return Uber(C = S(100), D = S(0),
             q = F(0),  r = F(8), s = F(0))
  def step(i,dt,t,u,v):
    def saturday(x): return int(x) % 7 == 6
    v.C +=  dt*(u.q - u.r)
    v.D +=  dt*(u.r - u.s)
    v.q  =  70  if saturday(t) else 0 
    v.s  =  u.D if saturday(t) else 0
    if t == 27: # special case (the day i forget)
      v.s = 0
