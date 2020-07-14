# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    result = []
    while (arrA and arrB):
        if arrA[0] < arrB[0]:
            result.append(arrA[0])
            arrA.pop(0)
        else:
            result.append(arrB[0])
            arrB.pop(0)

    if arrA:
        result += arrA
    if arrB:
        result += arrB

    return result

   

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2
    left_split = arr[:middle_index]
    right_split = arr[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

