def construct_margeTop(topSize):

    margeTop = generate_sequence(topSize)  # Generate the squence
    print(margeTop)

def generate_sequence(max_length):
    sequence = []
    length = 3
    indent = max_length - length  # start with maximum indentation
    while length <= max_length:
        section = " " * indent + "(" + "#" * length + ")"
        sequence.append(section)
        length += 2
        indent -= 2  # reduce the indentation by 2 for the next section
    return "\n".join(sequence)

def merge_sort(arr, depth=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_part = arr[:mid]
        right_part = arr[mid:]

        merge_sort(left_part, depth + 1)
        merge_sort(right_part, depth + 1)

        i = j = k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1

        print("       (", arr , ")")

    return arr

def main():

    import random

    artTop = '''
            (####)
          (#######)
        (#########)'''

    artBtm = '''       (#########)
      (#########)
     (#########)
    (#########)
   (#########)
  (#########) 
   (o)(o)(##)
 ,_C     (##)
/___,   (##)    
  \     (#) 
   |    |   
   OOOOOO  
  /      \
'''

    Z = []

    for i in range(9):
        Z.append(random.randint(0, 99))

    zSize = len(str(Z))

    print("Before: " + str(Z))

    construct_margeTop(zSize)   # Construct marge from the top
    print("(" +Z)

    # Do merge sort


    # Construct marge from bottom

    merge_sort(Z)

    print(artBtm)


    print("After " + str(Z))

main()