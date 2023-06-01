def merge_sorted_arrays(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += (a[i:])
    c += (b[j:])
    return c


print(merge_sorted_arrays([1, 4, 6, 7], [1, 2, 3, 4, 5, 6, 7]))
