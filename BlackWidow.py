# Print a header to introduce the program
print("\n******************************************\n")
print("Weather Branch - Developer: Aaron Bushouse")

# Import necessary libraries
import random  # For selecting a random weather condition
from time import sleep  # (Not used in this script but imported)

# Function to determine the weather
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    # Randomly choose one weather condition from the list
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition  # Return the chosen weather condition

# Generate a weather condition and store it in weatherAlert
weatherAlert = weather()

# Function to determine vehicle response based on weather conditions
def vehicleResponseSystem():
    # Check the weather condition and update the alarm accordingly
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " it is", weatherAlert,)
        sleep(1)
        print("VRS has been engaged allowing us to only drive 55MPH")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 60 minutes because"
              " it is a", weatherAlert,"!")
        sleep(1)
        print("VRS has been engaged allowing us to only drive 25MPH")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 90 minutes because"
              " it is", weatherAlert,", drive safe!")
        sleep(1)
        print("VRS has been engaged allowing us to only drive 25MPH")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 10 minutes because"
              " it is a", weatherAlert,", possible low visibility")
        sleep(1)
        print("VRS has been engaged allowing us to only drive 45MPH")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " it is a", weatherAlert,)
        sleep(1)
        print("VRS has been engaged allowing us to only drive 75MPH")
    else:
        # Default message for sunny weather
        print("\nThe National Weather Service is calling for",weatherAlert,"skies! Enjoy it!")
        sleep(1)
        print("VRS has been disengaged drive safely")

# Call the function to display the response based on the generated weather
vehicleResponseSystem()
