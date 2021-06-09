'''
Given an exclusive price and VAT Tax provided by the user,
calculate the VAT amount then return the inclusive price.
'''

from typing import AsyncGenerator


def calculateVAT(exclusivePrice, vatTax):
    vatAmount = 0
    inclusivePrice = 0

    vatAmount = exclusivePrice * vatTax
    inclusivePrice = exclusivePrice + vatAmount

    return inclusivePrice

def userInput(age, name):

    calculateVAT(exclusivePrice, vatTax):

userInput(age, name):
