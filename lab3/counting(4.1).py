def sort(array, maxval):
    n = len(array)
    m = maxval + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array

arr = list(map(int, input().split()))
print(" ".join([str(i) for i in sort(arr, max(arr))]))