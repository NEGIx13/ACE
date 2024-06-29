import math


def find_pairs(numbers, target_sum):
    # Create a dictionary to store the pairs we find
    pairs = {}
    # Iterate through the numbers
    # numbers = (math.ceil(len(numbers)/2) + 1
    for num1 in range(math.ceil(len(numbers)//2)):
        # Calculate the second number needed to reach the target sum
        num2 = target_sum - numbers[num1]
        # If num2 is in the list of numbers, add the pair to the dictionary
        if num2 in numbers:
            pairs[num1 + 1] = num2
    # Return the dictionary of pairs
    return pairs


# Test the function
R = int(input("Enter the size of array:- "))
array = []
print("array input")

for i in range(R):
    array.append(int(input()))

print("array is as follows:- ", array)

target = int(input("enter target number:- "))
print(find_pairs(array, target))
