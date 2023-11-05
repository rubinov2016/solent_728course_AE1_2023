def menu_file_path():
    import os.path
    # Query the file path
    i = 1
    # The number of attempts to enter value in the loop
    file_found = False
    path = ""
    max_attempts = 5
    while i <= max_attempts and file_found == False:
        path = input("Please provide the path to the CSV file (device_features.csv by default):")
        # If path is empty we use current folder and file "device_features.csv"
        if path == "":
            path = "device_features.csv"
        if os.path.isfile(path):
            print(f"File is found: {path} ")
            file_found = True
        else:
            print(f"There is no file: {path}. You have {max_attempts - i} attempts")
            i += 1
    return path


def menu_retrieve_choice(action_list):
    print()
    for count, action in enumerate(action_list):
        print(f"Press {count} to {action}")
    choice = int(input(f"Press from 0 to {len(action_list) - 1}: "))

    if choice in range(0, len(action_list)):
        print()
        print(f"You choose: {action_list[choice]}")
    else:
        print()
        print("Your choice is out of bounds")
    return choice
