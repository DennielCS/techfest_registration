print("Welcome to SMIT TechFest!")
print("Organized by Denniel Enraca of APPDAET BTCS2")
print()

number_of_participants = int(input("How many participants will register? "))

if number_of_participants <= 0:
    print("Invalid number of participants.")
else:
    participants = []

    for i in range(number_of_participants):
        name = input("Enter participant name: ")
        track = input("Enter chosen track: ")

        participant = {"name": name, "track": track}
        participants.append(participant)

    print("\nRegistered Participants:")
    for i, participant in enumerate(participants, 1):
        print(f"{i}. {participant['name']} - {participant['track']}")
