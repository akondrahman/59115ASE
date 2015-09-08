import randomGeneration, energy
#neighborVal = randomGeneration.getNeighbor()
#print neighborVal
import sys

def say(x):
  sys.stdout.write(str(x)); sys.stdout.flush()

minMaxSchaffer = energy.getBaselineMinMaxForSchaffer()
##############################
kMaxVal =1000
eMaxVal = -0.5 ## as we have normalized it , it should be in between 0 and 1 
###################### Start doing simulated annelaing 
startVal = randomGeneration.getRandVal()
currEnergyVal = energy.calcNormEnergy(startVal, minMaxSchaffer[0], minMaxSchaffer[1])
print ("Starting Energy -> {} for {}".format(currEnergyVal, startVal))
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

teja = 0

while (counter < kMaxVal)  and (currEnergyVal > eMaxVal):
    #print "Inside : {}----{}".format(currEnergyVal, counter)
    
    neighborVal = randomGeneration.getRandVal()
    energyNeighbour = energy.calcNormEnergy(neighborVal, minMaxSchaffer[0], minMaxSchaffer[1])
    if energyNeighbour < bestEnergyVal:
       bestEnergyVal = energyNeighbour
       bestSolVal = neighborVal 
       say("!") ,
       #cntForExcl = cntForExcl + 1
    
    if energyNeighbour < currEnergyVal:
       currSolnVal = neighborVal
       currEnergyVal = energyNeighbour 
       say("+") , 
       #cntForPlus = cntForPlus + 1
    elif randomGeneration.getProbOfAcceptance(currEnergyVal, energyNeighbour, float(counter)/float(kMaxVal))  <= randomGeneration.getRandomProb() :   
       currSolnVal = neighborVal
       currEnergyVal = energyNeighbour 
       say("?"),
       cntForQ = cntForQ + 1
       
       say("."), 
    #cntForDot = cntForDot + 1
    counter = counter + 1
    #if counter % 50 == 0:
       #print ("\n ?={} !={} +={} .={} |".format(cntForQ, cntForExcl, cntForPlus, cntForDot))
    teja += 1

    if teja%50 == 0:
      print(cntForQ)
      print("\n")
      teja = 0
      cntForQ = 0

print("\n")
print ("We tried it {} times".format(counter))
print("\n")
print ("The best solution is : {} , and it's energy is {}".format(bestSolVal, bestEnergyVal)     )

