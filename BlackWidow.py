# Import required libraries
import sys  # For controlling the output stream (writing to the console)
import time  # For adding delays (e.g., time.sleep())
import random  # For selecting a random weather condition
from time import sleep  # For adding delays in output

# ANSI escape sequences for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"  # Resets text to default color

# Display initial welcome message with developer information
print("Welcome Branch - Developer: Aaron Bushouse")

# Display system version information
print(f"\n{CYAN}Welcome to InfoTechCenter V1.0{RESET}\n")

# Initialize counters
x = 0  # Controls the number of iterations for the boot-up animation
ellipsis = 0  # Determines the number of dots displayed in the boot-up message

# Loop to simulate system boot-up progress
while x < 20:
    x += 1  # Increment iteration counter
    message = f"{GREEN}Infotech Center System Booting{'.' * ellipsis}{RESET}"  # Yellow text for boot-up message
    ellipsis = (ellipsis + 1) % 4  # Cycle through 0 to 3 dots for a smooth animation effect

    sys.stdout.write("\r" + message)  # Overwrite previous output in the console for a dynamic effect
    sys.stdout.flush()  # Ensure immediate display of the message
    time.sleep(0.55)  # Pause for 0.55 seconds before the next update

# Display final message after the boot-up sequence completes
print(f"\n\n{RED}Operating System Booting up - Retina Scanned - Access Granted{RESET}")

# Print program header
print("\n******************************************\n")
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

print("\n******************************************\n")
print("Weather Branch - Developer: Aaron Bushouse")

def weather():
    """Randomly selects a weather condition."""
    return random.choice(["snowing", "blizzard", "icy", "rainy", "windy", "sunny"])

def vehicleResponseSystem(weather_condition):
    """Determines the vehicle response based on weather conditions using a dictionary."""
    response_data = {
        "snowing": (30, 55),
        "blizzard": (60, 25),
        "icy": (90, 25),
        "rainy": (10, 45),
        "windy": (5, 75)
    }

    if weather_condition in response_data:
        delay, speed = response_data[weather_condition]
        print(f"\nThe National Weather Service has updated our alarm by {delay} minutes because it is {weather_condition}.")
        sleep(1)
        print(f"VRS has been engaged allowing us to only drive {speed}MPH.")
    else:
        print(f"\nThe National Weather Service is calling for {weather_condition} skies! Enjoy it!")
        sleep(1)
        print("VRS has been disengaged. Drive safely.")

# Generate a weather condition and process the response
weather_condition = weather()
vehicleResponseSystem(weather_condition)



