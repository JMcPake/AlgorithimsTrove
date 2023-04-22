def mergeSort(A):

    n = len(A)

    if n <= 1 :                     # If the list is 1 element long, return A
        return A

    else:

        mid = int(n / 2)            # Mark the middle point of A
        lA = mergeSort(A[:mid])     # Slice the left half of A
        rA = mergeSort(A[mid:])     # Slice the right half of A

        return merge(lA,rA)

def merge(lA, rA):

    result = []     # empty array for result
    i = 0           # set dual counters to 0
    j = 0

    while (i < len(lA) and j < len(rA)):    # While i within left and j within right
        if (lA[i] <= rA[j]):                # If left is smaller than or equal to right for i and j
            result.append(lA[i])            # Append the left to result and incrament i
            i += 1
        else:                               # If the right is smaller than the left 
            result.append(rA[j])            # Append the right to the result and incrament j
            j += 1
    while (i < len(lA)):                    # While i is within the left
        result.append(lA[i])                # Append the left to the result
        i += 1
    while (j < len(rA)):                    # While j is within the right
        result.append(rA[j])                # Append the right to the result
        j += 1
    
    return result                           # Return the result

def main():

    Z = [6,2,8,3,6,3]

    print("Before:  " + str(Z))


    Y = mergeSort(Z)

    print("After:   " + str(Y))

main()