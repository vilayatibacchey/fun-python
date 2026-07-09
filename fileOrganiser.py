#---Planning and System Design---#

# What system am I designing? 
    # A secure and reusable file organization system.

# How to make the file organiser
    # First, we must get the folder or directory the user must organise through user input.
    # If it is not a folder or if it does not exist, we will return an error and ask them so type another folder.
    # Now, we need to access only the files in the folder.
    # Check the extension of each of them. Based on the extension, return a value (inside a hashmap).
    # If the extension does not find any value, our default folder name is "Others".
    # Make the folder with the name and move it into the main folder to organise if it does not exist already.
    # Finally, move the file into the folder.
    # Log/print the file name in the main folder and the new folder it got shifted to.

#-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#---Main Code---#

# Importing File Handling Modules
import os
import shutil

# Defining the class for reusability
class FileOrganiser:

    # Initiating the extension map (Can change in future)
    def __init__(self) -> None:
        self.extension_map = {".pdf" : "Documents", ".xls" : "Documents", ".xlsx" : "Documents", ".docx" : "Documents", ".txt" : "Documents", ".doc" : "Documents",
                                ".png" : "Images", ".jpeg" : "Images", ".jpg" : "Images", ".gif" : "Images", ".mp3" : "Audio", ".mp4" : "Audio", ".wav" : "Audio",
                                ".zip" : "Archives", ".exe" : "Executables", ".html" : "Programs", ".py" : "Programs", ".java" : "Programs", ".css" : "Programs", ".db" : "Database"}
    
    # Define organise function
    def organise(self, target_path):

        # Check if the path does not exist and if it is not a directory
        if not os.path.exists(target_path) or not os.path.isdir(target_path):
            print("Invalid path. Try again.")
            return False
        
        # Loop through the files in the directory
        for file_name in os.listdir(target_path):

            # Get the absolute path of the files
            file_path = os.path.join(target_path, file_name)

            # Check if it is a directory, if so, skip it
            if os.path.isdir(file_path):
                continue
            
            # Get the extension only (no need for the name) and lower it to bug-proof
            _ , file_extension = os.path.splitext(file_path)
            file_extension = file_extension.lower()

            # Get the folder name value from the extension hashmap
            folder_name = self.extension_map.get(file_extension, "Others")

            # Derive the folder path from the target folder to organise
            folder_path = os.path.join(target_path, folder_name)

            # Create the actual folder as long as it does not exist
            os.makedirs(folder_path, exist_ok=True)

            # Move the files into the folder and print the results
            shutil.move(file_path, folder_path)
            print(f"Moved {file_name} -> {folder_name}")

#-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

# Main Program
if __name__ == "__main__":
    organiser = FileOrganiser()
    
    # Main User Loop
    while True:
        # Get the target path through user input
        target_path = input("Please type a valid folder path to be organised: ")
        # Check if it returns an error
        if not organiser.organise(target_path):
                continue
        else:
            # Continue choice
            choice_to_continue = input("Continue? (y/n) ").strip().lower()
            if choice_to_continue == "n":
                print("Thank you for using this file organiser!")
                break