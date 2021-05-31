# Jolly Village Set Encounters
# First Script

import random

DEFINE = 1

BASE1 = (random.randrange(1, 4))
if BASE1 == 1: NAME = "Craytal-C"
if BASE1 == 1: BASEHP = 76
if BASE1 == 1: BASEENRG = 74
if BASE1 == 1: BASEMATK = 34
if BASE1 == 1: BASEMDEF = 43
if BASE1 == 1: BASERATK = 76
if BASE1 == 1: BASERDEF = 43
if BASE1 == 1: BASESPD = 62
if BASE1 == 1: ABILITY1 = 1
if BASE1 == 2: NAME = "Kleptyke"
if BASE1 == 2: BASEHP = 55
if BASE1 == 2: BASEENRG = 48
if BASE1 == 2: BASEMATK = 50
if BASE1 == 2: BASEMDEF = 40
if BASE1 == 2: BASERATK = 20
if BASE1 == 2: BASERDEF = 30
if BASE1 == 2: BASESPD = 95
if BASE1 == 2: ABILITY1 = 2
if BASE1 == 3: NAME = "Kabunga"
if BASE1 == 3: BASEHP = 52
if BASE1 == 3: BASEENRG = 53
if BASE1 == 3: BASEMATK = 76
if BASE1 == 3: BASEMDEF = 43
if BASE1 == 3: BASERATK = 64
if BASE1 == 3: BASERDEF = 34
if BASE1 == 3: BASESPD = 86
if BASE1 == 3: ABILITY1 = 3
HPUP = (random.randrange(0, 41))
ENRGUP = (random.randrange(0, 41))
MATKUP = (random.randrange(0, 41))
MDEFUP = (random.randrange(0, 41))
RATKUP = (random.randrange(0, 41))
RDEFUP = (random.randrange(0, 41))
SPDUP = (random.randrange(0, 41))
HPTP = 0
ENRGTP = 0
MATKTP = 0
MDEFTP = 0
RATKTP = 0
RDEFTP = 0
SPDTP = 0
LEVEL = (random.randrange(15, 21))
GENDER1 = (random.randrange(1, 3))
if GENDER1 == 1: GENDER = "Male"
if GENDER1 == 2: GENDER = "Female"
NATURE1 = (random.randrange(0, 43))
if ABILITY1 == 1: ABILITY_1 = (random.randrange(1, 257))
else: ABILITY_1 = 257
if ABILITY_1 < 256: ABILITY01 = (random.randrange(1,3))
if ABILITY_1 == 257: ABILITY01 = 3
if ABILITY1 == 2: ABILITY_2 = (random.randrange(1, 257))
else: ABILITY_2 = 257
if ABILITY_2 < 256: ABILITY02 = (random.randrange(1,3))
if ABILITY_2 == 257: ABILITY02 = 3
if ABILITY1 == 3: ABILITY_3 = (random.randrange(1, 257))
else: ABILITY_3 = 257
if ABILITY_3 < 256: ABILITY03 = (random.randrange(1,3))
if ABILITY_3 == 257: ABILITY03 = 3

if NATURE1 == 0: NATURE = "Indifferent"
if NATURE1 == 1: NATURE = "Hyper"
if NATURE1 == 2: NATURE = "Brawny"
if NATURE1 == 3: NATURE = "Robust"
if NATURE1 == 4: NATURE = "Smart"
if NATURE1 == 5: NATURE = "Clever"
if NATURE1 == 6: NATURE = "Nimble"
if NATURE1 == 7: NATURE = "Dull"
if NATURE1 == 8: NATURE = "Frail"
if NATURE1 == 9: NATURE = "Tender"
if NATURE1 == 10: NATURE = "Clumsy"
if NATURE1 == 11: NATURE = "Foolish"
if NATURE1 == 12: NATURE = "Sluggish"
if NATURE1 == 13: NATURE = "Hyper, Frail"
if NATURE1 == 14: NATURE = "Hyper, Tender"
if NATURE1 == 15: NATURE = "Hyper, Clumsy"
if NATURE1 == 16: NATURE = "Hyper, Foolish"
if NATURE1 == 17: NATURE = "Hyper, Sluggish"
if NATURE1 == 18: NATURE = "Brawny, Dull"
if NATURE1 == 19: NATURE = "Brawny, Tender"
if NATURE1 == 20: NATURE = "Brawny, Clumsy"
if NATURE1 == 21: NATURE = "Brawny, Foolish"
if NATURE1 == 22: NATURE = "Brawny, Sluggish"
if NATURE1 == 23: NATURE = "Robust, Dull"
if NATURE1 == 24: NATURE = "Robust, Frail"
if NATURE1 == 25: NATURE = "Robust, Clumsy"
if NATURE1 == 26: NATURE = "Robust, Foolish"
if NATURE1 == 27: NATURE = "Robust, Sluggish"
if NATURE1 == 28: NATURE = "Smart, Dull"
if NATURE1 == 29: NATURE = "Smart, Frail"
if NATURE1 == 30: NATURE = "Smart, Tender"
if NATURE1 == 31: NATURE = "Smart, Foolish"
if NATURE1 == 32: NATURE = "Smart, Sluggish"
if NATURE1 == 33: NATURE = "Clever, Dull"
if NATURE1 == 34: NATURE = "Clever, Frail"
if NATURE1 == 35: NATURE = "Clever, Tender"
if NATURE1 == 36: NATURE = "Clever, Clumsy"
if NATURE1 == 37: NATURE = "Clever, Sluggish"
if NATURE1 == 38: NATURE = "Nimble, Dull"
if NATURE1 == 39: NATURE = "Nimble, Frail"
if NATURE1 == 40: NATURE = "Nimble, Tender"
if NATURE1 == 41: NATURE = "Nimble, Clumsy"
if NATURE1 == 42: NATURE = "Nimble, Foolish"

if NATURE1 == 1: ENRGNATURE = 1.1
elif NATURE1 == 7: ENRGNATURE = 0.9
elif NATURE1 == 13: ENRGNATURE = 1.1
elif NATURE1 == 14: ENRGNATURE = 1.1
elif NATURE1 == 15: ENRGNATURE = 1.1
elif NATURE1 == 16: ENRGNATURE = 1.1
elif NATURE1 == 17: ENRGNATURE = 1.1
elif NATURE1 == 18: ENRGNATURE = 0.9
elif NATURE1 == 23: ENRGNATURE = 0.9
elif NATURE1 == 28: ENRGNATURE = 0.9
elif NATURE1 == 33: ENRGNATURE = 0.9
elif NATURE1 == 38: ENRGNATURE = 0.9
else: ENRGNATURE = 1

if NATURE1 == 2: MATKNATURE = 1.1
elif NATURE1 == 8: MATKNATURE = 0.9
elif NATURE1 == 13: MATKNATURE = 0.9
elif NATURE1 == 18: MATKNATURE = 1.1
elif NATURE1 == 19: MATKNATURE = 1.1
elif NATURE1 == 20: MATKNATURE = 1.1
elif NATURE1 == 21: MATKNATURE = 1.1
elif NATURE1 == 22: MATKNATURE = 1.1
elif NATURE1 == 24: MATKNATURE = 0.9
elif NATURE1 == 29: MATKNATURE = 0.9
elif NATURE1 == 34: MATKNATURE = 0.9
elif NATURE1 == 39: MATKNATURE = 0.9
else: MATKNATURE = 1

if NATURE1 == 3: MDEFNATURE = 1.1
elif NATURE1 == 9: MDEFNATURE = 0.9
elif NATURE1 == 14: MDEFNATURE = 0.9
elif NATURE1 == 19: MDEFNATURE = 0.9
elif NATURE1 == 23: MDEFNATURE = 1.1
elif NATURE1 == 24: MDEFNATURE = 1.1
elif NATURE1 == 25: MDEFNATURE = 1.1
elif NATURE1 == 26: MDEFNATURE = 1.1
elif NATURE1 == 27: MDEFNATURE = 1.1
elif NATURE1 == 30: MDEFNATURE = 0.9
elif NATURE1 == 35: MDEFNATURE = 0.9
elif NATURE1 == 40: MDEFNATURE = 0.9
else: MDEFNATURE = 1

if NATURE1 == 4: RATKNATURE = 1.1
elif NATURE1 == 10: RATKNATURE = 0.9
elif NATURE1 == 15: RATKNATURE = 0.9
elif NATURE1 == 20: RATKNATURE = 0.9
elif NATURE1 == 25: RATKNATURE = 0.9
elif NATURE1 == 28: RATKNATURE = 1.1
elif NATURE1 == 29: RATKNATURE = 1.1
elif NATURE1 == 30: RATKNATURE = 1.1
elif NATURE1 == 31: RATKNATURE = 1.1
elif NATURE1 == 32: RATKNATURE = 1.1
elif NATURE1 == 36: RATKNATURE = 0.9
elif NATURE1 == 41: RATKNATURE = 0.9
else: RATKNATURE = 1

if NATURE1 == 5: RDEFNATURE = 1.1
elif NATURE1 == 11: RDEFNATURE = 1.1
elif NATURE1 == 16: RDEFNATURE = 1.1
elif NATURE1 == 21: RDEFNATURE = 1.1
elif NATURE1 == 26: RDEFNATURE = 1.1
elif NATURE1 == 31: RDEFNATURE = 1.1
elif NATURE1 == 33: RDEFNATURE = 0.9
elif NATURE1 == 34: RDEFNATURE = 0.9
elif NATURE1 == 35: RDEFNATURE = 0.9
elif NATURE1 == 36: RDEFNATURE = 0.9
elif NATURE1 == 37: RDEFNATURE = 0.9
elif NATURE1 == 42: RDEFNATURE = 1.1
else: RDEFNATURE = 1

if NATURE1 == 6: SPDNATURE = 1.1
elif NATURE1 == 12: SPDNATURE = 0.9
elif NATURE1 == 17: SPDNATURE = 0.9
elif NATURE1 == 22: SPDNATURE = 0.9
elif NATURE1 == 27: SPDNATURE = 0.9
elif NATURE1 == 32: SPDNATURE = 0.9
elif NATURE1 == 37: SPDNATURE = 0.9
elif NATURE1 == 38: SPDNATURE = 1.1
elif NATURE1 == 39: SPDNATURE = 1.1
elif NATURE1 == 40: SPDNATURE = 1.1
elif NATURE1 == 41: SPDNATURE = 1.1
elif NATURE1 == 42: SPDNATURE = 1.1
else: SPDNATURE = 1

ICIGOOL = (random.randrange(1,91))
if ICIGOOL == 90: GENDER = "None"
if ICIGOOL == 90: ABILITY = "Parting Gift"
if ICIGOOL == 90: BASEHP = 95
if ICIGOOL == 90: BASEENRG = 69
if ICIGOOL == 90: BASEMATK = 112
if ICIGOOL == 90: BASEMDEF = 94
if ICIGOOL == 90: BASERATK = 10
if ICIGOOL == 90: BASERDEF = 81
if ICIGOOL == 90: BASESPD = 39
if ICIGOOL == 90: ICICOLOR1 = (random.randrange(1,21))
else: ICICOLOR1 = 0
if ICICOLOR1 == 1: ICICOLOR = (random.randrange(1,5))
if ICICOLOR1 == 2: ICICOLOR = (random.randrange(1,5))
if ICICOLOR1 == 3: ICICOLOR = (random.randrange(1,5))
elif ICICOLOR1 > 3: ICICOLOR = 5
else: ICICOLOR = 0
if ICICOLOR == 5: NAME = "Icigool"
elif ICICOLOR == 1: NAME = "Icigool (Indigo)"
elif ICICOLOR == 2: NAME = "Icigool (Pink)"
elif ICICOLOR == 3: NAME = "Icigool (Black)"
elif ICICOLOR == 4: NAME = "Icigool (White)"

ABILITYZ = 0
ABILITYS = 0
PYRAMIND = (random.randrange(1,301))
if PYRAMIND == 300: NAME = "Pyramind"
if PYRAMIND == 300: GENDER = "None"
if PYRAMIND == 300: ABILITYZ = (random.randrange(1,257))
if ABILITYZ == 256: ABILITY = "Contact Curse"
else: DEFINE = 0
if PYRAMIND == 300: ABILITY01 = 0
if PYRAMIND == 300: ABILITY02 = 0 
if PYRAMIND == 300: ABILITY03 = 0
if PYRAMIND == 300: ABILITY_1 = 0
if PYRAMIND == 300: ABILITY_2 = 0
if PYRAMIND == 300: ABILITY_3 = 0 
if DEFINE == 0: ABILITYS + (random.randrange(1,3))
if ABILITYS == 1: ABILITY = "Temper"
if ABILITYS == 2: ABILITY = "Idiosyncratic"
if PYRAMIND == 300: BASEHP = 88
if PYRAMIND == 300: BASEENRG = 60
if PYRAMIND == 300: BASEMATK = 45
if PYRAMIND == 300: BASEMDEF = 69
if PYRAMIND == 300: BASERATK = 84
if PYRAMIND == 300: BASERDEF = 99
if PYRAMIND == 300: BASESPD = 35

HP = str(int((BASEHP*2+HPUP+HPTP/4)*LEVEL/100+LEVEL+10))
ENRG = str(int(((BASEENRG*2+ENRGUP+ENRGTP/4)*LEVEL/65+80)*ENRGNATURE))
MATK = str(int(((BASEMATK*2+RDEFUP+MATKTP/4)*LEVEL/100+5)*MATKNATURE))
MDEF = str(int(((BASEMDEF*2+MDEFUP+MDEFTP/4)*LEVEL/100+5)*MDEFNATURE))
RATK = str(int(((BASERATK*2+RATKUP+RATKTP/4)*LEVEL/100+5)*RATKNATURE))
RDEF = str(int(((BASERDEF*2+RDEFUP+RDEFTP/4)*LEVEL/100+5)*RDEFNATURE))
SPD = str(int(((BASESPD*2+SPDUP+SPDTP/4)*LEVEL/100+5)*SPDNATURE))

GLEAM = (random.randrange(1, 129))
GAMMA = (random.randrange(1, 641))
CORRUPT = (random.randrange(1, 126))
if CORRUPT == 125: GLEAM = 129
if CORRUPT == 125: GAMMA = 641
if GAMMA == 640: GLEAM = 129

x = str(LEVEL)
a = str(HPUP)
b = str(ENRGUP)
c = str(MATKUP)
d = str(MDEFUP)
e = str(RATKUP)
f = str(RDEFUP)
g = str(SPDUP)

print("Name = " + NAME)
print("Gender = " + GENDER)
print("Level = " + x)

print()
if ABILITY01 == 1: print("Ability = Parting Gift")
if ABILITY01 == 2: print("Ability = Chill")
if ABILITY_1 == 256: print ("Ability = Regift ☆")
if ABILITY02 == 1: print("Ability = Apprehension")
if ABILITY02 == 2: print("Ability = Burglar")
if ABILITY_2 == 256: print("Ability = Ability Thief ☆")
if ABILITY03 == 1: print("Ability = Territorial")
if ABILITY03 == 2: print("Ability = Communication")
if ABILITY_3 == 256: print("Ability = Noxious Weeds ☆")

print()
print("Personality = " + NATURE)
print()
print("HP: " + HP)
print("Energy: " + ENRG)
print("Melee Attack: " + MATK)
print("Melee Defense: " + MDEF)
print("Ranged Attack: " + RATK)
print("Ranged Defense: " + RDEF)
print("Speed: " + SPD)

print()
print("Health UP = " + a)
print("Energy UP = " + b)
print("Melee Attack UP = " + c)
print("Melee Defense UP = " + d)
print("Ranged Attack UP = " + e)
print("Ranged Defense UP = " + f)
print("Speed UP = " + g)

print()
if GLEAM == 128: print("Is Alpha Gleaming!") 
if CORRUPT == 125: print("Is Corrupted!")
if GAMMA == 640: print("Is Gamma Gleaming!")
