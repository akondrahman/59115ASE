# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:50:55 2015

@author: akond
"""

from __future__ import division, print_function
import os, sys, subprocess
from time import sleep
# Get the git root directory
root=repo_dir = subprocess.Popen(['git'
                                      ,'rev-parse'
                                      , '--show-toplevel']
                                      , stdout=subprocess.PIPE
                                    ).communicate()[0].rstrip()
sys.path.append(root)

import numpy as np
from random import uniform

class DTLZ2:
  """
  DTLZ2
  """
  def __init__(i):
    i.n_dec = 30
    i.n_obj = 2

  def generate(i,n):
    return [[uniform(0,1) for _ in xrange(i.n_dec)] for _ in xrange(n)]

  def generateForBaseline(i):
    return [uniform(0,1) for _ in xrange(i.n_dec)]     

  def get_pareto(i):
    rows = []
    with open(root+"/code/problems/dtlz/DTLZ2_3D.csv", "r") as f:
      lines = f.readlines()
      for line in lines:
        rows.append([float(pt) for pt in line.split(",")])
    return rows

  def solve(i,dec):
    k = i.n_dec - i.n_obj + 1
    g =  np.sum([(dec[n] - 0.5)**2 for n in range(i.n_dec-k, i.n_dec)])
    objs = [1 + g] * i.n_obj
    for n in range(i.n_obj):
      for j in range(i.n_obj - n - 1):
        objs[n] *= np.cos(0.5 * np.pi * dec[j])
      if n != 0:
        objs[n] *= np.sin(0.5 * np.pi * dec[i.n_obj - n - 1])
    # sleep(0.5)
    #print("Hello from objs", objs)    
    return objs

if __name__=='__main__':
#  problem = DTLZ2(30,3)
#  row = problem.generate(1)
#  print(problem.solve(row[0]))
  print("Doing baseline ....") 
  theModel = DTLZ2()
  minB = 99999 
  maxB = 0
  for cnt in xrange(int(1e6)):
    vec = theModel.generateForBaseline()
    objs = theModel.solve(vec)    
    sumOfObjs = sum(objs)
    if sumOfObjs > maxB: 
      maxB = sumOfObjs
    if sumOfObjs < minB: 
      minB = sumOfObjs  
  print("Finally the baseline is min={}, max={} ", minB, maxB)    