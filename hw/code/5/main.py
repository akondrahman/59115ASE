from __future__ import print_function
import random
from baseline import  getValidVector, getBaselineMinMaxForO2, calcNormEnergy
import checker


def say(x): print(x, end="")


def doMaxWalkSat(maxTries=10000, maxChanges=50, threshold=1.0, p=0.5):
  ''' This is the main place holder fo the MaxSatWalk() Algo '''
  solutionVecAndEnergyToRet=[]
  minMaxTuple = getBaselineMinMaxForO2()
  ####
  #print purpose
  output = ""
  printCounter = 0
  cnt_Exc = 0
  cnt_Que = 0
  cnt_Dot = 0
  cnt_Pls = 0

  xCurrent = []
  xBest = []
  for cntTry in range(maxTries):
    #solution = start
    vec = getValidVector()
    #energy = calcNormEnergy(vec, minMaxTuple)
    if cntTry==0:
      xBest= [_ for _ in vec]
      #bestEnergy = calcNormEnergy(vec, minMaxTuple)

    for cntChange in range(maxChanges):

      if calcNormEnergy(vec, minMaxTuple) >= threshold:
        _printEndMsg( cntTry, cntChange )
        solutionVecAndEnergyToRet = [vec, calcNormEnergy(vec, minMaxTuple)]
        return solutionVecAndEnergyToRet
      indexToChange = random.randint(0,5)
      oldSol = [ _ for _ in vec ]
      #oldEnergy = calcNormEnergy(vec, minMaxTuple)
      if p < random.random():
        ## when probailility is > 0.5 then we randomly select a variable and mutate it
        #print "!"

        #print "Now we will mutate randomly "
        mutatedVec  = _mutateRandomly(vec, indexToChange )
        #energy = calcNormEnergy(mutatedVec, minMaxTuple)
        #solutionVecToRet = mutatedVec
        #print "Energy !!! ", solution
      else:
        ## when probailility is <= 0.5 then we  mutate all the variables in the vector
        ## one by one ,see which gives the maximum energy, and keep it as solution
        mutatedVec = _mutateSelectively(vec, minMaxTuple, indexToChange)


      xCurrent =   [ _ for _ in mutatedVec]
      if calcNormEnergy(xBest, minMaxTuple) < calcNormEnergy(xCurrent, minMaxTuple):
         ## the jump was better than the best soultion in hand
         xBest= [ _ for _ in xCurrent ]
         output += "?"
         cnt_Que = cnt_Que + 1
      elif calcNormEnergy(xCurrent, minMaxTuple) < calcNormEnergy(oldSol, minMaxTuple):
         xBest= [ _ for _ in oldSol ]
         output += "+"
         cnt_Pls = cnt_Pls + 1
      #elif calcNormEnergy(xCurrent, minMaxTuple) == calcNormEnergy(oldSol, minMaxTuple):
      #   print "." ,
      #   cnt_Dot = cnt_Dot + 1
      elif calcNormEnergy(xBest, minMaxTuple) > calcNormEnergy(xCurrent, minMaxTuple):
         output += "!"
         cnt_Exc = cnt_Exc + 1
      else:
        output += "."
        cnt_Dot = cnt_Dot + 1
      solutionVecAndEnergyToRet = [xBest, calcNormEnergy(xBest, minMaxTuple)]
      printCounter = printCounter + 1
      if printCounter % 40 == 0:
        say("count={} ?={} !={} +={} .={} |".format(printCounter, cnt_Que, cnt_Exc, cnt_Pls, cnt_Dot))
        say(output + '\n')
        output = ""

        cnt_Que = 0
        cnt_Exc = 0
        cnt_Pls = 0
        cnt_Dot = 0


  _printEndMsg(cntTry, cntChange )
  return  solutionVecAndEnergyToRet





def _mutateRandomly(xVecParam, indexParam):
  import baseline
  vecToUse = [ _ for _ in xVecParam]
  while True:
   #vecToUse[indexParam] = random.uniform(listOfMin[indexParam], listOfMax[indexParam])
   vecToUse[indexParam] = baseline.getVariableBounds(indexParam)
   if checker.checkConstraints(vecToUse):
     break
  return vecToUse



def _mutateSelectively(xVecParam, minMaxTuple,indexP, stepParam=20):
    valToret = 0
    xCurrent=[x for x in xVecParam]
    xBest=xVecParam

    listOfMax=[10, 10, 5, 6, 5, 10]
    listOfMin=[ 0,  0, 1, 0, 1,  0]

#    distance=(listOfMax[indexP]-listOfMin[indexP])/stepParam
#
#    range1 = int((xCurrent[indexP]-listOfMin[indexP])/distance)
#    range2 = int((listOfMax[indexP]-xCurrent[indexP])/distance)
#    #print "r-1 {}, r-2 {},  dist = {}".format(range1, range2, distance)
#    for cnt in range(-range1, range2+1):
#        xCurrent[indexP]=xVecParam[indexP]+cnt*distance
#        if not checker.checkConstraints(xCurrent):
#           continue
#        else:
#          if calcNormEnergy(xBest, minMaxTuple) <= calcNormEnergy(xCurrent, minMaxTuple):
#           xBest=xCurrent
    maxRangeOI = float(listOfMax[indexP])
    minRangeOI = float(listOfMin[indexP])
    stepOfI = float((maxRangeOI - minRangeOI)/stepParam)
    cnt = minRangeOI
    while cnt <= maxRangeOI:
      xCurrent[indexP] = cnt
      if checker.checkConstraints(xCurrent):
        if calcNormEnergy(xBest, minMaxTuple) <= calcNormEnergy(xCurrent, minMaxTuple):
           xBest = [xtemp for xtemp in xCurrent]
      cnt = cnt + stepOfI
    valToret = [ _ for _ in xBest]
    return valToret


def _printEndMsg( cntTryParam, cntChnageParam):
        print("\n")
        print("End of MaxWalkSat .... ")
        #print "got lucky : run info. ----->TRY: {}<>CHANGE:{}".format(cntTryParam, cntChnageParam )


completeSolution = doMaxWalkSat()
print("Final answer: solution {}, corresponding energy {}".format(completeSolution[0], completeSolution[1]))
