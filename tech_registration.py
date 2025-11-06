# Task 1
print("Welcome to SMIT TechFest!")
print("Organized by Denniel Enraca of APPDAET BTCS2")
print()

number_of_participants = int(input("How many participants will register? "))

# Task 2
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

# Task 3
    unique_tracks = set()
    for participant in participants:
        unique_tracks.add(participant['track'])

    tracks_list = sorted(list(unique_tracks))
    print("\nTracks offered in this event:")
    print(", ".join(tracks_list))

    if len(unique_tracks) < 2:
        print("Not enough variety in tracks.")

# Task 4
    detected_names = set()
    duplicate_found = False
    duplicate_name = None

    for participant in participants:
        name = participant['name']
        if name in detected_names:
            duplicate_found = True
            duplicate_name = name
            break
        detected_names.add(name)

    if duplicate_found:
        print(f"\nDuplicate name found: {duplicate_name}")
    else:
        print("\nNo duplicate names.")