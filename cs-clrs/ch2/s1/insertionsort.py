import sys


def insertionSort(arr):

    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def insertionSortDescending(arr):

    for j in range(len(arr) - 2, -1, -1):
        key = arr[j]
        i = j + 1
        while i < len(arr) and arr[i] > key:
            arr[i - 1] = arr[i]
            i += 1
        arr[i - 1] = key
    return arr


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    # print(insertionSort(arr))
    print(insertionSortDescending(arr))

    arr = [31, 41, 59, 26, 41, 58]
    print(insertionSortDescending(arr))
