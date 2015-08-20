# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:59:26 2015

@author: akond
"""
from swampy.TurtleWorld import *  
   
def drawTriangle(turtleParam, length, angle):
    '''
     This module draws a triangle
    '''
    import math
    legLen = length * math.sin(angle * math.pi / 180)
    #for i in range(3):
    rt(turtleParam, angle)
    fd(turtleParam, length)
    lt(turtleParam, 90 + angle)
    fd(turtleParam, 2 * legLen)    
    lt(turtleParam, 90 + angle)
    fd(turtleParam, length)
    lt(turtleParam, 180 - angle)    
    
## 
def drawPie(tParam, segmentCount, lengthParam):
    angle = 360 / segmentCount
    for count in range(segmentCount):
        drawTriangle(tParam, lengthParam, angle/2)
        lt(tParam, angle)
    
    
lengthVal = 100
segments=10

#Picture # 1
world = TurtleWorld()
turtleObj = Turtle()
drawPie(turtleObj, segments, lengthVal)
#Picture # 2 
world = TurtleWorld()
turtleObj = Turtle()
segments=6
drawPie(turtleObj, segments, lengthVal)
#Picture # 3 
world = TurtleWorld()
turtleObj = Turtle()
segments=5
drawPie(turtleObj, segments, lengthVal)
#Picture # 4
world = TurtleWorld()
turtleObj = Turtle()
segments=4
drawPie(turtleObj, segments, lengthVal)
#Picture # 5
world = TurtleWorld()
turtleObj = Turtle()
segments=10
drawPie(turtleObj, segments, lengthVal)
#Picture # 6
world = TurtleWorld()
turtleObj = Turtle()
segments=8
drawPie(turtleObj, segments, lengthVal)
#drawTriangle(turtleObj, lengthVal, angleVal)       
wait_for_user()