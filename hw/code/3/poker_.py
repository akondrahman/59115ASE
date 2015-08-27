# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:21:15 2015

@author: akond
"""


import sys

from Card import * 
import PokerHand



#class Hist(dict):
#    """A map from each item (x) to its frequency."""

#    def __init__(self, seq=[]):
#        "Creates a new histogram starting with the items in seq."
#        for x in seq:
#            self.count(x)

#    def count(self, x, f=1):
#        "Increments the counter associated with item x."
#        self[x] = self.get(x, 0) + f
#        if self[x] == 0:
#            del self[x]





class PokerDeck(Deck):
    """Represents a deck of cards that can deal poker hands."""

    def deal_hands(deck, numCardParam, numHandParam):
        import PokerHand
        hands = []
        for i in range(numHandParam):        
            hand = PokerHand()
            deck.move_cards(hand, numCardParam)
            hand.classify()
            hands.append(hand)
        return hands
        
def incrementCounter(histParam, labelP): 
    histParam[labelP] = histParam.get(labelP, 0) + 1    
    if histParam[labelP] == 0:
        del histParam[labelP]


def main(*args):
    # the label histogram: map from label to number of occurances
    labelDict = {}
    cardNumber = 5 
    handNumber = 10 

    # loop n times, dealing 7 hands per iteration, 7 cards each
    #n = 10000
    n = 1000     
    for i in range(n):
        #if i%1000 == 0:
        #    print i
            
        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(cardNumber, handNumber)
        for hand in hands:
            for label in hand.labels:
                #print "labelDict: ", labelDict
                #lhist.count(label)
                incrementCounter(labelDict, label)
            
    # print the results
    totalCnt = 7.0 * n
    print "Total number of handling {}".format(totalCnt)

    for label in PokerHand.pokerLabels:
        freq = labelDict.get(label, 0)
        if freq == 0: 
            continue
        p = totalCnt / freq
        print "{} happens one time in {}".format(label, p)

        
if __name__ == '__main__':
    main(*sys.argv)

