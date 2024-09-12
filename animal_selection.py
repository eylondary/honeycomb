#This script will prompt the user to select an animal ID and create a csv file to store the data for that animal ID.

import os
import csv

animal_id = None

#User selects Animal's ID via keyboard
def animal_selection():
    animal_ids = ['1X', '2X', '1Y', '2Y', '1W', '2W', '1Z', '2Z']

    #Prompt the user to select an animal ID
    while True:
        print("Please select an animal ID from the following list: 1X, 2X, 1Y, 2Y, 1W, 2W, 1Z, 2Z")
        animal_id = input("Enter the animal ID: ").strip()
        # .strip() strips any spaces from the user input to make the function work better.

        if animal_id in animal_ids:
            print(f"You have selected Animal {animal_id}.")
            return animal_id
        else:
            print(f"{animal_id} is not a valid Animal ID, please try again")

#Check if the csv file exists or create a new one
def process_animal_selection(animal_id):
    #Defines the directory to  Eylon/Animal_Data folder
    behaviour_directory = os.path.join(os.path.expanduser('~'), "Animal_Data")

    #Check if the directory exists, if not, create it
    if not os.path.exists(behaviour_directory):
        os.makedirs(behaviour_directory)
    
    #Define the file path based on the selected animal ID
    file_path = os.path.join(behaviour_directory, f"{animal_id}.csv")

    #Check if the file exists, if not, create it
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Arm 1", "Arm 2", "Correct?", " ", #Trial Data
                             "Arm 1 Lowered", "Arm 2 Lowered", "Prospective Goal Raised", "Connecting Raised", "Animal Choice", "Total Trial Time", " ",  #Timestamps 
                             "Delay 1 Settings", "Delay 2 Settings", "Delay 3 Settings", "Delay 4 Settings", " ", #Delay Settings
                             "Erratic?", "Jumped?", "Considered?", "Spinned?","Commments"]) #Behavioural Data
            print(f"File created at {file_path}")
    else:
        print(f"File already exists at {file_path}")
    return file_path


def main():
    animal_id = animal_selection() #This function will return the selected animal ID
    print(f"Selected Animal: {animal_id}") 
    process_animal_selection(animal_id) #This function will create the file if it doesn't exist

if __name__ == "__main__":
    main()