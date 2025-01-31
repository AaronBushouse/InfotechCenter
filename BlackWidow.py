#Libraries HERE
import sys
import time

print("Welcome Branch - Developer: Aaron Bushouse")

print("\nWelcome to InfoTechCenter V1.0")

x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message)
    time.sleep(.55)
    if ellipsis == 4:
        ellipsis= 0
    if x == 20:
        print("\nOperating System Booting up - Retina Scanned - Access Granted")