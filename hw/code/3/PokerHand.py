# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:13:18 2015

@author: akond
"""
from Card import  *
import sys 

class DeckOfCards(Deck):
    def deal_hands(deck, numCardParam, numHandParam):
      listOfHands = []
      for i in range(numHandParam):        
            handObj = PokerHand()
            deck.move_cards(handObj, numCardParam)            
            handObj.classify()            
            listOfHands.append(handObj)
      return listOfHands

class PokerHand(Hand):

    # 
    pokerLabels = ["three_kind" , "four_kind", "full_house", "flush", "straight_flush",
                     "one_pair",   "high_card",   "two_pair",  "straight"]

    def getCardFreq(self):
        """Computes histograms for suits and hands.

        Creates attributes:

          suits: a histogram of the suits in the hand.
          ranks: a histogram of the ranks.
          sets: a sorted list of the rank sets in the hand.
        """

        self.suits = {}
        self.ranks = {}        
        
        for cardObj in self.cards:

            incrementCounter(self.suits, cardObj.suit)
            incrementCounter(self.ranks, cardObj.rank)            

        self.sets = self.ranks.values()
        self.sets.sort(reverse=True)
 


    def has_flush(self):
        ## Wiki says: where all five cards are of the same suit, but not in sequence
        for val in self.suits.values():
            if val >= 5:
                return True
	return False

    def has_straight(self):
        ## Wiki says: 
        ##  a hand that contains five cards of sequential rank in at least two different suits.
        cardRanks = self.ranks
        cardRanks[14] = cardRanks.get(1, 0)
        return self.checkIfInARow(cardRanks, 5)

    def checkIfInARow(self, ranksParam, howManyP):
        valToRet = False 
        count = 0
        for i in range(1, 15):
            if ranksParam.get(i, 0):
                count += 1
                if count == howManyP: 
                    valToRet =  True
            else:
                count = 0
        return valToRet



    
        
    def check_sets(self, *otherParam):
        valToRet = True
        tempMap = zip(otherParam, self.sets)
        for comparer, compared in tempMap:
            if comparer > compared: 
                valToRet = False
        return valToRet

    def has_one_pair(self):
        ## (1) Wiki says : a hand that contains two cards of one rank, plus three cards which are not of this rank nor the same as each other. 
        ##
        return self.check_sets(2)
        
    def has_two_pair(self):
        ## (2) Wiki says : a hand that contains two cards of the same rank, plus two cards of another rank
        ##
        return self.check_sets(2, 2)
        
    def has_three_kind(self):
        ## (3) Wiki says : a hand that contains all three cards of one rank and any other (unmatched) card
        ##
        return self.check_sets(3)
        
    def has_four_kind(self):
        ## (4) Wiki says : a hand that contains three cards of the same rank, plus two cards which are not of this rank nor the same as each other.
        ##
        return self.check_sets(4)

    def has_full_house(self):
        ## (5) Wiki says : a hand that  contains three matching cards of one rank and two matching cards of another rank
        ##
        return self.check_sets(3, 2)    

                
    def has_straight_flush(self):
        # (6) Wiki says: 
        # A straight flush is a hand that contains five cards in sequence, all of the same suit 
        # partition the hand by suit and check each
        # sub-hand for a straight
        myDict = {}
        for cardObj in self.cards:
            tempHand = PokerHand()
            temp = myDict.setdefault(cardObj.suit, tempHand)
            temp.add_card(cardObj)
            

        for handObj in myDict.values():
            if len(handObj.cards) < 5:
                continue
            handObj.getCardFreq()
            if handObj.has_straight():
                return True
        return False
    def has_high_card(self):
        ## Wiki says: does not fall under (1)-(6) 
        return len(self.cards)

    def classify(self):
        ### ???
        ### ???
        self.getCardFreq()

        self.labels = []
        for label in PokerHand.pokerLabels:
            boolValToUse = getattr(self, 'has_' + label)
            #print "f: {} <> {}".format(f, f())
            if boolValToUse():
                self.labels.append(label)
                
                
                

        
def incrementCounter(histParam, labelP): 
    histParam[labelP] = histParam.get(labelP, 0) + 1    
    if histParam[labelP] == 0:
        del histParam[labelP]


def main(*args):
    labelDict = {}
    cardNumber = 5
    handNumber = 10


    n = 1000     
    for i in range(n):
        deck = DeckOfCards()
        deck.shuffle()

        hands = deck.deal_hands(cardNumber, handNumber)
        for hand in hands:
            for label in hand.labels:
                incrementCounter(labelDict, label)
            
    #totalCnt = 7 * n
    #print "Total number of handling {}".format(totalCnt)
    totalCnt = n 

    for label in PokerHand.pokerLabels:
        freq = labelDict.get(label, 0)
        if freq == 0:
            continue
        prob = float (totalCnt) / float(freq)
        print "{} happens once out of {} times".format(label, prob)

        
if __name__ == '__main__':
    main(*sys.argv)           