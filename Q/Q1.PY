# Defines an array as a local variable
from typing import Self


TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

# Performs insertion on the data in TheData
def InsertionSort(TheData):
    for count in range(0, len(TheData)):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
                Inserted = 1
            else:
                break

# Calling function to sort the data
def PrintArray(TheData):
    for count in range(0, len(TheData)):
        print(TheData[count])

# Print TheData before sorting
print("Before")
PrintArray(TheData)

# Calling function to sort the data
InsertionSort(TheData)

# Print TheData after sorting
print("After")
PrintArray(TheData)

# Write a function that takes a whole number as input from the user
def Search(TheData):
    NumberInput = int(input("Enter a whole number: "))
    for count in range(0, len(TheData)):
        if TheData[count] == NumberInput:
            print("Found")
            return True
    print("Not found")
    return False
Search(TheData)

   