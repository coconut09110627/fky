def sort_list(data):
    n = len(data)
    for i in range(len(data)):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

data = [5, 3, 8, 1, 9, 2]
result = sort_list(data)
print(result)