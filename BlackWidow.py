# Importing required libraries
import sys  # For controlling the output stream (such as writing to the console)
import time  # For adding delays (e.g., time.sleep())

# Print initial welcome message with developer info
print("Welcome Branch - Developer: Aaron Bushouse")

# Print version information for the system
print("\nWelcome to InfoTechCenter V1.0")

# Initialize variables
x = 0  # Counter for the while loop
ellipsis = 0  # Counter for the number of dots in the message

# Loop that runs until 'x' reaches 20
while x != 20:
    x += 1  # Increment the counter 'x' by 1 each time
    message = ("Infotech Center System Booting" + "." * ellipsis)  # Create a message with dots increasing each loop
    ellipsis += 1  # Increase the number of dots (ellipsis) each time
    sys.stdout.write("\r" + message)  # Write the message to the same line of the console, overwriting the previous one
    time.sleep(.55)  # Pause for 0.55 seconds between each update of the message
    
    # Reset ellipsis to 0 after 4 dots to keep the message clean
    if ellipsis == 4:
        ellipsis = 0
    
    # Once 'x' reaches 20, print a final message indicating the system has booted up
    if x == 20:
        print("\n\nOperating System Booting up - Retina Scanned - Access Granted")
