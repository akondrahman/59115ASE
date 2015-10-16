# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:47:36 2015

@author: akond
"""

from random import uniform
import math 

class Model(object):
    def __init__(self):
        self.decisionVec=[0]        
        self.lowerRange=[0]
        self.numOfDec=0
        self.numOfObjs=0        
        self.upperRange=[0]


    def check(self):
        for count in range(0,self.numOfDec):
            if (self.decisionVec[count]<self.lowerRange[count]) or (self.decisionVec[count]>self.upperRange[count]):
              return False
        return True

    def copy(self,other):
        self.decisionVec = [_ for _ in other.decisionVec]
        self.lowerRange = [_ for _ in other.lowerRange]
        self.numOfDec = other.numOfDec
        self.numOfObjs = other.numOfObjs        
        self.upperRange = [_ for _ in other.upperRange]

    def generateInitialVector(self):
        ## we use random.uniform() as it geives floating point values as well 
        while True:
            for cnt in range(0,self.numOfDec):
                self.decisionVec[cnt]=uniform(self.lowerRange[cnt],self.upperRange[cnt])
            if self.check(): break

    def getobj(self):
        return []

    def sumOfObjs(self):
        return sum(self.getobj())

class Golinski(Model):

    def __init__(self):
        ## first specify the requirements         
        self.decisionVec=[0,0,0,0,0,0,0]        
        self.lowerRange=[2.6,0.7,17.0,7.3,7.3,2.9,5.0]
        self.numOfDec=7
        self.numOfObjs=10
        self.upperRange=[3.6,0.8,28.0,8.3,8.3,3.9,5.5]
        ## then create the initialization 
        self.generateInitialVector()

    def check(self):
        constCheckerVec = [0,0,0,0,0,0,0]
        constCheckerVec[0]=     ((1.0)/(self.decisionVec[0]*math.pow(self.decisionVec[1],2)*self.decisionVec[2])) - (1.0/27.0) 
        constCheckerVec[1]= 6 - (self.decisionVec[0]) - (self.decisionVec[1])
        constCheckerVec[2]= 2 - (self.decisionVec[1]) + (self.decisionVec[0])
        constCheckerVec[3]= 2 - (self.decisionVec[0]) + (3*self.decisionVec[1])
        constCheckerVec[4]= 4 - (self.decisionVec[3]) - math.pow(((self.decisionVec[2]) - 3), 2)
        constCheckerVec[5]=     math.pow((self.decisionVec[4]-3), 3) + ((self.decisionVec[5]) - 4) 
        for cnt in range(0,self.numOfDec):
            if (self.decisionVec[cnt] < self.lowerRange[cnt]) or (self.decisionVec[cnt]>self.upperRange[cnt]) or (constCheckerVec[cnt] < 0):
              return False
        return True


    def getobj(self):
        giveSquaredValue = lambda val : math.pow(val, 2)
        f1=-(
             25 * math.pow((self.decisionVec[0]-2), 2)+
             math.pow((self.decisionVec[1]-2), 2)     +
             math.pow((self.decisionVec[2]-1), 2)     * 
             math.pow((self.decisionVec[3]-4), 2)     + 
             math.pow((self.decisionVec[4]-1), 2)
             )
        
        f2=( 
             giveSquaredValue(self.decisionVec[0]) + 
             giveSquaredValue(self.decisionVec[1]) +
             giveSquaredValue(self.decisionVec[2]) +
             giveSquaredValue(self.decisionVec[3]) +
             giveSquaredValue(self.decisionVec[4]) +
             giveSquaredValue(self.decisionVec[5])
           )
        return [f1,f2]

class Osyczka2(Model):

    def __init__(self):
        ## first specify the requirements         
        self.decisionVec=[0,0,0,0,0,0]        
        self.lowerRange=[0,0,1,0,1,0]
        self.numOfDec=6
        self.numOfObjs=2
        self.upperRange=[10,10,5,6,5,10]
        ## then create the initialization 
        self.generateInitialVector()

    def check(self):
        constCheckerVec = [0,0,0,0,0,0]
        constCheckerVec[0]=     (self.decisionVec[0]) + (self.decisionVec[1]) - 2 
        constCheckerVec[1]= 6 - (self.decisionVec[0]) - (self.decisionVec[1])
        constCheckerVec[2]= 2 - (self.decisionVec[1]) + (self.decisionVec[0])
        constCheckerVec[3]= 2 - (self.decisionVec[0]) + (3*self.decisionVec[1])
        constCheckerVec[4]= 4 - (self.decisionVec[3]) - math.pow(((self.decisionVec[2]) - 3), 2)
        constCheckerVec[5]=     math.pow((self.decisionVec[4]-3), 3) + ((self.decisionVec[5]) - 4) 
        for cnt in range(0,self.numOfDec):
            if (self.decisionVec[cnt] < self.lowerRange[cnt]) or (self.decisionVec[cnt]>self.upperRange[cnt]) or (constCheckerVec[cnt] < 0):
              return False
        return True


    def getobj(self):
        giveSquaredValue = lambda val : math.pow(val, 2)
        f1=-(
             25 * math.pow((self.decisionVec[0]-2), 2)+
             math.pow((self.decisionVec[1]-2), 2)     +
             math.pow((self.decisionVec[2]-1), 2)     * 
             math.pow((self.decisionVec[3]-4), 2)     + 
             math.pow((self.decisionVec[4]-1), 2)
             )
        
        f2=( 
             giveSquaredValue(self.decisionVec[0]) + 
             giveSquaredValue(self.decisionVec[1]) +
             giveSquaredValue(self.decisionVec[2]) +
             giveSquaredValue(self.decisionVec[3]) +
             giveSquaredValue(self.decisionVec[4]) +
             giveSquaredValue(self.decisionVec[5])
           )
        return [f1,f2]



class Schaffer(Model):

    def __init__(self):
        ## first specify the requirements         
        self.decisionVec=[0]
        self.lowerRange=[-100000]
        self.numOfDec=1
        self.numOfObjs=2
        self.upperRange=[100000]
        ## then create the initialization 
        self.generateInitialVector()

    def getobj(self):
        f1=math.pow(self.decisionVec[0], 2)
        f2=math.pow((self.decisionVec[0]-2), 2)
        return [f1,f2] 



class Kursawe(Model):

    def __init__(self):
        ## first specify the requirements 
        self.decisionVec=[0,0,0]        
        self.lowerRange=[-5,-5,-5]
        self.numOfDec=3
        self.numOfObjs=2
        self.upperRange=[5,5,5]
        ## then create the initialization 
        self.generateInitialVector()

    def getobj(self):
        f1=0
        f2=0 
        theA = 0.8
        theB = 1.0
        for cntI in range(0,self.numOfDec):
            if cntI< self.numOfDec-1: 
                f1 = f1 + ( -10*math.exp(-0.2*math.sqrt( math.pow( self.decisionVec[cntI], 2) + math.pow( self.decisionVec[cntI+1], 2))))
                f2 = f2 + ( math.pow( abs(self.decisionVec[cntI]), theA ) + 5 * math.sin( math.pow( self.decisionVec[cntI], theB) ) )
        return [f1,f2]