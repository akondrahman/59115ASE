# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:13:18 2015

@author: akond
"""
from Card import  *

### As per assignment instructions, this code works on top of PokerHand.py available at http://www.greenteapress.com/thinkpython/code/ 

class DeckOfCards(Deck):
    def assignCardsToHands(deck, numCardParam, numHandParam):
      listOfHands = []
      for cnt in range(numHandParam):        
            handObj = PokerHand()
            deck.move_cards(handObj, numCardParam)            
            handObj.classify()            
            listOfHands.append(handObj)
      return listOfHands

class PokerHand(Hand):

    # 
    pokerLabels = ["three_kind" , "four_kind", "full_house", "flush", "straight_flush",
                        "two_pair",  "straight"]
                     
    #pokerLabels = ["three_kind" , "four_kind", "full_house", "flush", "straight_flush",
    #                 "one_pair",   "high_card",   "two_pair",  "straight"]
                     
    def getCardFreq(self):
        self.suits = {}
        self.ranks = {}        
        
        for cardObj in self.cards:

            incrementCounter(self.suits, cardObj.suit)
            incrementCounter(self.ranks, cardObj.rank)            

        self.sets = self.ranks.values()
        self.sets.sort(reverse=True)
 


    def flush_exists(self):
        ## Wiki says: where all five cards are of the same suit, but not in sequence
        valToRet = False
        for val in self.suits.values():
            if val >= 5:
                valToRet =  True
	return valToRet

    def straight_exists(self):
        ## Wiki says: 
        ##  a hand that contains five cards of sequential rank in at least two different suits.
        cardRanks = self.ranks
        cardRanks[14] = cardRanks.get(1, 0)
        return self.checkIfInARow(cardRanks, 5)

    def checkIfInARow(self, ranksParam, howManyP):
        valToRet = False 
        count = 0
        # remmeber there are 14 different ranks as defined in Card.py 
        for i in range(1, 14):
            if ranksParam.get(i, 0):
                count += 1
                if count == howManyP: 
                    valToRet =  True
            else:
                count = 0
        return valToRet

        
    def checkRankCriteria(self, *otherParam):
        # didn't have to write functions for method overloading : thanks * operator !
        valToRet = True
        tempMap = zip(otherParam, self.sets)
        for comparer, compared in tempMap:
            if comparer > compared: 
                valToRet = False
        return valToRet

    #buggy
    #def one_pair_exists(self):
        ## (1) Wiki says : a hand that contains two cards of one rank, plus three cards which are not of this rank nor the same as each other. 
        ##
   #     return self.checkRankCriteria(2)
        
    def two_pair_exists(self):
        ## (2) Wiki says : a hand that contains two cards of the same rank, plus two cards of another rank
        ##
        return self.checkRankCriteria(2, 2)
        
    def three_kind_exists(self):
        ## (3) Wiki says : a hand that contains all three cards of one rank and any other (unmatched) card
        ##
        return self.checkRankCriteria(3)
        
    def four_kind_exists(self):
        ## (4) Wiki says : a hand that contains three cards of the same rank, plus two cards which are not of this rank nor the same as each other.
        ##
        return self.checkRankCriteria(4)

    def full_house_exists(self):
        ## (5) Wiki says : a hand that  contains three matching cards of one rank and two matching cards of another rank
        ##
        return self.checkRankCriteria(3, 2)    

                
    def straight_flush_exists(self):
        # (6) Wiki says: 
        # A straight flush is a hand that contains five cards in sequence, all of the same suit 
        # partition the hand by suit and check each
        # sub-hand for a straight
        valToRet = False        
        myDict = {}
        for cardObj in self.cards:
            tempHand = PokerHand()
            temp = myDict.setdefault(cardObj.suit, tempHand)
            temp.add_card(cardObj)
        for handObj in myDict.values():
            if len(handObj.cards) < 5:
                continue
            handObj.getCardFreq()
            if handObj.straight_exists():
                valToRet = True
        return valToRet
    
    #buggy    
    #def high_card_exists(self):
    #    valToRet = False 
    #    if len(self.cards) > 0:
    #        valToRet = True
        ## Wiki says: this does not fall under (1)-(6) 
    #    return valToRet

    def classify(self):
        self.getCardFreq()

        self.labels = []
        for label in PokerHand.pokerLabels:
            # if my hand has flush/st. flush then add the correspondin label to the hand 
            boolValToUse = getattr(self,  label + "_exists")
            if boolValToUse():
                self.labels.append(label)
                
def incrementCounter(histParam, labelP): 
    histParam[labelP] = histParam.get(labelP, 0) + 1    
    if histParam[labelP] == 0:
        del histParam[labelP]


def executeSimulation(cardP, handP, simRunP):
    labelDict = {}
    for i in range(simRunP):
        deck = DeckOfCards()
        deck.shuffle()
        hands = deck.assignCardsToHands(cardP, handP)
        for hand in hands:
            for label in hand.labels:
                incrementCounter(labelDict, label)
    printResultTable(labelDict, simRunP)            

def printResultTable(labelDictP, simRunP):
      sepVar = "=\t"
      print "LabelName" + sepVar + "Probability"
      print "---------------------------"
      for label in PokerHand.pokerLabels:
        freq = labelDictP.get(label, 0)
        if freq == 0:
            continue
            # to handle division by error 
        prob = float (simRunP) / float(freq)
        print "{}".format(label) + sepVar +"{}/{}".format(str(1), prob)    