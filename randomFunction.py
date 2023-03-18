import random

def randomKZ(placeKz):
    masEvents = ["трехфазное", "однофазное", 
                 "двухфазное КЗ"]
    if (placeKz == "TR1" or placeKz == "TR2"):
        return "витковое замыкание в Т"
    else:
        return random.choice(masEvents)

def levelKzCurrent(myEvents):
    if myEvents == "двухфазное КЗ":
        return random.randint(0, 700)
    elif myEvents == "трехфазное":
        return random.randint(701, 1000)
    elif myEvents == "однофазное":
        return random.randint(0, 1000)
    elif myEvents ==  "витковое замыкание в Т":
        return random.randint(0, 1000)

def FixOrNoFixKzVl():
    return random.randint(0,100)

def breakProtection():
    return random.randint(0, 100)

def randomPlaceKz():
    placeKz = ["W1", "W2", "W3", "W4", "TR1", "TR2", "Bus1", 
               "Bus2", "Bus3", "between bus2 and bus3"]
    return random.choice(placeKz)
            
