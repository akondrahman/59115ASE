# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:14:39 2015

@author: akond
"""
from Uber import Uber
class Model:
  def state(i):
    """To create a state vector, we create 
    one slot for each name in 'have'."""
    tmp=i.have()
    for k,v in tmp.has().items():
      v.name = k
    return tmp 
  def run(i,dt=1,tmax=30):
    """For time up to 'tmax', increment 't' 
       by 'dt' and 'step' the model."""
    t,b4 = 0, Uber()
    keep = []    ## 1
    state = i.state()
    for k,a in state.items(): 
      b4[k] = a.init
    keys  = sorted(state.keys(),  ## 3
                   key=lambda z: state[z].rank())
    keep = [["t"] +  keys,
            [0] + b4.asList(keys)]
    while t < tmax:
      now = b4.copy()
      i.step(dt,t,b4,now)
      for k in state.keys(): 
        now[k] = state[k].restrain(now[k]) ## 4
      keep += [[t] + now.asList(keys)] ## 2
      t += dt
      b4 = now
    return keep