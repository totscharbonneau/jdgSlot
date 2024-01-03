# import RPi.GPIO as GPIO
import time
import random

beerPump = 11
swompPump = 13
leverPull = 15

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(beerPump, GPIO.OUT)
# GPIO.setup(swompPump, GPIO.OUT)
# GPIO.setup(leverPull, GPIO.IN)
# GPIO.input(leverPull) # Permet de check le status de la switch.

# Define symbols for the slot machine
symbols = ['Cherry', 'Bell', 'Bar', 'Seven', 'Orange']

def spin_slot_machine():
    # Spin the slot machine
    result = [random.choice(symbols) for _ in range(3)]
    return result

def display_slot_machine(result):
    # Display the result of the spin
    print("Slot Machine Result:")
    for item in result:
        print(item, end=" ")
    print("\n")

def check_winning(result):
    # Check if the player wins based on the result
    if len(set(result)) == 1:
        print("Congratulations! You win!")
    else:
        print("Sorry, you didn't win this time.")

# Simulate the slot machine
def play_slot_machine():
    print("Welcome to the Slot Machine!")
    while True:
        input("Press Enter to spin. Press 'q' to quit.\n")
        
        result = spin_slot_machine()
        display_slot_machine(result)
        check_winning(result)
        
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != 'y':
            break

print(spin_slot_machine())