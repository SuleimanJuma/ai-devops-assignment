def sort_dicts_by_key(dicts, sort_key):
    return sorted(dicts, key=lambda d: d.get(sort_key, 0))

if __name__ == "__main__":
    data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie"}]
    sorted_data = sort_dicts_by_key(data, "age")
    print(sorted_data)