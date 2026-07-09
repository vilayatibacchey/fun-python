import random

def select_number():
    selected_number = random.randint(1,100)
    return selected_number

print('Welcome!\nTo the number guessing game!')
print('You have to basically guess a number from 1-100 (including the end points).\nIf it matches, you win the round!')

point = 0
turn = 5
round = 0
number = select_number()

while True:
    if round == 5 :
        print('Well done! You have won the game! Congratulations and bye for now.')
        break
    print('There are 5 rounds in the game. Each game you have 5 turns. If you lose, you can try again.')
    guess = input('What number do you guess it is? (Type E to exit.)')
    if guess == 'E' or guess == 'e':
        print('Hope to see you play again soon!')
        break
    elif guess.isdigit():
        guess = int(guess)
        if guess > 100:
            print("Try again. You can't go above 100.")
            if turn > 0:
                turn -= 1
                print('You lost one turn for a penalty. Do better next time.')
            if turn == 0:
                choice = input('You ran out of turns from penalties. Would you like to try again? ')
                if choice in ['Yes', 'yes']:
                    turn = 5
                elif choice in ['No','no']:
                    print('Hope to see you soon!')
                    break
                else:
                    print('Error! Your game is restarted by default.')
                    turn = 5
        elif guess < 1:
            print("Try again. You can't go less than 1.")
            if turn > 0:
                turn -= 1
                print('You lost one turn for a penalty. Do better next time.')
            if turn == 0:
                choice = input('You ran out of turns from penalties. Would you like to try again? ')
                if choice in ['Yes', 'yes']:
                    turn = 5
                elif choice in ['No','no']:
                    print('Hope to see you soon!')
                    break
                else:
                    print('Error! Your game is restarted by default.')
                    turn = 5
            number = select_number()
        elif guess < number:
            print('Too low. Try again.')
            turn -= 1
            if turn == 0:
                choice = input('You ran out of turns. Would you like to try again?')
                if choice in ['Yes', 'yes']:
                    turn = 5
                elif choice in ['No','no']:
                    print('Hope to see you soon!')
                    break
                else:
                    print('Error! Your game is restarted by default.')
                turn = 5
            else:
                print(f'You have {turn} turns left. This is round no. {round}')
            
        elif guess > number:
            print('Too high. Try again.')
            turn -= 1
            if turn == 0:
                choice = input('You ran out of turns. Would you like to try again?')
                if choice in ['Yes', 'yes']:
                    turn = 5
                elif choice in ['No','no']:
                    print('Hope to see you soon!')
                    break
                else:
                    print('Error! Your game is restarted by default.')
                turn = 5
            else:
                print(f'You have {turn} turns left. This is round no. {round}')
        elif guess == number:
            print('Correct! You get 1 point.')
            print(f'You have {turn} turns left. This is round no. {round}')
            point += 1
            round += 1
            turn = 5
            number = select_number()
    else:
        print('Try again. Your guess should be an integer between 1 and 100.')
        if turn > 0:
            turn -= 1
            print('You lost one turn for a penalty. Do better next time.')
        if turn == 0:
            choice = input('You ran out of turns from penalties. Would you like to try again? ')
            if choice in ['Yes', 'yes']:
                turn = 5
            elif choice in ['No','no']:
                print('Hope to see you soon!')
                break
            else:
                print('Error! Your game is restarted by default.')
                turn = 5
    
    
