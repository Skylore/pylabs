from ast import literal_eval

data = input().split()

def parseType(var):
    try:
        return type(literal_eval(var))
    except ValueError:
        return str

for i in range(len(data)):
    parseVar = parseType(data[i])
    data[i] = parseVar(data[i])

def sort(A):
    if len(A) <= 1:
        return A

    middle = int(len(A) / 2)
    left = sort(A[:middle])
    right = sort(A[middle:])

    return merge(left, right)

def merge(left, right):
    res = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
            left = left[1:]
        else:
            res.append(right[0])
            right = right[1:]

    if len(left) > 0:
        res += left
    if len(right) > 0:
        res += right

    return res

print(" ".join([str(i) for i in sort(data)]))
