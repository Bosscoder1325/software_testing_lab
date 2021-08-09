def quickSort(arr, first, last):
    if first < last:
        pivot = first
        i = first
        j = last

        while i < j:
            while arr[i] <= arr[pivot] and i < last:
                i += 1
            while arr[j] > arr[pivot]:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot], arr[j] = arr[j], arr[pivot]
        quickSort(arr, first, j-1)
        quickSort(arr, j+1, last)


def driver():
    n = int(input("enter size: "))
    arr = []

    if n > 0:
        for i in range(n):
            arr.append(int(input()))

        quickSort(arr, 0, n-1)
        print("element in sorted array is: ")

        print(arr)
    else:
        print("size invalid ")


driver()
