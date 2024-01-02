data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

def get_age(dictionary):
    return dictionary['age']

# Sorting the list by the key 'age' using the custom function
sorted_data = sorted(data, key='age')

print(sorted_data)
