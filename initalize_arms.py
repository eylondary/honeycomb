import os
import csv

arm1 = None
arm2 = None


def initialize_trial(animal_id):
    # Define the directory and file paths
    behaviour_directory = os.path.join(os.path.expanduser('~'), "Animal_Data")
    file_path = os.path.join(behaviour_directory, f"{animal_id}.csv")
    task_schedule_file = os.path.join(behaviour_directory, "task_schedule.csv")
    
    # Read the number of trials completed
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            num_trials = len(rows) - 1  # Exclude the header row
            
            if num_trials < 0:
                num_trials = 0
    except FileNotFoundError:
        num_trials = 0
    
    # Read the task schedule
    try:
        with open(task_schedule_file, 'r') as file:
            reader = csv.reader(file)
            schedule = list(reader)
            
            if not schedule or len(schedule) <= 1:
                raise ValueError("Task schedule file is empty or not properly formatted.")
            
            # Skip the header row
            schedule = schedule[1:]
    except FileNotFoundError:
        raise FileNotFoundError(f"Task schedule file not found: {task_schedule_file}")
    
    # Determine the next trial number
    next_trial_index = num_trials
    
    if next_trial_index >= len(schedule):
        raise ValueError("Not enough trials in the task schedule to proceed.")
    
    # Get the arms for the current trial
    arm1, arm2, direction = schedule[next_trial_index]
    print(f"Trial arms: {arm1} and {arm2}")
    
    return arm1, arm2

# Example usage
def main():
    animal_id = "1X"  # Example animal ID
    
    arm1, arm2 = initialize_trial(animal_id)
    print(f"Trial arms: {arm1} and {arm2}")

if __name__ == "__main__":
    main()
