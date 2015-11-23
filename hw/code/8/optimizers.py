# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:25:29 2015

@author: akond
"""



from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform,randint,random
import utilities 
#from time import time
#import numpy as np
#Currently Minimizing
def SimulatedAnnealing(modelParam):
    ###print purpose
    output = ""
    cntForQ=0
    cntForExcl=0
    cntForPlus=0
    cntForDot=0

    printCounter =  0 

    eMaxVal = 0
    curr_sol=modelParam()
    best_sol =modelParam()
    best_sol.copy(curr_sol)
    #print("Before ... ", curr_sol.getCurrentBaseline()) 
    
    curr_sol.updateBaseline(curr_sol.getIntialBaseline())
    #print( "After ... ",    curr_sol.getCurrentBaseline())  
    #exit 
    ## kMaxVal is always fixed to 1000 !
    kMaxVal=1000
    counter = 0 
    counter = 1000
    ## to keep track of eras 
    eraDict = {}
    eraCount  = 0
    eraTracker = 50
    crr_era, prev_era = [], [0 for _ in range(curr_sol.numOfDec)]
    terminateCount = 0 
    terminator = 10 
    eraList = []
    a12Factor = 0.56
    eraDictCount  = 0
    while (counter > 0) and (curr_sol.sumOfObjs() > eMaxVal):
        printCounter = printCounter + 1

        neighbor_sol=generateNeighbor(curr_sol, randint(0, curr_sol.numOfDec-1), modelParam)
        

        if neighbor_sol.sumOfObjs() < best_sol.sumOfObjs():
            best_sol.copy(neighbor_sol)
            curr_sol.copy(neighbor_sol)
            cntForExcl = cntForExcl + 1
            output = output + "!"
        elif neighbor_sol.sumOfObjs() < curr_sol.sumOfObjs():
            curr_sol.copy(neighbor_sol)
            cntForPlus = cntForPlus + 1
            output = output + "+"
        elif fetchProbOfAcceptance(neighbor_sol.sumOfObjs(), curr_sol.sumOfObjs(), float(counter)/float(kMaxVal)) > random():
            curr_sol.copy(neighbor_sol)
            cntForQ = cntForQ + 1
            output = output + "?"            
        else:
           output = output + "."
           cntForDot = cntForDot  + 1
        if printCounter % eraTracker == 0:
           print("\ncounter={}, best energy seen so far={}, '?'={}, '!'={}, '+'={}, '.'={}, output={}".format(printCounter, best_sol.sumOfObjs(), cntForQ, cntForExcl, cntForPlus, cntForDot, output))
           cntForQ = 0
           cntForExcl = 0
           cntForPlus = 0
           cntForDot = 0
           output = ""
           ## era purpose 
        if eraCount >=20:   
          ## comparing prev and current 
          crr_era = sorted(eraList, reverse=True)
          #print("Current era: ", crr_era)
          eraDictCount = eraDictCount + 1
          eraDict[eraDictCount] = crr_era
          a12Output =  utilities.a12(crr_era, prev_era) 

          if a12Output <= a12Factor:
             terminateCount = terminateCount + 1 
          eraList = []
          eraCount = 0
          prev_era = crr_era
          #print("era count ={}, era dict= {}, a12={}, terminator={}".format(eraCount, prev_era, crr_era, a12Output, terminateCount))
        else:
          eraList.append(best_sol.getobj()) 
          eraCount +=  1
        #if terminateCount >= terminator: 
        #     break 
        if best_sol.sumOfObjs() < best_sol.getCurrentBaseline()[0]: 
          best_sol.updateBaseline( [best_sol.sumOfObjs(), best_sol.getCurrentBaseline()[1]])
        if best_sol.sumOfObjs() > best_sol.getCurrentBaseline()[1]: 
          best_sol.updateBaseline([best_sol.getCurrentBaseline()[0], best_sol.sumOfObjs()])          
        counter = counter - 1    
        #counter= counter + 1   

    _printSolution(best_sol.decisionVec, best_sol.sumOfObjs(), best_sol.getobj(), printCounter)
    _printEndMsg(SimulatedAnnealing.__name__)
    print("------------------------------------------------------------------------------------------------")
    print("Era dictionary First:=", eraDict[1])
    print("Era dictionary Last:=", eraDict[eraDictCount])
    print("------------------------------------------------------------------------------------------------")
    return best_sol.decisionVec


#Currently Minimizing
def MaxWalkSat(model, maxTries=100, maxChanges=10, threshold=0, p=0.5, step=10):
    printCounter = 0
    ####
    #print purpose
    output = ""
    printCounter = 0
    cnt_Exc = 0
    cnt_Que = 0
    cnt_Dot = 0
    cnt_Pls = 0
    ## to keep track of eras
    eraDict = {}
    eraCount = 0
    eraTracker = 50
    temporary_sol= model()   # Just for getting the object
    crr_era, prev_era = [], [0 for _ in xrange(temporary_sol.numOfDec)]   
    terminateCount = 0
    terminator = 10
    eraList = []
    a12Factor = 0.56
    eraDictCount = 0

    for cntTry in range(maxTries):
        curr_solve_for_model = model()
        if cntTry==0:
            sbest=model()
            sbest.copy(curr_solve_for_model)
        for cng in range(maxChanges):
            printCounter = printCounter + 1

            if curr_solve_for_model.sumOfObjs() < threshold:
                print("\n Got lucky !. \n Found the solution early for {} by MaxWlakSat at step {} \n".format(model.__name__, printCounter))
                sbest.copy(curr_solve_for_model)                 
                _printSolution(curr_solve_for_model.decisionVec, curr_solve_for_model.sumOfObjs(), curr_solve_for_model.getobj(), printCounter)
                _printEndMsg(MaxWalkSat.__name__)
                return sbest.decisionVec

            decToMutate=randint(0, curr_solve_for_model.numOfDec-1)
            ## keeping tack of values before mutating annd labeling them as old              
            score_old = curr_solve_for_model.sumOfObjs()
            oldModel = model()
            oldModel.copy(curr_solve_for_model)
            
            if p < random():
                curr_solve_for_model=generateNeighbor(curr_solve_for_model, decToMutate, model)
            else:
                #curr_solve_for_model=_mutateSelectivelyWithModifiedRange(model, curr_solve_for_model, decToMutate, step)
                curr_solve_for_model=_mutateSelectively(model, curr_solve_for_model, decToMutate, step)
            ## lets heck teh ebhavior !    
            if curr_solve_for_model.sumOfObjs() < sbest.sumOfObjs():
                sbest.copy(curr_solve_for_model)
                #'?' means muatted solution  is better than best soultuion
                # btw, we are only interested in the best and we keep that 
                output = output + "?"
                cnt_Que = cnt_Que + 1
            elif curr_solve_for_model.sumOfObjs() < score_old:
                #'!' means muatted solution  is better than old soultuion 
                                
                output = output + "!"
                cnt_Exc = cnt_Exc + 1
            elif curr_solve_for_model.sumOfObjs() >= score_old:
                ## '+' means old solution is better than mutated solution 
                output = output + "+"
                cnt_Pls = cnt_Pls + 1
            else: 
                output = output + "."
                cnt_Dot = cnt_Dot + 1
            # if printCounter % 40 == 0:
            if printCounter % eraTracker == 0:
                print("itrations so far={} '?'={}, '!'={}, '+'={}, '.'={}, output={} ".format(printCounter, cnt_Que, cnt_Exc, cnt_Pls, cnt_Dot,output))
                #print(output + '\n')
                output = ""

                cnt_Que = 0
                cnt_Exc = 0
                cnt_Pls = 0
                cnt_Dot = 0 

            ## era purpose

            if eraCount >=20:
                ## comparing prev and current
                crr_era = sorted(eraList, reverse=True)
                #print("Current era:", curr_era)
                eraDictCount = eraDictCount + 1
                eraDict[eraDictCount] = crr_era
                a12Output = utilities.a12(crr_era, prev_era)

                if a12Output <= a12Factor:
                    terminateCount = terminateCount + 1
                eraList = []
                eraCount = 0
                prev_era = crr_era
                #print("era count ={}, era dict= {}, a12={}, terminator={}".format(eraCount, prev_era, crr_era, a12Output, terminateCount))
            else:
                eraList.append(sbest.getobj())
                eraCount += 1


    print("Era Dict Count :", eraDictCount)
    print("Era Dictionary First:", eraDict[1])
    print("-------------------------------------------------------------------------------------")     
    print("Era Dictionary Last:", eraDict[eraDictCount])
    print("-------------------------------------------------------------------------------------")     
    
    _printSolution(sbest.decisionVec, sbest.sumOfObjs() , sbest.getobj(), printCounter)    
    _printEndMsg(MaxWalkSat.__name__)
    return sbest.decisionVec




#def _mutateSelectivelyWithModifiedRange(modelP, currSolP, indexP, stepParam=10.0):
#        ## keeptrack ofcurrent         
#        curr=modelP()
#        curr.copy(currSolP)
#        ## keep track of best          
#        best=modelP()
#        best.copy(curr)
#        
#        listOfMax=curr.upperRange
#        listOfMin=curr.lowerRange  
#        
#        fractionedMax = [float(x)*float(stepParam*10)/float(100) for x in listOfMax]
#        fractionedMin = [float(x)*float((stepParam*10)/100) for x in listOfMin]   
#
#        maxRangeOI = float(fractionedMax[indexP])
#        minRangeOI = float(fractionedMin[indexP])
#        stepOfI = (maxRangeOI - minRangeOI)/stepParam   
#        #print("Step of I ", stepOfI) 
#        cnt = minRangeOI    
#        #run = 0 
#        #print("Max Range ",maxRangeOI)
#        while cnt <= maxRangeOI:
#          curr.decisionVec[indexP] = cnt 
#          ## my version of curr.decisionVec[indexP]=curr.decisionVec[indexP]+i*dis
#          if curr.check(): 
#              print("Am I ever true ?")
#              # refactored version of the follwoing for ##  
#              ##if checker.checkConstraints(xCurrent):            
#              if curr.sumOfObjs() < best.sumOfObjs():
#                print("Can we get the best  ?")  
#                best.copy(curr)            
#          # refactored version of the following 
#          ##  if calcNormEnergy(xBest, minMaxTuple) <= calcNormEnergy(xCurrent, minMaxTuple):
#          ##     xBest = [xtemp for xtemp in xCurrent] 
#          cnt = cnt + stepOfI   
#          #print("Value of cnt" , cnt )
#        #print("Bye bbye ")  
#        return best
        
def _mutateSelectively(modelP, currSolP, indexP, stepParam=20):
        ## keeptrack ofcurrent      

        curr=modelP()
        curr.copy(currSolP)
        ## keep track of best          
        best=modelP()
        best.copy(curr)
        ## this implementation of_muateselectively was gathered from Rahul's(TA) 
        ## suggestions          
        ## ranges 
        currLowerRange = curr.lowerRange[indexP]
        currUpperRange = curr.upperRange[indexP]
        theRange = (currUpperRange - currLowerRange )/stepParam
        lowerHalf  = - int((currSolP.decisionVec[indexP]-currSolP.lowerRange[indexP])/theRange)
        # - gives a broader range to look for 
        upperHalf =  int((currSolP.upperRange[indexP]-currSolP.decisionVec[indexP])/theRange) + 1
        for cnt in range( lowerHalf , upperHalf):
            curr.decisionVec[indexP]=curr.decisionVec[indexP] + cnt *theRange
            if curr.check(): 
                if curr.sumOfObjs()<best.sumOfObjs():
                  best.copy(curr)
        return best          
        
def generateNeighbor(currSolP,index,model):
    solToUse=model()
    solToUse.copy(currSolP)
    lowerHalf = solToUse.lowerRange[index] 
    upperHalf  = solToUse.upperRange[index]
    while True:
        solToUse.decisionVec[index]=uniform( lowerHalf, upperHalf)
        if solToUse.check(): 
            break
    return solToUse    
          
def _printSolution(decisionVecParam, energyVal, getObjParam,  stepParam):
  print ("Best solution = {} ... best energy ={}, corresponding objectives: first {}, second {}. Number of steps taken = {}".format(decisionVecParam, energyVal ,getObjParam[0], getObjParam[1], stepParam))  


def fetchProbOfAcceptance(neighborEnergy, currEnergy, theTParam):
    import math     
    normalizationForNegativeEnergy = max(abs(neighborEnergy), abs(currEnergy))
    ## no strong rationale for this 'normalzation' thing ... found sth. on the internet 
    ## and it works 
    theFraction = (((currEnergy - neighborEnergy)/normalizationForNegativeEnergy)/theTParam)
    return math.exp(theFraction)


#def getProbOfAcceptance(currEnergyP, neighbourEnergyP, tParam):
#  # t = k/kmax
#  import math
#  equation = float(1*(currEnergyP-neighbourEnergyP)/float(tParam))
#  accepProbToret = math.exp(equation)
#  return accepProbToret    
    
    
def _printEndMsg(nameOfCaller):
        print("\n")
        print("End of {} .... ".format(nameOfCaller))
        print("----------")
        print("\n")
        #print "got lucky : run info. ----->TRY: {}<>CHANGE:{}".format(cntTryParam, cntChnageParam )        
