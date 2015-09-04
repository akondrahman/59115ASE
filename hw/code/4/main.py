# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:28:18 2015

@author: akond
"""



import randomGeneration, energy
#neighborVal = randomGeneration.getNeighbor()
#print neighborVal
minMaxSchaffer = energy.getBaselineMinMaxForSchaffer()
##############################
kMaxVal =1000
eMaxVal = -1.0 ## as we have normalized it , it should be in between 0 and 1 
###################### Start doing simulated annelaing 
startVal = randomGeneration.getRandVal()
currEnergyVal = energy.calcNormEnergy(startVal, minMaxSchaffer[0], minMaxSchaffer[1])
print "Starting Energy -> {} for {}".format(currEnergyVal, startVal)
#### assignment 
currSolnVal=startVal
bestSolVal = startVal 
bestEnergyVal = currEnergyVal
counter = 1  

###print purpose
cntForQ=0
cntForExcl=0
cntForPlus=0
cntForDot=0


while (counter < kMaxVal)  and (currEnergyVal > eMaxVal):
    #print "Inside : {}----{}".format(currEnergyVal, counter)
    
    neighborVal = randomGeneration.getRandVal()
    energyNeighbour = energy.calcNormEnergy(neighborVal, minMaxSchaffer[0], minMaxSchaffer[1])
    if energyNeighbour < bestEnergyVal:
       bestEnergyVal = energyNeighbour
       bestSolVal = neighborVal 
       print "!" ,
       cntForExcl = cntForExcl + 1
    
    if energyNeighbour < currEnergyVal:
       currSolnVal = neighborVal
       currEnergyVal = energyNeighbour 
       print "+" , 
       cntForPlus = cntForPlus + 1
    elif randomGeneration.getProbOfAcceptance(currEnergyVal, energyNeighbour, float(counter)/float(kMaxVal))  > randomGeneration.getRandomProb() :   
       currSolnVal = neighborVal
       currEnergyVal = energyNeighbour 
       print "?" ,
       cntForQ = cntForQ + 1
       
    print "." , 
    cntForDot = cntForDot + 1
    counter = counter + 1
    if counter % 50 == 0:
       print "\n ?={} !={} +={} .={} |".format(cntForQ, cntForExcl, cntForPlus, cntForDot)

print"\n"
print "We tried it {} times".format(counter)
print"\n"
print "The best solution is : {} , and it's energy is {}".format(bestSolVal, bestEnergyVal)        
        