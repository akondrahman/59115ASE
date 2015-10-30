# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:18:44 2015

@author: akond
"""

class Uber:
  """Emulate Javascript's uber simple objects.
  Note my convention: I use "`i`" not "`this`."""
  def has(i)             : return i.__dict__
  def keys(i)            : return i.has().keys()
  def items(i)           : return i.has().items()
  def __init__(i,**d)    : i.has().update(d)
  def __setitem__(i,k,v) : i.has()[k] = v
  def __getitem__(i,k)   : return i.has()[k]
  def __repr__(i)        : return 'Uber'+str(i.has())
  def copy(i): 
      j = Uber()
      for k in i.has(): j[k] = i[k]
      return j
  def asList(i,keys=[]):
    keys = keys or i.keys()
    return [i[k] for k in keys]