import random
from time import sleep

# Print program header
print("\n***************************************************\n")
print("Gasoline Branch - Developer: Aaron Bushouse\n")


# Function to randomly determine the current gas level
def gas_level_gauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])


# Function to randomly select a nearby gas station
def gas_station():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees"])


# Function to alert the user about their gas level and find the nearest gas station if needed
def gas_level_alert():
    gas_level = gas_level_gauge()  # Get the current gas level
    station = gas_station()  # Get a random gas station

    # Define distance ranges (in miles) based on gas level
    distance_ranges = {
        "Empty": (0.1, 100),  # If empty, AAA could be far away
        "Low": (0.1, 25),  # Low gas means a nearby station is needed
        "Quarter Tank": (25.001, 50)  # Quarter tank allows a slightly longer trip
    }

    print(f"Your gas level: {gas_level}")

    # Handle different gas levels
    if gas_level == "Empty":
        # If the tank is empty, simulate calling AAA for help
        miles_aaa = round(random.uniform(*distance_ranges["Empty"]), 1)
        print("***** WARNING - YOU ARE OUT OF GAS *****\n")
        sleep(1.2)  # Pause for effect
        print("Calling AAA...")
        sleep(2)  # Simulate waiting for response
        print(f"AAA is {miles_aaa} miles away from you. Sit tight!")

    elif gas_level in distance_ranges:
        # If gas is low or at a quarter tank, find the nearest gas station
        miles_to_station = round(random.uniform(*distance_ranges[gas_level]), 1)
        print(f"Your gas tank is {gas_level.lower()}, checking GPS for the closest gas station.")
        sleep(1.2)  # Simulate GPS processing
        print(f"The closest gas station is {station}, which is {miles_to_station} miles away.")

    else:
        # If the tank is at half, three-quarters, or full, no immediate action is needed
        print("You have plenty of gas to reach your destination. Drive safely!")


# Run the gas level alert function
gas_level_alert()
