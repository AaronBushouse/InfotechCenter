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
print("Weather Branch - Developer: Aaron Bushouse")

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
