def quicksort(array):
    if len(array) < 1:
        return []
    pivot = list()
    pivot.append(array[0])
    left = list()
    rigth = list()

    for i in range(1, len(array)):
        if array[i] < pivot[0]:
            left.append(array[i])
        else:
            rigth.append(array[i])

    return quicksort(left) + pivot + quicksort(rigth)


def main():
    print(quicksort([1, 5, 9, 5, 1, 0, 8]))


if __name__ == "__main__":
    main()
