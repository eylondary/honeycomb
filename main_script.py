from animal_selection import animal_selection, process_animal_selection
from initalize_arms import initialize_trial

def main():
    animal_id = animal_selection()
    process_animal_selection(animal_id)
    
    arm1, arm2 = initialize_trial(animal_id)

if __name__ == "__main__":
    main()
    