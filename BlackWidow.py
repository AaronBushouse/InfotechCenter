print("\n******************************************\n")
 
print("Weather Branch - Developer: Aaron Bushouse\n\n\n")
 
#Import Libraries HERE!
import random
from time import sleep
 
# Weather Function to determine the weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\n\nThe National Weather Service has updated our alarm by 30 minutes because"
              " it is", weatherAlert,"\n\n")
    elif weatherAlert == "blizzard":
        print("\n\nThe National Weather Service has updated our alarm by 60 minutes because"
              " it is a", weatherAlert,"!\n\n")
    elif weatherAlert == "icy":
        print("\n\nThe National Weather Service has updated our alarm by 90 minutes because"
              " it is a", weatherAlert,"drive safe!\n\n")
    elif weatherAlert == "rainy":
        print("\n\nThe National Weather Service has updated our alarm by 10 minutes because"
              " it is a", weatherAlert,", possible low visiblity\n\n") 
    elif weatherAlert == "windy":
        print("\n\nThe National Weather Service has updated our alarm by 5 minutes because"
              " it is a", weatherAlert,"\n\n")
    else:
        print("\nThe National Weather Service is calling for",weatherAlert,"skys! Enjoy it!\n\n")
vehicleResponseSystem()