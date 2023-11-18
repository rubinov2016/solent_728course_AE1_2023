def input_file_path(default_path):
    import os.path
    # Query the file path
    i = 1
    # The number of attempts to enter value in the loop
    file_found = False
    path = ""
    max_attempts = 5
    while i <= max_attempts and file_found == False:
        path = input(f"Please provide the path to the CSV file ({default_path} by default):")
        # If path is empty we use current folder and file "device_features.csv"
        if path == "":
            path = default_path
            # path = "device_features.csv"
        if os.path.isfile(path):
            print(f"File is found: {path} ")
            file_found = True
        else:
            print(f"There is no file: {path}. You have {max_attempts - i} attempts")
            i += 1
    return path


def input_choice(action_list):
    print()
    for count, action in enumerate(action_list):
        print(f"Press {count} to {action}")
    while True:
        try:
            choice = int(input(f"Press from 0 to {len(action_list) - 1} (exit): "))
            if choice in range(0, len(action_list)):
                print()
                print(f"You choose: {action_list[choice]}")
                break
            else:
                print()
                print("Your choice is out of bounds")
        except:
            print("That's not a valid option!")
    return choice


def input_value(key):
    value = input(f"Enter {key}:")
    return value


def input_value_range(key):
    min_value = float(input(f"Enter minimal value of {key}:"))
    max_value = min_value
    while max_value <= min_value:
        max_value = float(input(f"Enter maximal value above {min_value}:"))
    return min_value, max_value
