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
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


print(" ".join([str(i) for i in sort(data)]))