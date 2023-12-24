
def retrieve(path, condition):
    import csv
    import menu_module as menu
    import key_match_module as key_match
    data_set = []
    # Create a dictionary by pairing the header with the row values
    try:
        with open(path, newline='') as device_features:
            csv_read = csv.reader(device_features, delimiter=',')
            header = next(csv_read)
            for row in csv_read:
                row_dict = {header[i]: row[i] for i in range(len(header))}
                data_set.append(row_dict)
            # Alternate solution
            # csv_read = csv.DictReader(device_features)
            # data_set = list(csv_read)

        # Main filter
        key = condition[0]
        labels = condition[1]
        # Run the range function (flag=TRUE) or one-value function (FALSE)
        if condition[2]:
            min_value, max_value = menu.input_value_range(key)
            result = key_match.find_by_key_range(data_set=data_set, min_value=min_value, max_value=max_value, key=key)
            print(f"We found {len(result)} device(s) with {key} between {min_value} and {max_value}")
        else:
            value = menu.input_value(key)
            result = key_match.find_by_key(data_set=data_set,value=value, key=key)
            print(f"We found {len(result)} device(s) with {key} = {value}")
        # Build an output string
        for count, obj in enumerate(result):
            print_string = ""
            for count_label, obj_labels in enumerate(labels):
                print_string += labels[count_label] + ": " + obj[labels[count_label]] + "; "
            print(f"{count + 1} {print_string} ")

    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
    except IOError:
        print(f"Error: IO error occurred while opening {path} ")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    retrieve_condition = {0: ['oem_id',
                              ['model', 'manufacturer', 'weight_gram', 'price', 'price_currency'],
                              False],
                          1: ['codename',
                              ['brand', 'model', 'ram_capacity', 'market_regions', 'info_added_date'],
                              False],
                          2: ['ram_capacity',
                              ['oem_id', 'released_date', 'announced_date', 'dimensions', 'device_category'],
                              False],
                          # Can work with range of values
                          3: ['weight_gram',
                              ['hardware_designer', 'display_diagonal', 'sim_card_slot', 'weight_gram'],
                              True]}
    retrieve(path="device_features.csv", condition=retrieve_condition[3])
