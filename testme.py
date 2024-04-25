from collections import Counter

TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def insertion_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i])

# Print TheData before sorting
print("Before sorting:")
print_array(TheData)      
# Q1(c) Calling function to sort the data
insertion_sort(TheData)

# Print TheData after sorting
print("After sorting:")
print_array(TheData)
#function to take input from the user and output found if the number is found in TheData and not Found if the number is not found in TheData
def search(TheData):
    NumberInput = int(input("Enter a whole number: "))
    if NumberInput in TheData:
        print("Found")
        return True
    else:
        print("Not found")
        return False