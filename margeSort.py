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

    art_top = '''
            (####)
          (#######)
        (#########)'''

    art_bottom = '''       (#########)
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

    random_numbers = []

    for _ in range(9):
        random_numbers.append(random.randint(0, 99))

    print("Before: " + str(random_numbers))

    print("Merge Sort!!\n", art_top)
    merge_sort(random_numbers)
    print(art_bottom)

    print("After " + str(random_numbers))

main()
