from ast import literal_eval

data = input().split()

def parseType(data):
    try:
        return type(literal_eval(data))
    except (ValueError, SyntaxError):
        return str

for i in range(len(data)):
    parse = parseType(data[i])
    data[i] = parse(data[i])

def sort(arr):
    for i in range(len(arr)):
        min = i

        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr

print(" ".join([str(i) for i in sort(data)]))