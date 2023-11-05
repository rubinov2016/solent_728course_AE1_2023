def menu_value(choice, map_choice):
    key = map_choice[choice][0]
    value = input(f"Enter {key}:")
    labels = map_choice[choice][1]
    return key, value, labels

def menu_value_range(choice, map_choice):
    key = map_choice[choice][0]
    min_value = float(input("Enter minimal value:"))
    max_value = float(input(f"Enter maximal value above {min_value}:"))
    if max_value < min_value:
        print(f"Minimal {min_value} is higher than maximal {max_value}")
        exit()
    labels = map_choice[choice][1]
    return key, min_value, max_value, labels

def retrieve_from_CSV(path, choice, map_choice):
    import csv
    data_set = []
    with open(path, newline='') as device_features:
        csv_read = csv.DictReader(device_features)  # reader = csv.reader(f, delimiter=',')
        data_set = list(csv_read)
    # Found and print all found devices
    import key_match_module as key_match
    print()
    if map_choice[2]:
        key, min_value, max_value, labels = menu_value_range(choice, map_choice)
        result = key_match.find_by_key_range(min_value, max_value, key, data_set)
        print(f"We found {len(result)} device(s) with {key} between {min_value} and {max_value}")
    else:
        key, value, labels = menu_value(choice, map_choice)
        result = key_match.find_by_key(value, key, data_set)
        print(f"We found {len(result)} device(s) with {key} = {value}")

    # Build an output string
    for count, obj in enumerate(result):
        print_string = ""
        for count_label, obj_labels in enumerate(labels):
            print_string += labels[count_label] + ": " + obj[labels[count_label]] + "; "
        print(f"{count + 1} {print_string} ")