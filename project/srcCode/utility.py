# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:12:10 2015

@author: akond
"""

def printm(matrix,less=True):
   """Print a list of list, only showing changes
   in each column (if less is True)."""
   def ditto(m,mark="."):
     def worker(lst):
       out = []
       for i,now in enumerate(lst):
         before = old.get(i,None) # get old it if exists
         out += [mark if before == now else now]
         old[i] = now # next time, 'now' is the 'old' value
       return out # the lst with ditto marks inserted
     old = {}
     return [worker(row) for row in m]
   matrix = ditto(matrix) if less else matrix
   s = [[str(e) for e in row] for row in matrix]
   lens = [max(map(len, col)) for col in zip(*s)]
   fmt = ' | '.join('{{:{}}}'.format(x) for x in lens)
   for row in [fmt.format(*row) for row in s]:
      print(row)