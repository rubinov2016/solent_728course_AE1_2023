# Filter by one value
def find_by_key(data_set, value, key):
    data_set_match = []
    for obj in data_set:
        if key in obj and obj[key] == value:
            data_set_match.append(obj)
    return data_set_match


# Filter by the range
def find_by_key_range(data_set, min_value, max_value, key):
    data_set_match = []
    for obj in data_set:
        if key in obj and min_value <= float(obj[key]) <= max_value:
            data_set_match.append(obj)
    return data_set_match
