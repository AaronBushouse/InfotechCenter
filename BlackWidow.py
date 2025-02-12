import random  # For selecting a random weather condition
from time import sleep  # For adding delays in output

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
        print(f"VRS has been engaged allowing us to only drive a maximum of {speed}MPH.")
    else:
        print(f"\nThe National Weather Service is calling for {weather_condition} skies! Enjoy it!")
        sleep(1)
        print("VRS has been disengaged. Drive safely.")

# Generate a weather condition and process the response
weather_condition = weather()
vehicleResponseSystem(weather_condition)
