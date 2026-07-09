import time
import os
count = 0

# Gets the person's name and removes any extra leading/trailing spaces
def get_name():
    name = input('What is your name? ').strip(' ')
    return name

def write(msg : str,username : str):
    # Moving the time check INSIDE the function ensures it grabs the exact moment they hit enter
    local_struct = time.localtime()
    current_local_time = time.strftime("%m-%d-%Y" , local_struct)
    
    folder_name = 'diaries'
    os.makedirs(folder_name,exist_ok=True)

    file_path = os.path.join(folder_name,f"{username}'sdiary.txt")


    # Open in 'a' mode just for writing, then safely close automatically
    with open(file_path, "a") as userdiary:
        userdiary.write(f"Dear diary,\n{msg} | Date: {current_local_time}\n\n")

def read_diary(username : str):
    folder_name = 'diaries'
    file_path = os.path.join(folder_name,f"{username}'sdiary.txt")
    # Open in 'r' mode just for reading
    try:
        with open(file_path, "r") as userdiary:
            content = userdiary.read()
            print(content)
    except FileNotFoundError:
        print("Your diary is empty! Try writing an entry first.")

# --- Main Program ---
username = get_name()
print(f'Welcome, {username}, to your personal diary application.')

while True:
    choice = input('\nWould you like to:\na) Write a new entry\nb) Read past entries\nc) Exit\nChoice: ').lower()
    
    if choice == 'a':
        message = input('Type what you want to enter in your diary: ')
        write(message,username)
        print("Entry saved!")
        
    elif choice == 'b':
        print('\n--- Sure, here is your diary written so far ---')
        read_diary(username)
        print('------------------------------------------------')
        
    elif choice == 'c':
        print('Hope to see you back soon!')
        break
    else:
        print("Invalid choice, please type a, b, or c.")