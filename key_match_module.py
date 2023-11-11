def find_by_key(value, key, data_set):
    data_set_match = []
    for obj in data_set:
        if key in obj and obj[key] == value:
            data_set_match.append(obj)
    return data_set_match


def find_by_key_range(min_value, max_value, key, data_set):
    data_set_match = []
    for obj in data_set:
        if key in obj and min_value <= float(obj[key]) <= max_value:
            data_set_match.append(obj)
    return data_set_match
