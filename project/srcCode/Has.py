# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:23:31 2015

@author: akond
"""



class Has:
  def __init__(i,init,lo=0,hi=100):
    i.init,i.lo,i.hi = init,lo,hi
  def restrain(i,x):
    return max(i.lo, 
               min(i.hi, x))
  def rank(i): 
    "Trick to sort together columns of the same type."
    return 0
  def __repr__(i):
    return str(dict(what=i.__class__.__name__,
                name= i.name,init= i.init,
                 lo  = i.lo,  hi  = i.hi))
                 
class Flow(Has) :
  def rank(i): return 3
class Stock(Has):
  def rank(i): return 1
class Aux(Has)  :
  def rank(i): return 2