# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:09:35 2015

@author: akond
"""

from ok import * 
import time, checker, oscyzaka2, math
print time.strftime("%H:%M:%S\n")

@ok
def test_a_checkVariableBounds():
    assert True==checker.checkVariableBounds([0, 10, 5, 3, 1, 9])    

@ok
def test_b_checkVariableBounds():
    assert False==checker.checkVariableBounds([-1, 10, 5, 3, 1, 9])        
@ok
def test_c_checkVariableBounds():
    assert False==checker.checkVariableBounds([-1, 10, 5, 3, 0, 9])            
    
@ok
def test_d_checkVariableBounds():
    assert False==checker.checkVariableBounds([-1, 12, 5, 3, 0, 9])                
    
@ok
def test_e_checkVariableBounds():
    assert False==checker.checkVariableBounds([-1, 12, 0, 3, 0, 9])    
    
@ok
def test_f_checkVariableBounds():
    assert True==checker.checkVariableBounds([1, 2, 3, 3, 3, 9])        

@ok
def test_a_checkConstraints():
    vecToTest = [1, 2, 3, 3, 3, 9]
    assert True == checker.checkVariableBounds(vecToTest)
    assert True==checker.checkConstraints(vecToTest)        
    
@ok
def test_b_checkConstraints():
    vecToTest = [-1, 2, 3, 3, 3, 9]
    assert False==checker.checkVariableBounds(vecToTest)
    assert False==checker.checkConstraints(vecToTest)        
@ok
def test_c_checkConstraints():
    vecToTest = [0, 2, 3, 3, 1, 9]
    assert True==checker.checkVariableBounds(vecToTest)
    assert False==checker.checkConstraints(vecToTest)   
    
@ok
def test_a_checkoscyzaka2_obj1():
    vecToTest = [1, 2, 3, 3, 3, 9]
    assert True==checker.checkVariableBounds(vecToTest)
    assert True==checker.checkConstraints(vecToTest)   
    assert -33==oscyzaka2._firstObj(vecToTest)         

@ok
def test_b_checkoscyzaka2_obj1():
    vecToTest = [0, 2, 3, 3, 1, 9]
    assert True==checker.checkVariableBounds(vecToTest)
    assert False==checker.checkConstraints(vecToTest)   
    assert True==math.isnan(oscyzaka2._firstObj(vecToTest))         

@ok
def test_c_checkoscyzaka2_obj1():
    vecToTest = [1.0, 2.0, 3.0, 3.0, 3.0, 9.0]
    assert True==checker.checkVariableBounds(vecToTest)
    assert True==checker.checkConstraints(vecToTest)   
    assert -33==oscyzaka2._firstObj(vecToTest)          
    
@ok
def test_a_checkoscyzaka2_obj2():
    vecToTest = [1, 2, 3, 3, 3, 9]
    assert True==checker.checkVariableBounds(vecToTest)
    assert True==checker.checkConstraints(vecToTest)   
    assert 113==oscyzaka2._secondObj(vecToTest)


@ok
def test_b_checkoscyzaka2_obj2():
    vecToTest = [0, 2, 3, 3, 1, 9]
    assert True==checker.checkVariableBounds(vecToTest)
    assert False==checker.checkConstraints(vecToTest)   
    assert True==math.isnan(oscyzaka2._secondObj(vecToTest))
    
@ok
def test_c_checkoscyzaka2_obj2():
    vecToTest = [-5.5, 2, 3, 3, 1, -1.9]
    assert False==checker.checkVariableBounds(vecToTest)
    assert False==checker.checkConstraints(vecToTest)   
    assert True==math.isnan(oscyzaka2._secondObj(vecToTest))