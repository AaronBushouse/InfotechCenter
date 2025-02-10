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
    
vehicleResponseSystem()