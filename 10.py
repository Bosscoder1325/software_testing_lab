def binsrc(x, low, high, key):
    mid = 0
    while low <= high:
        mid = (low+high) // 2

        if x[mid] == key:
            return mid
        elif x[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


n = int(input("Enter how many numbers you want to store"))

if n > 0:
    print(f"enter {n} numbers in ascending order")
    a = [int(x) for x in input().split()]

    key = int(input("Enter the key element to be searched"))
    res = binsrc(a, 0, n-1, key)

    if res >= 0:
        print(f"Element found in position = {res+1}")
    else:
        print("Element not found")

else:
    print("Number of element should be greater than zero")
