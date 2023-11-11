


def retrieve(path, choice, retrieve_condition):
    import csv
    import menu_module as menu
    data_set = []
    with open(path, newline='') as device_features:
        csv_read = csv.DictReader(device_features)  # reader = csv.reader(f, delimiter=',')
        data_set = list(csv_read)
    # Found and print all found devices
    import key_match_module as key_match
    print()
    if not retrieve_condition:
        print("Analyse and Visualize")
    else:
        key = retrieve_condition[0]
        labels = retrieve_condition[1]
        # Select range function (TRUE) or exact value (FALSE)
        if retrieve_condition[2]:
            min_value, max_value = menu.input_value_range(key)
            result = key_match.find_by_key_range(min_value, max_value, key, data_set)
            print(f"We found {len(result)} device(s) with {key} between {min_value} and {max_value}")
        else:
            value = menu.input_value(key)
            result = key_match.find_by_key(value, key, data_set)
            print(f"We found {len(result)} device(s) with {key} = {value}")
        # Build an output string
        for count, obj in enumerate(result):
            print_string = ""
            for count_label, obj_labels in enumerate(labels):
                print_string += labels[count_label] + ": " + obj[labels[count_label]] + "; "
            print(f"{count + 1} {print_string} ")
