# Input for number of trainees
num_trainees = 3

# Initialize lists to store oxygen levels for each round and average oxygen levels
round1_oxygen = []
round2_oxygen = []
round3_oxygen = []
avg_oxygen = []

# Input oxygen levels for each trainee and round
for i in range(num_trainees):
    print(f"\nTrainee {i+1}:")
    
    while True:
        round1_oxygen_input = int(input("Enter oxygen level after round 1: "))
        if 1 <= round1_oxygen_input <= 100:
            round1_oxygen.append(round1_oxygen_input)
            break
        else:
            print("Invalid input. Oxygen level should be between 1 and 100.")
    
    while True:
        round2_oxygen_input = int(input("Enter oxygen level after round 2: "))
        if 1 <= round2_oxygen_input <= 100:
            round2_oxygen.append(round2_oxygen_input)
            break
        else:
            print("Invalid input. Oxygen level should be between 1 and 100.")
    
    while True:
        round3_oxygen_input = int(input("Enter oxygen level after round 3: "))
        if 1 <= round3_oxygen_input <= 100:
            round3_oxygen.append(round3_oxygen_input)
            break
        else:
            print("Invalid input. Oxygen level should be between 1 and 100.")

# Calculate average oxygen level for each trainee
for i in range(num_trainees):
    avg_oxygen.append(round((round1_oxygen[i] + round2_oxygen[i] + round3_oxygen[i]) / 3))

# Find the highest average oxygen level
max_avg_oxygen = max(avg_oxygen)

# Check if all trainees are unfit
if max_avg_oxygen < 70:
    print("All trainees are unfit.")
else:
    # Find the most fit trainee(s)
    most_fit_trainees = []
    for i in range(num_trainees):
        if avg_oxygen[i] == max_avg_oxygen:
            most_fit_trainees.append(i+1)

    # Display the most fit trainee(s) and the highest average oxygen level
    if len(most_fit_trainees) > 1:
        print("Most fit trainees:", most_fit_trainees)
    else:
        print("Most fit trainee:", most_fit_trainees[0])
    print("Highest average oxygen level:", max_avg_oxygen)