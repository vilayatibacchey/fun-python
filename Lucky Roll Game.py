from random import randint

def roll():
    max = input('How many sides on your dice?:')
    print(f'You have a D {max}')
    rollnumber = randint(1,int(max))
    print(f'You have rolled a {rollnumber} {"hehe" * rollnumber}!\n')

while True:
    print("Wanna try a lucky roll?")
    answer = input("Yes or No?:\n")
    if str(answer) == "Yes" or str(answer) == 'yes':
        roll()
    if str(answer) == "No" or str(answer) == 'no':
        print("I guess another day!")
        print('Bye!')
        break
    else:
        print("ERROR! Try again.")

