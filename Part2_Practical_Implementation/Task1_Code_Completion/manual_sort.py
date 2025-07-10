

# manual_sort.py
def sort_dicts_by_key(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda x: x[key])

if __name__ == "__main__":
    data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
    sorted_data = sort_dicts_by_key(data, "age")
    print(sorted_data)
# Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]