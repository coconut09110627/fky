def find_max(data):
    max_number = data[0]
    for number in data:
        if number > max_number:
            max_number = number
    return max_number

data = [5, 3, 8, 1, 9, 2]
result = find_max(data)
print(result)