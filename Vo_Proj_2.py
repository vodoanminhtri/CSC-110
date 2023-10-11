# Minh Tri Doan Vo
# 10/10/2023
# Project 2
# Groceries list and total groceries cost for making brownies

import math

# serving per batch
batch           = int(12)
person          = int(input("How many people to be servied? "))
servingBatch    = math.ceil(person/batch)

# conversion
OZ              = float(28.3495231)
LB              = int(16)
CUP             = int(8)
CUPtsp          = int(48)
TBSP            = int(3)

# Recipe for 1 batch converted to oz for calculation later
COCOA           = float(106/OZ)
SALT            = float(6/OZ)
BAPOWDER        = float(5/OZ)
ESPPOWDER       = float(2/OZ)
SUGAR           = float(447/(OZ*LB))
FLOUR           = float(180/(OZ*LB))
CHOCOCHIP       = float(340/OZ)
BUTTER          = float(1/2)
VANILLA         = float((1*TBSP*CUP)/CUPtsp)
EGG             = int(4)

# Cost for ingredients per container
cocoaPrice      = float(1.99)
saltPrice       = float(0.49)
baPowderPrice   = float(1.89)
espPowderPrice  = float(5.39)
sugarPrice      = float(1.99)
flourPrice      = float(1.99)
chocoChipPrice  = float(1.99)
butterPrice     = float(2.99)
vanillaPrice    = float(10.59)
eggPrice        = float(1.99)

# volume per Container
cocoaCon        = int(8)
saltCon         = int(26)
baPowderCon     = float(8.1)
espPowderCon    = float(7.05)
sugarCon        = int(4)
flourCon        = int(5)
chocoChipCon    = int(12)
butterCon       = int(1)
vanillaCon      = int(2)
eggCon          = int(18)

# Total item needed for grocery list
cocoaGro        = math.ceil(servingBatch * COCOA / cocoaCon)
saltGro         = math.ceil(servingBatch * SALT / saltCon)
baPowderGro     = math.ceil(servingBatch * BAPOWDER / baPowderCon)
espPowderGro    = math.ceil(servingBatch * ESPPOWDER / espPowderCon)
sugarGro        = math.ceil(servingBatch * SUGAR / sugarCon)
flourGro        = math.ceil(servingBatch * FLOUR / flourCon)
chocoChipGro    = math.ceil(servingBatch * CHOCOCHIP / chocoChipCon)
butterGro       = math.ceil(servingBatch * BUTTER / butterCon)
vanillaGro      = math.ceil(servingBatch * VANILLA / vanillaCon)
eggGro          = math.ceil(servingBatch * EGG / eggCon)

# Price for each item in the grocery list
cocoaTotal      = cocoaGro * cocoaPrice
saltTotal       = saltGro * saltPrice
baPowderTotal   = baPowderGro * baPowderPrice
espPowderTotal  = espPowderGro * espPowderPrice
sugarTotal      = sugarGro * sugarPrice
flourTotal      = flourGro * flourPrice
chocoChipTotal  = chocoChipGro * chocoChipPrice
butterTotal     = butterGro * butterPrice
vanillaTotal    = vanillaGro * vanillaPrice
eggTotal        = eggGro * eggPrice
# Total list in dollar
totalPrice      = cocoaTotal + saltTotal + baPowderTotal + espPowderTotal + sugarTotal + flourTotal + chocoChipTotal + butterTotal + vanillaTotal + eggTotal

# Output result
print("You will need to make", int(servingBatch), "batches of brownies.")
print()
print("-" * 30)
print("\t","Grocery List")
print("-" * 30)
print()
print("Cocoa Powder\t", cocoaGro)
print("Salt\t\t", saltGro)
print("Baking Powder\t", baPowderGro)
print("Espresso Powder\t", espPowderGro)
print("Sugar\t\t", sugarGro)
print("Flour\t\t", flourGro)
print("Chocolate Chip\t", chocoChipGro)
print("Butter\t\t", butterGro)
print("Vanilla\t\t", vanillaGro)
print("Egg\t\t", eggGro)
print()
print("Total price $\t", format(totalPrice, ".2f"))


# Summary Report

# Using the method you taught during the zoom session, I break down the basic calculation on paper. Especially during the conversion from gr to oz.
# Once I figured the conversion math on paper, I then went back and look at the constant I created earlier, and replace the math with the constant.

# For testing, I did a couple of test case for 9 batches and 10 batches and 11 batches. I did the manual calculation on paper and compare the result.
# I didn't encounter any problem. I feel like since the math calculation was done on paper, I was able to replace formulas with constants in my
# program. It went smooth, and I didn't have errors. It just took me longer because of all the manual calculation. I think I traded the errors
# with the time I spend doing the calculations.

# I learned about using variables in conjunction with formating. Not sure what other format I will learn in the future, but I found putting a nice
# and neat result is very satisfying. 
