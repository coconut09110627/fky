def search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
        return -1


data = [5, 3, 8, 1, 9, 2]
result = search(data, 9)
print(result)
