def merge_sort(arr):
    if len(arr) > 1:
        # Split the list in half
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort each half
        merge_sort(left)
        merge_sort(right)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # If there are any remaining elements in the left half, add them to the result
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # If there are any remaining elements in the right half, add them to the result
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Test the merge_sort function
R = int(input("Enter the size of array:- "))
arr = []
print("array input")

for a in range(R):
    arr.append(int(input()))

print("array is as follows:- ", arr)
# sorting the array in acending order using merge sort
merge_sort(arr)
# printing the sorted array
print(arr)
