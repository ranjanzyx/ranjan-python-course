# Write a program to traverse a dictionary with an unknown level of nesting and print each key-value pair.

def traverse_dict(d):
    for key, value in d.items():
        if isinstance(value, dict):
            traverse_dict(value)  # It's a dictionary, so perform recursion.
        else:
            print(f"{key}: {value}")

# Example usage:
nested_dict = {
    'key1': 'value1',
    'key2': {
        'key3': 'value3',
        'key4': {
            'key5': 'value5'
        }
    }
}

traverse_dict(nested_dict)