#---Planning and System Design---#

# What system am I building?
    # A file-organiser because me and my friends are lazy.

# How to make a file organiser:
    # Loop through all my files in a specific path:
        # Use shutil utilies to move my files to different specified path.
        # Print a message with the name of the file and where it was moved.

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#---Main Code---#

# Importing modules for file handling
import os
import shutil

class fileOrganiserwJasan:

    def __init__(self) -> None:
        self.initial_path = ""
        self.destination_path = ""

    def getPaths(self) -> None:
            initial_path = input("Type the initial path of the directory in which the files you wish to shift: ")
            destination_path = input("Type the destination path: ")

            self.initial_path = initial_path
            self.destination_path = destination_path

    def validatePaths(self):
        if os.path.exists(self.initial_path) and os.path.isdir(self.initial_path) and os.path.exists(self.destination_path) and os.path.isdir(self.destination_path):
            print("Success! Organising...")
        else:
            print("Try a different path.")
            return False

        return True
    
    def organise(self):
        for file_name in os.listdir(self.initial_path):
            file_path = os.path.join(self.initial_path, file_name)
            shutil.move(file_path, self.destination_path)
            print(f"Moved {file_name} -> {self.initial_path}")
        os.rmdir(self.initial_path)
        print("Done!")

while True:
    organiser = fileOrganiserwJasan()

    organiser.getPaths()
    if not organiser.validatePaths():
        continue
    else:
        organiser.organise()
