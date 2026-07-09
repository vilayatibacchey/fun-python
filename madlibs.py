# Create the game class for reusability
class Madlibs:
    def ask(self):
        # Get the player's options
        noun = input("Type any noun you like: ")
        verb = input("Type any verb you like: ")
        adjective = input("Type any adjective you like: ")
        adverb = input("Type any adverb you like: ")
        return noun, verb, adjective, adverb

    def write_story(self, noun, verb, adjective, adverb):
        # Removed the large indentation spaces inside the triple quotes
        print(f"\nOnce upon a time, there was a {noun} who liked to {verb} "
              f"very {adverb}. It was a {adjective} day, and the {noun} was feeling {adverb}.\n"
              f"The {noun} soon found a {adjective} treasure, and lived a happy life!\n")
        
    def game_loop(self):
        # Loop
        while True:
            # Ask the user
            noun, verb, adjective, adverb = self.ask()

            # Make the story
            self.write_story(noun, verb, adjective, adverb)

            # Ask to continue (Fixed indentation here)
            user_choice = input("Continue? (y/n): ").strip().lower()
            
            # If not, terminate
            if user_choice == "n":
                print("Thanks for playing!")
                break

# Main Program
if __name__ == "__main__":
    new_madlibs = Madlibs()
    new_madlibs.game_loop()
