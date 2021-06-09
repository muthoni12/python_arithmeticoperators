'''
Given an exclusive price and VAT Tax provided by the user,
calculate the VAT amount then return the inclusive price.
'''

from typing import AsyncGenerator

exclusivePrice = 50
vatTax = 0.16 #16/100
vatAmount = 0
inclusivePrice = 0

vatAmount = exclusivePrice * vatTax
inclusivePrice = exclusivePrice + vatAmount

print(exclusivePrice)

Given an inclusive price and VAT Tax provided by the user,
calculate the VAT amount then return the exclusive price.

inclusivePrice = 53
vatTax = 0.17 #17/100
vatAmount = 0
exclusivePrice = 0

vatAmount = inclusivePrice * vatTax
exclusivePrice = inclusivePrice - vatAmount

print(exclusivePrice)


def calculateVAT(inclusivePrice, vatTax):
    vatAmount = 0
    exclusivePrice = 0

    vatAmount = exclusivePrice * vatTax
    inclusivePrice = exclusivePrice + vatAmount

    return inclusivePrice

def userInput():
    inclusivePrice = input("inclusive price"))
    vatTax = input("vatTax"))

    calculateVAT(inclusivePrice, vatTax):

userInput():
