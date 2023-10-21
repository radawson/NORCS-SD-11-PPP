"""
Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

>>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
"""
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

"""
Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.

>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
"""
def unflatten_dict(d, sep='.'):
    result = {}
    for key, value in d.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result

"""
Problem 3: Write a function treemap to map a function over nested list.

>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
"""
def treemap(f, nested_list):
    if isinstance(nested_list, list):
        return [treemap(f, x) for x in nested_list]
    else:
        return f(nested_list)

if __name__ == "__main__":
    print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
    print("_" *40)
    print(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
    print("_" *40)
    print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]))