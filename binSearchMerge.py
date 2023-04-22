def binSearch(i, A):
    low = 0
    high = len(A) - 1
    return binSearch_aux(A, int(i), low, high)

def binSearch_aux(A, i, l, h):
    while l <= h:
        mid = (l + h) // 2
        if A[mid] == i:
            return True
        elif A[mid] > i:
            return binSearch_aux(A, i, l, mid - 1)
        else:
            return binSearch_aux(A, i, mid + 1, h)
    return False

def main():

    import random
    from mergeSort import mergeSort


    Z = []

    for i in range(10):
        Z.append(random.randint(0, 99))

    print("Before: " + str(Z))
    print("After " + str(mergeSort(Z)))

    target = input("Enter target: ")

    if binSearch(target, Z) == True :
        print("Target found!")
    else:
        print("Target not present in list.")

main()