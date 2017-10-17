from items import *
from map import rooms
from math import *

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]

attributes = {
    "Strength": 5,
    "Intelligence": 5,
    "Charisma": 4,
    "Endurance": 3,
    "Agility": 3,
    "Luck": 2,
    "Faith": 0,
    "Dexterity": 2
}

def getCarryCapacity():
    return ceil(attributes["Strength"] / 2)

def getInventoryMassTotal():
    total = 0
    for item in inventory:
        total += float(item["mass"])
    return total
    
def isOverencumbered():
    if(getInventoryMassTotal() > getCarryCapacity()):
        return True
    else:
        return False
        
def wouldBeOverencumbered(item):
    if(getInventoryMassTotal() + float(item["mass"]) > getCarryCapacity()):
        return True
    else:
        return False