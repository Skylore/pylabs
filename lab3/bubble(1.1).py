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
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(" ".join([str(i) for i in sort(data)]))