def sort(arr, base=10):
    if arr == []:
        return

    def key_factory(digit, base):
        def key(arr, index):
            return ((arr[index] // (base ** digit)) % base)

        return key

    largest = max(arr)
    exp = 0
    while base ** exp <= largest:
        arr = counting_sort(arr, base - 1, key_factory(exp, base))
        exp = exp + 1
    return arr


def counting_sort(arr, largest, key):
    c = [0] * (largest + 1)
    for i in range(len(arr)):
        c[key(arr, i)] = c[key(arr, i)] + 1

    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        result[c[key(arr, i)]] = arr[i]
        c[key(arr, i)] = c[key(arr, i)] - 1

    return result


print(" ".join([str(i) for i in sort(list(map(int, input().split())))]))