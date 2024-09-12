#ONLY USE THIS FUNCTION IF YOU WOULD LIKE TO OVERRITE THE EXISTING TASK SCHEDULE AND CREATE A NEW ONE



import os
import random
import csv

def generate_task_schedule(num_trials):
    if num_trials % 12 != 0:
        raise ValueError("Number of trials must be a multiple of 12 for equal distribution.")

    clockwise_pairs = [('N', 'SE'), ('NE', 'S'), ('SE', 'SW'), ('S', 'NW'), ('SW', 'N'), ('NW', 'NE')]
    anti_clockwise_pairs = [('N', 'SW'), ('NW', 'S'), ('SW', 'SE'), ('S', 'NE'), ('SE', 'N'), ('NE', 'NW')]

    total_pairs = len(clockwise_pairs) + len(anti_clockwise_pairs)
    pairs_per_type = num_trials // total_pairs

    scheduled_pairs = []
    scheduled_pairs.extend(clockwise_pairs * pairs_per_type)
    scheduled_pairs.extend(anti_clockwise_pairs * pairs_per_type)

    random.shuffle(scheduled_pairs)

    schedule = []
    recent_pairs = []
    recent_directions = []

    def get_available_pairs(current_direction):
        return [pair for pair in (clockwise_pairs if current_direction == 'Clockwise' else anti_clockwise_pairs)
                if pair not in recent_pairs]

    def get_direction(pair):
        return 'Clockwise' if pair in clockwise_pairs else 'Anti-clockwise'

    for _ in range(num_trials):
        if len(recent_directions) >= 3 and recent_directions[-3] == recent_directions[-2] == recent_directions[-1]:
            current_direction = 'Clockwise' if recent_directions[-1] == 'Anti-clockwise' else 'Anti-clockwise'
        else:
            current_direction = random.choice(['Clockwise', 'Anti-clockwise'])

        available_pairs = get_available_pairs(current_direction)

        if not available_pairs:
            current_direction = 'Clockwise' if current_direction == 'Anti-clockwise' else 'Anti-clockwise'
            available_pairs = get_available_pairs(current_direction)

        pair = random.choice(available_pairs)
        schedule.append((pair[0], pair[1], current_direction))

        recent_pairs.append(pair)
        recent_directions.append(current_direction)

        if len(recent_pairs) > 2:
            recent_pairs.pop(0)
        if len(recent_directions) > 3:
            recent_directions.pop(0)

    # Define the path where you want to save the file
    schedule_directory = os.path.join(os.path.expanduser("~"), "Animal_Data")
    if not os.path.exists(schedule_directory):
        os.makedirs(schedule_directory)

    csv_file = os.path.join(schedule_directory, "task_schedule.csv")
    
    # Save to CSV
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Arm 1', 'Arm 2', 'Direction'])
        writer.writerows(schedule)

    print(f"Task schedule saved to {csv_file}")

# Example usage
def main():
    num_trials = 300  # Adjust as needed
    generate_task_schedule(num_trials)

if __name__ == "__main__":
    main()
