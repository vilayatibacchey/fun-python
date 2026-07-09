#---Planning and System Design---#

# What system am I trying to make?
    # A simple dice game that adds rolls to a total

# How to make the dice game:
    # Ask the user how dice they wish to roll   
    # Check if the number is negative or zero
    # If so:
        # Print a warning to the user to enter a valid number
    # If not:
        # Loop the number of times the user requested
            # Roll a dice (generate a random number betewen 1 and 6)
            # Print the dice number (iteration) and the roll (random number) for each dice
        # Print the total sum of the dice rolls
        # Add the total to the list
        # Print the high score (highest value in the list of the totals or the highest in a database) 
        # Ask to continue or not
        # If not:
            # Save the high score
            # Terminate

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#---Main Code---#

# Importing modules to get random numbers and make database
import random
import sqlite3

# Defining a class for reusability
class Dice:
    
    # Initialization method
    def __init__(self) -> None:
        
        # Create the highscore database
        connection : sqlite3.Connection = sqlite3.connect("game.db")
        cursor : sqlite3.Cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS HighScore (
                       high_score int NOT NULL
                       );''')
        
        # Save changes in the database
        connection.commit()

        # Safely close the connection
        connection.close()

        # Defining the list of sums beforehand
        self.totals : list = []

    # Returns a normal string when printed
    def __str__(self) -> str:
        return "Dice"

    # Validates user input
    def validate(self, roll_times : str) -> bool:

        # Validating user input
        try:
            times : int = int(roll_times)
        except ValueError:
            print("Type an integer!")
            return False

        if times <= 0:
            print("Invalid number, try again.")
            return False
        
        # Returns true as we know the user input passed all tests
        return True

    # Rolls the dice/dices and displays stats
    def roll(self, roll_times : int) -> None:

        # Defining the sum of dice rolls beforehand
        total_sum : int = 0

        # Rolling the dice n times
        for i in range(roll_times):

            # Getting the dice roll
            dice_roll : int = random.randint(1, 6)

            # Adding the roll to the total sum
            total_sum += dice_roll

            # Prints the dice number and roll value
            print(f"Dice {i + 1}: {dice_roll}")

        # Print the total sum
        print(f"Total sum of dice rolls: {total_sum}")

        # Add the sum to the list of totals
        self.totals.append(total_sum)
        
        # Access the database
        connection : sqlite3.Connection = sqlite3.connect("game.db")
        cursor : sqlite3.Cursor = connection.cursor()

        # Get the all-time high score
        cursor.execute("SELECT MAX(high_score) FROM HighScore;")
        result : tuple = cursor.fetchone()

        # Checks if the database is empty
        if result and result[0] is not None:

            # Check if a new high score has beaten the old one
            current_high_score : int = result[0]

            if max(self.totals) > current_high_score:
                print(f"All-Time High Score: {max(self.totals)}")
            else:
                print(f"All-Time High Score: {current_high_score}")

        else:
            # Print the high score
            print(f"High score: {max(self.totals)}")

        # Close the connection safely
        connection.close()

    # Saves changes to the database
    def save_changes(self):

        # Fail-safe check to prevent crashes if save is called with an empty list
        if not self.totals:
            return
        
        # Get the local high score
        high_score : int = max(self.totals)

        # Get the connection and cursor of the database
        connection : sqlite3.Connection = sqlite3.connect("game.db")
        cursor : sqlite3.Cursor = connection.cursor()

        # Insert the new highscore and save the changes
        cursor.execute("INSERT INTO HighScore (high_score) VALUES (?);", (high_score,))
        connection.commit()

        # Safely close the database
        connection.close()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#---Main Program---#

if __name__ == "__main__":

    # Creates a new dice object
    dice : Dice = Dice()

    # Main game loop
    while True:

        # Gets user input
        rolls_times : str = input("How many dice do you wish to roll?")

        # Validates user input
        if not dice.validate(rolls_times):
            continue
        else:
            # Rolls the dices and displays stats
            dice.roll(int(rolls_times))

        # Choice to continue
        user_choice : str = input("Would you like to continue? (y/n) ").strip().lower()
        if user_choice == "n":
            print("Thanks for playing!")
            dice.save_changes()
            break