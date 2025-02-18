import random
from time import sleep

print("\n***************************************************\n")
print("Gasoline Branch - Developer: Aaron Bushouse\n")

def gas_level_gauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])

def gas_station():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees"])

def gas_level_alert():
    gas_level = gas_level_gauge()
    station = gas_station()
    
    # Define distance ranges based on gas level
    distance_ranges = {
        "Empty": (0.1, 5),
        "Low": (0.1, 25),
        "Quarter Tank": (25.001, 50)
    }
    
    print(f"Your gas level: {gas_level}")

    if gas_level == "Empty":
        miles_aaa = round(random.uniform(*distance_ranges["Empty"]), 1)
        print("***** WARNING - YOU ARE OUT OF GAS *****\n")
        sleep(1.2)
        print("Calling AAA...")
        sleep(2)
        print(f"AAA is {miles_aaa} miles away from you. Sit tight!")
    
    elif gas_level in distance_ranges:
        miles_to_station = round(random.uniform(*distance_ranges[gas_level]), 1)
        print(f"Your gas tank is {gas_level.lower()}, checking GPS for the closest gas station.")
        sleep(1.2)
        print(f"The closest gas station is {station}, which is {miles_to_station} miles away.")
    
    else:
        print("You have plenty of gas to reach your destination. Drive safely!")

gas_level_alert()
