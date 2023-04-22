def InsertSort(A):

    X = A

    for i in range(1, len(X)):          # For the length of the Array, starting from elem 1
        x = X[i]                        # x is current element
        j = i - 1                       # j is past index

        while j >= 0 and X[j] > x:      # While j is not zero and X[j] is greater than x
            X[j + 1] = X[j]             # Next element is shifted up one
            j = j - 1                   # Moves backwards 1
        X[j + 1] = x                    # X[j+1] = x

    return X

def main():

    Z = [6,2,8,3,6,3]

    print("Before:  " + str(Z))


    Y = InsertSort(Z)

    print("After:   " + str(Y))

main()