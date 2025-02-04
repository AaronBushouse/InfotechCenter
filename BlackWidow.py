# Import required libraries
import sys  # For controlling the output stream (writing to the console)
import time  # For adding delays (e.g., time.sleep())

# ANSI escape sequences for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"  # Resets text to default color

# Display initial welcome message with developer information
print(f"{GREEN}Welcome Branch - Developer: Aaron Bushouse{RESET}")

# Display system version information
print(f"\n{CYAN}Welcome to InfoTechCenter V1.0{RESET}")

# Initialize counters
x = 0  # Controls the number of iterations for the boot-up animation
ellipsis = 0  # Determines the number of dots displayed in the boot-up message

# Loop to simulate system boot-up progress
while x < 20:
    x += 1  # Increment iteration counter
    message = f"{YELLOW}Infotech Center System Booting{'.' * ellipsis}{RESET}"  # Yellow text for boot-up message
    ellipsis = (ellipsis + 1) % 4  # Cycle through 0 to 3 dots for a smooth animation effect

    sys.stdout.write("\r" + message)  # Overwrite previous output in the console for a dynamic effect
    sys.stdout.flush()  # Ensure immediate display of the message
    time.sleep(0.55)  # Pause for 0.55 seconds before the next update

# Display final message after the boot-up sequence completes
print(f"\n\n{BLUE}Operating System Booting up - Retina Scanned - Access Granted{RESET}")