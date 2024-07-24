#
# CGS 2060 – Spring Semester 2024
#
# CGS 2060 Homework #4 – Time For Roulette
#
# (Dennys Bach)
#

# Import required libraries
import random

#
# Function Name: printWheel
#
# Description: Prints out the numbers on the Roulette
# wheel in correct order and the color associated with
# each number
#
# Inputs:
#    rWheel: roulette wheel numbers
#    wheelColors: red/black colors for each number
#

# Roulette wheel numbers and colors
rWheel = [i for i in range(0, 38)]  # 0-36 numbers plus 00
wheelColors = ['Green' if x == 0 or x == 37 else 'Red' if x % 2 == 0 else 'Black' for x in rWheel]

# Function to print the roulette wheel
def printWheel(rWheel, wheelColors):
    print("Roulette Wheel:\n")
    location1 = 0
    location2 = 0
    for index1 in range(1, 4):
        for index2 in range(1, 14):
            print("{0:3d}".format(rWheel[location1]), end="")
            location1 += 1
            if (index1 == 3) and (index2 == 12):
                break
        print()
        for index2 in range(1, 14):
            print(wheelColors[location2].rjust(3), end="")
            location2 += 1
            if (index1 == 3) and (index2 == 12):
                break
        print()
    print()

#
# Function Name: spinWheel
#
# Description: Starting at the current location, the Roulette wheel is
# spun and it randomly ends up at a new location on the wheel. The number 
# on the wheel at this new location is then returned to the calling 
# routine.
#
# Inputs:
#    rWheel: roulette wheel numbers
#    location: the number currently being pointed to by the Roulette wheel 
#
# Output:
#    The value that the Roulette wheel ends up pointing to
#

def spinWheel(rWheel, location):
    # How many total times does the wheel spin?
    numRotations = random.randint(5, 10)
    # How many numbers are passed on the final spin?
    numSteps = random.randint(1, 38)
    # Calculate the total number of Roulette pockets passed
    totalPockets = (numRotations * 38) + numSteps

    for index in range(totalPockets):
        # Move to the next pocket
        location += 1
        # If the wheel has completed a full rotation, point to the first pocket
        if location > 37:
            location = 0

    return rWheel[location]

#
# Function Name: straightBet
#
# Function Description: This function is called when the player is
# placing a straight bet. It will calcuate and return the number to be
# bet on.
#
# Inputs:
#    rWheel: roulette wheel numbers
#
# Output:
#    Roulette pocket number to be bet on

def straightBet(rWheel):
    return random.choice(rWheel)


#
# Function Name: colorBet
#
# Function Description: This function is called when the player is
# placing a color bet. It will calcuate and return the color to be
# bet on.
#
# Inputs:
#    None
#
# Output:
#    Either "Black" or "Red"

def colorBet():
    return random.choice(wheelColors)

#
# Function Name: oddEvenBet
#
# Function Description: This function is called when the player is
# placing an Odd/Even bet. It will calcuate and return if the bet is to
# be either "Odd" or "Even".
#
# Inputs:
#    None
#
# Output:
#    Either "Even" or "Odd"

def oddEvenBet():
    return random.choice(['Odd', 'Even'])

#
# Function Name: lowHighBet
#
# Function Description: This function is called when the player is
# placing an Low/High bet. It will calcuate and return if the bet is to
# be either "Low" or "High".
#
# Inputs:
#    None
#
# Output:
#    Either "Low" or "High"

def lowHighBet():
    return random.choice(['Low', 'High'])





# Main game loop
def playRoulette():
    currentLocation = random.randint(0, 37)
    spinCount = 0
    winCount = 0
    totalMoney = 0
    totalWon = 0  # Initialize a counter for the total money won
    # Initialize counters for the amount of money won for each type of bet
    totalWonStraight = 0
    totalWonColor = 0
    totalWonOddEven = 0
    totalWonLowHigh = 0
    for i in range(500):  # Spin the wheel 500 times
        betMoney = random.randint(1, 100)  # Randomly choose a money bet value
        totalMoney += betMoney
        choice = str(random.randint(1, 4))  # Randomly choose a bet type
        if choice == '1':
            betNumber = straightBet(rWheel)
            print(f"Placing a straight bet on number: {betNumber}")
        elif choice == '2':
            betColor = colorBet()
            print(f"Placing a bet on color: {betColor}")
        elif choice == '3':
            betOddEven = oddEvenBet()
            print(f"Placing a bet on: {betOddEven}")
        elif choice == '4':
            betLowHigh = lowHighBet()
            print(f"Placing a bet on: {betLowHigh}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue
        winningNumber = spinWheel(rWheel, currentLocation)
        spinCount += 1  # Increment the spin counter each time the wheel is spun
        print(f"The wheel stopped at number: {winningNumber}")
        if choice == '1':
            if betNumber == winningNumber:
                print("Congratulations! You won!")
                winCount += 1
                winnings = betMoney * 35  # In roulette, a straight bet pays 35 to 1
                totalWon += winnings
                totalWonStraight += winnings
            else:
                print("Better luck next time!")
        elif choice == '2':
            if betColor == wheelColors[winningNumber]:
                winCount += 1
                winnings = betMoney * 2  # In roulette, a color bet pays 2 to 1
                totalWon += winnings
                totalWonColor += winnings
                print("Congratulations! You won!")
            else:
                print("Better luck next time!")
        elif choice == '3':
            if (betOddEven == 'Odd' and winningNumber % 2 == 1) or (betOddEven == 'Even' and winningNumber % 2 == 0):
                print("Congratulations! You won!")
                winCount += 1
                winnings = betMoney * 2  # In roulette, an odd/even bet pays 2 to 1
                totalWon += winnings
                totalWonOddEven += winnings
            else:
                print("Better luck next time!")
        elif choice == '4':
            if (betLowHigh == 'Low' and winningNumber < 19) or (betLowHigh == 'High' and winningNumber >= 19):
                print("Congratulations! You won!")
                winCount += 1
                winnings = betMoney * 2  # In roulette, a low/high bet pays 2 to 1
                totalWon += winnings
                totalWonLowHigh += winnings
            else:
                print("Better luck next time!")
    print("")
    print("-----Results-----")
    print(f"The player won {winCount} times.")
    print(f"The total money bet was ${totalMoney:,}.")  # Print the total money bet
    print(f"The total money won was ${totalWon:,}.")  # Print the total money won
    # After the game ends, compare the total money won for each type of bet
    maxWon = max(totalWonStraight, totalWonColor, totalWonOddEven, totalWonLowHigh)
    if maxWon == totalWonStraight:
        print("The straight bet made the most money.")
    elif maxWon == totalWonColor:
        print("The color bet made the most money.")
    elif maxWon == totalWonOddEven:
        print("The odd/even bet made the most money.")
    else:  # maxWon == totalWonLowHigh
        print("The low/high bet made the most money.")
# Start the game
playRoulette()