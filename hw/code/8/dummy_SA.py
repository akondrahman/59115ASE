# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:47:32 2015

@author: akond
"""



from __future__ import print_function
import randomGeneration, energy

def say(x): print(x, end="")

#neighborVal = randomGeneration.getNeighbor()
#print neighborVal
minMaxSchaffer = energy.getBaselineMinMaxForSchaffer()
##############################
kMaxVal =1000
#kMinVal = 1
eMaxVal = 0.00000000001 ## as we have normalized it , it should be in between 0 and 1
###################### Start doing simulated annelaing
startVec = randomGeneration.getRandVec()
startVal = startVec[1] 
currEnergyVal = energy.calcNormEnergy(startVal, minMaxSchaffer[0], minMaxSchaffer[1])
say("Starting Energy -> {} for {}\n".format(currEnergyVal, startVal))
#### assignment
currVec=startVec
#
currSolnVal=startVal
bestSolVal = startVal
bestEnergyVal = currEnergyVal
## counter tells howmany times we will iterate 
counter = 100000

###print purpose
output = ""
cntForQ=0
cntForExcl=0
cntForPlus=0
cntForDot=0
countLoop=0

while (counter > 0)  and (currEnergyVal > eMaxVal):
    #print "Inside : {}----{}".format(currEnergyVal, counter)

    #neighborVal = randomGeneration.getRandVal()
    ###
    neighborVec=randomGeneration.getNeighborRandonmly(currVec)
    neighborVal = neighborVec[1]
    energyNeighbour = energy.calcNormEnergy(neighborVal, minMaxSchaffer[0], minMaxSchaffer[1])
    ## check if energy is negative 
    if energyNeighbour < 0:
       #energyNeighbour = energyNeighbour * float(-1)  
       energyNeighbour = bestEnergyVal

    if energyNeighbour < bestEnergyVal:
       bestEnergyVal = energyNeighbour
       bestSolVal = neighborVal
       output +=  "!"
       cntForExcl = cntForExcl + 1

    if energyNeighbour < currEnergyVal:
       currSolnVal = neighborVal
       currEnergyVal = energyNeighbour
       output +=  "+"
       cntForPlus = cntForPlus + 1
    elif randomGeneration.getProbOfAcceptance(currEnergyVal, energyNeighbour, float(counter)/float(kMaxVal))  > randomGeneration.getRandomProb() :
       currSolnVal = neighborVal
       currEnergyVal = energyNeighbour
       output += "?"
       cntForQ = cntForQ + 1
    else:
      output +=  "."
      cntForDot = cntForDot + 1
    counter = counter - 1
    countLoop = countLoop + 1
    if counter % 40 == 0:
       say("\n count ={}, best energy seen so far= {},  ?={}, !={}, +={}, .={} :".format(countLoop, bestEnergyVal, cntForQ, cntForExcl, cntForPlus, cntForDot))
       say(output + '\n')
       cntForQ = 0
       cntForExcl = 0
       cntForPlus = 0
       cntForDot = 0
       output = ""

# print "We tried it {} times".format( counter)
say("\n")
say("The best solution is : {} , and it's energy is {}\n".format(bestSolVal, bestEnergyVal))
say("\n")
say("Baseline energy values for Shaffer: min={}, max={}".format(minMaxSchaffer[0], minMaxSchaffer[1]))
say("\n")
