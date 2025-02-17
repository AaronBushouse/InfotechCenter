print("\n***************************************************\n")
print("Gasoline Branch - Developer: Aaron Bushouse\n")
 
import random
from time import sleep
 
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)
 
def gasStations():
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees"]
    return random.choice(gasStationsList)
 
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(.1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.001,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("*****WARNING - YOU ARE OUT OF GAS*****\n")
        sleep(1.225)
        print("calling AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is really low, checking GPS for closest gas station")
        sleep(1.225)
        print("the closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quater tank, checking GPS for closest gas station")
        sleep(1.225)
        print("the closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away")
        
gasLevelAlert()