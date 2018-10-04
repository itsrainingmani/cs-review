def merge(a, p, q, r):
    l = a[p : q + 1]
    r = a[q + 1 : r]
    print(l, r)

    # for i in range(p, r+1):
    #     if l[]
    return a


if __name__ == "__main__":
    arr = [1, 5, 2, 4, 3, 7, 6, 2, 4, 1, 5, 3, 8]
    print(merge(arr, 2, 5, 10))

