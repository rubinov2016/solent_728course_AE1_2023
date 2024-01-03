# Returns a file name and path
def input_file_path(default_path, max_path_attempts):
    # default_path - file name by default
    # max_path_attempts - max number of attempts to find the file
    import os.path
    file_found = False
    path = ""
    i = 1
    while i <= max_path_attempts and file_found == False:
        path = input(f"Please provide the path to the CSV file ({default_path} by default):")
        # If path is empty we use current folder and file "device_features.csv"
        if path == "":
            path = default_path
        if os.path.isfile(path):
            print(f"File is found: {path} ")
            file_found = True
        else:
            print(f"There is no file: {path}. You have {max_path_attempts - i} attempts")
            i += 1
    return path


# Returns the index number of the selected menu option
def input_choice(choice_list):
    # choice_list - dataset with possible menu options
    print()
    for count, action in enumerate(choice_list):
        print(f"Press {count} to {action}")
    while True:
        try:
            print()
            choice = int(input(f"Press from 0 to {len(choice_list) - 1} (exit): "))
            if choice in range(0, len(choice_list)):
                print()
                print(f"You choose: {choice_list[choice]}")
                break
            else:
                print()
                print("Your choice is out of bounds")
        except:
            print()
            print("That's not a valid option!")
    return choice


# Returns a value
def input_value(key):
    value = input(f"Enter {key}:")
    return value


# Returns two values
def input_value_range(key):
    min_value = float(input(f"Enter minimal value of {key}:"))
    max_value = min_value-1
    while max_value < min_value:
        max_value = float(input(f"Enter maximal value above {min_value}:"))
    return min_value, max_value


# Returns a value
def input_feature(df, filter_feature):
    # df - dataset to filter
    # filter_feature - name of the feature to filter
    distinct_feature = df[filter_feature].unique()
    print(f"Choose the {filter_feature} from the following:")
    print(distinct_feature)
    # value - value of the feature to filter
    value = input_value(filter_feature)
    return value
