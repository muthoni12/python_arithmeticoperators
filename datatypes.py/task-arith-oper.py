inclusivePrice = 53
vatTax = 0.17 #17/100
vatAmount = 0
exclusivePrice = 0

vatAmount = (inclusivePrice * vatTax) / (1 + vatTax)
exclusivePrice = inclusivePrice - vatAmount

print(exclusivePrice)